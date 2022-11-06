# Importing the time module, BeautifulSoup and requests module.
from time import time
from bs4 import BeautifulSoup
import requests

def find_jobs():
    """
    It scrapes the website for jobs that are posted in the last 
    few days and filters out the jobs that require skills that you are not familiar with.
    """
    html_text = requests.get("https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=").text
    soup = BeautifulSoup(html_text, "lxml")
    jobs = soup.find_all("li", class_="clearfix job-bx wht-shd-bx")
    print("Put some skill that you are not familiar with")
    unfamiliar_skill = input(">")
    print(f"Filtering Out {unfamiliar_skill}")

    # Looping through the jobs and getting the published date.
    for index,job in enumerate(jobs):
        job = job.text
        published_date = job.find("span", class_="sim-posted").span.text
        # Checking if the job was posted in the last few days. If it was, then it will get the company
        # name, required skills and more info.
        if "few" in published_date:

            company_name = (job.find("h3", class_="joblist-comp-name")).text.replace(" ", "")
            skills = job.find("span", class_="srp-skills").text.replace(" ", "")
            more_info = job.header.h2.a["href"]
            # Checking if the skill that you are not familiar with is not in the skills required for
            # the job. If it is not, then it will write the company name, required skills and more
            # info to a file.
            if unfamiliar_skill not in skills:
                with open(f"posts/{index}.txt","w") as file:
                     file.write(f"Company Name: {company_name.strip()}\n")
                     file.write(f"Required Skills: {skills.strip()}\n")
                     file.write(f"More Info: {more_info}\n")
    
                     print(f"FIle saved: {index}")

# This is a way to make sure that the code is only executed when the file is run directly.
if __name__ == "__main__":
    while True:
        find_jobs()
        time_wait = 10
        print(f"Waiting {time_wait} seconds")
        time.sleep(input("Enter Seconds to refresh:"))