import scraper2
import pytest
import sys

def test_html_text_text():
    assert type(scraper2.html_text) is str

@pytest.mark.xfail
def test_date_added_today():
    assert scraper2.date_posted[0] == 'T' # can fail if the date added is not 'Today'

def test_job_desc_added():
    assert scraper2.job_description[1] != None

@pytest.mark.xfail
def test_company_name_working():
    assert scraper2.company_name[1] == 'Apple' # fails as it should

@pytest.mark.skipif(sys.version_info < (3, 10), reason="requires python3.10 or higher")
def test_city_added():
    assert scraper2.location[0] == 'P' 


def test_full_part_time_working():
    assert scraper2.full_part_time[0] == 'F'

def test_languages_output():
    assert scraper2.languages[0] == 'E'

def test_more_info_output():
    assert scraper2.more_info[1] != None
