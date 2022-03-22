from bs4 import BeautifulSoup
import requests
import pandas as pd


html_text = requests.get('https://www.expats.cz/jobs/offers/it-itc').text
soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all('article')


job_dict = []

for job in jobs:
    date_posted = job.find('div', {"class": ['extras logo', 'extras no-logo']}).find('span').text
    #optional. Only include jobs posted today or yesterday:
    #if 'Today' in date_posted or 'Yesterday' in date_posted:
#    print(date_posted) - works fine
    job_description = job.find('h3').text
#    print(job_description) - fine

#    parent = soup.find('div', class_='info').find_all('a')
    #print(parent)
## another way to find a tags:
    for tag in soup.find_all('div', {'class' : 'info'}):
        anchor = tag.find_all('a')
        text = list(anchor)
#        print(text)
    for i in range(len(text)):
        company_name = text[1].text
        location = text[2].text
        full_part_time = text[0].text
        #print(company_name) #--good
        #print(location[11]) #--good
        # print(full_part_time)
    parent2 = job.find_all('span', class_='lang')
    lang = list(parent2)
#    print(lang)
    languages = ('')
    for i in range(len(lang)):
        languages = (lang[i].text.strip() + " " + "," + languages)




    more_info = f"expats.cz{job.div.h3.a['href']}"


    print(f"Job Description: {job_description.strip()}")
    print(f"Company name: {company_name.strip()}")
    print(f"Full-time or part-time?: {full_part_time.strip()}")
    print(f"Location: {location.strip()}")
    print(f"Required languages: {languages.strip()}")
    print(f"Date posted: {date_posted.strip()}") #- not needed if were filtering by date already
    print(f"More info: {more_info.strip()}")
    print("")

    job_dict.append( {
        'Job description': job_description,
        'Company name': company_name,
        'Full/Part-time': full_part_time,
        'Location': location,
        'Required Languages': languages,
        'Date': date_posted,
        'More info': more_info
    }  )
expats_data = pd.DataFrame(job_dict)
expats_data.to_csv('expats.csv', index=None)
