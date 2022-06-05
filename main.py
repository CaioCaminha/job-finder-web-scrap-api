from bs4 import BeautifulSoup
import requests

indeed_url_search_page = 'https://www.indeed.com/jobs?q&l=Remote&sc=0kf%3Aattr(DSQF7)jt(contract)%3B&rbl=Remote&jlid=aaa2b906602aa8f5&fromage=1'
indeed_url_job_page = 'https://www.indeed.com/viewjob'

def find_jobs():


    html_text = requests.get(indeed_url_search_page).text
    soup = BeautifulSoup(html_text, 'lxml')
    job_list = soup.find('ul', class_='jobsearch-ResultsList')


    jobs = []

    for job_element in job_list:
        job = {

        }

        div_title = job_element.find('h2', class_='jobTitle jobTitle-color-purple jobTitle-newJob')
        title = ''
        company = job_element.find('span', class_='companyName')
        job_id = ''

        if div_title is not None and company is not None:
            title = div_title.a.span.text

            job_id = div_title.a['id'].replace('job_', '')
            url = f'{indeed_url_job_page}?jk={job_id}'

            html_job_page = requests.get(url).text
            job_soup = BeautifulSoup(html_job_page, 'lxml')
            job_description = job_soup.find(id='jobDescriptionText').text
            #print(url)

            job["Description"] = job_description.strip()
            job["JobUrl"] = url
            job["Title"] = title
            job["Company"] = company.text
        jobs.append(job)


    print(jobs)







find_jobs()