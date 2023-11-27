from bs4 import BeautifulSoup
import requests
import time
import csv

print('put some skill that you are not familer with')
unfamilier_skill = input('>')
print(f'Filtering out: {unfamilier_skill}')

def find_jobs():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Data+Scientist&txtLocation=Bengaluru%2F+Bangalore').text

    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li',class_='clearfix job-bx wht-shd-bx')
    # for index ,job in enumerate(jobs):
    #     published_date = job.find('span', class_ = 'sim-posted').span.text
    #     if 'few' in published_date:
    #         company_name = job.find('h3', class_ = 'joblist-comp-name').text.replace(' ','')# replace empty with nothin
    #         skills = job.find('span', class_ = 'srp-skills').text.replace(' ','')
    #         more_info = job.header.h2.a['href']
    #         if unfamilier_skill not in skills:
    #             with open(f'posts/{index}.txt','w') as f:
    #                 f.write(f'Company Name : {company_name.strip()} \n')
    #                 f.write(f'Requried Skill : {skills.strip()} \n')
    #                 f.write(f'More Info: {more_info}')
    #             print(f'File saved : {index}')

    with open('posts/jobs.csv', 'w', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['Company Name', 'Required Skill', 'More Info'])

        for index, job in enumerate(jobs):
            published_date = job.find('span', class_='sim-posted').span.text
            if 'few' in published_date:
                company_name = job.find('h3', class_='joblist-comp-name').text.strip()
                skills = job.find('span', class_='srp-skills').text.strip()
                more_info = job.header.h2.a['href']
                if unfamilier_skill not in skills:
                    csv_writer.writerow([company_name, skills, more_info])
                    print(f'Entry saved: {index}')


if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f'Waiting {time_wait} in minutes...')
        time.sleep(time_wait * 60)