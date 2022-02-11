from bs4 import BeautifulSoup
import requests
print('Do you want to work Full-time or Part-time?')
des_avail = input('>')
print('What languages do you speak?')
des_lang = input('>')
print('What city would you like to work in?')
des_loc = input('>')
print(f'Filtering by these parameters: {des_loc}, {des_lang}, {des_avail}')
print("")

html_text = requests.get('https://www.expats.cz/jobs/offers/it-itc').text
soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all('article')
for job in jobs:
    date_posted = job.find('div', {"class": ['extras logo','extras no-logo']}).find('span').text
    #optional. Only include jobs posted today or yesterday:
    #if 'Today' in date_posted or 'Yesterday' in date_posted:

    job_description = job.find('h3').text
    parent = soup.find('article').find_all('a')
    text = list(parent) # not neccessary, just in case
    for i in range(3, len(text), 3):
        company_name = text[i].text
    for i in range(2, len(text), 3):
        full_part_time = text[i].text
    for i in range(2, len(text), 2):
        location = text[i].text
    parent2 = job.find_all('span', class_='lang')
    lang = list(parent2)
    languages = ('')
    for i in range(len(lang)):
        languages = (lang[i].text.strip() + " " + "," + languages)
    more_info = job.div.h3.a['href']
    if des_loc in location and des_lang in languages and des_avail in full_part_time:

        print(f"Job Description: {job_description.strip()}")
        print(f"Company name: {company_name.strip()}")
        print(f"Full-time or part-time?: {full_part_time.strip()}")
        print(f"Location: {location.strip()}")
        print(f"Required languages: {languages}")
        print(f"Date posted: {date_posted.strip()}") #- not needed if were filtering by date already
        print(f"More info: {more_info.strip()}")
        print("")
