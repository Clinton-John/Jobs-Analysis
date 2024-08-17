from bs4 import BeautifulSoup
import requests

import pandas as pd 


def get_webpage():
    scrape_url = "https://www.brightermonday.co.ke/jobs?experience=entry-level"
    page_response = requests.get(scrape_url)
    soup = BeautifulSoup(page_response.text, 'html.parser')

    return soup


def get_fields(soup):
    jobs_page = soup.find_all('div', class_ ='mx-5 md:mx-0 flex flex-wrap col-span-1 mb-5 bg-white rounded-lg border border-gray-300 hover:border-gray-400 focus-within:ring-2 focus-within:ring-offset-2 focus-within:ring-gray-500' )
    #number of jobs per page
    jobs_count = len(jobs_page)

    
    job_titles = [title.text.strip() for title in soup.find_all('p', class_='text-lg font-medium break-words text-link-500')]
    companies = [company.text.strip() for company in soup.find_all('p', class_='text-sm text-link-500')]
    lctn_type_salaries = [lctn_type_salary.text.strip() for lctn_type_salary in soup.find_all('div', class_='flex flex-wrap mt-3 text-sm text-gray-500 md:py-0')]
    job_functions = [job_function.text.strip() for job_function in soup.find_all('p', class_='text-sm text-gray-500 text-loading-animate inline-block')]
    date_posted = [date_posted.text.strip() for date_posted in soup.find_all('p', class_='ml-auto text-sm font-normal text-gray-700 text-loading-animate')]
    job_descriptions = [job_description.text.strip() for job_description in soup.find_all('p', class_='text-sm font-normal text-gray-700 md:text-gray-500 md:pl-5')]

    # Create a DataFrame
    jobs_df1 = pd.DataFrame({
        'job_title': job_titles,
        'company': companies,
        'lctn_type_salary': lctn_type_salaries,
        'job_function': job_functions,
        'date_posted': date_posted,
        'job_description': job_descriptions
    })

    # print(jobs_df1.head())

    return jobs_df1


def main():
    soup = get_webpage()
    list_fields = get_fields(soup)
    print(f"There are {list_fields} in the WebPage")
    jobs_df = get_fields(soup)
    print(jobs_df.head())
 

if __name__ == '__main__':
    main()


