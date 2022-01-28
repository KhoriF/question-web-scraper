from bs4 import BeautifulSoup 
import requests   
import time 
import os
import subprocess


class Scraper: 

    def find_questions(self): 

        repeats = ['Give me food and I will live give me water and I will die what am I?',

                    'Is it better to take a shower in the morning or at night?',

                    'A teacher walks into the Classroom and says If only Yesterday was Tomorrow Today would have been a Saturday Which Day did the Teacher make this Statement?',

                    'What is bigger MB vs GB?',

                    'Are the members of Hollywood Undead Scientologists?',

                    'What are the 5 oceans of the world?',

                    'What is the fourth element of the periodic table of elements?',

                    'Best foods for weight loss?'
                    ]

        web_text = requests.get('https://www.answers.com/t/random').text

        #print(web_text) # Checking if web request is successful 

        soup = BeautifulSoup(web_text, 'html.parser') 

        questions = soup.find_all('div', class_='no-underline headline2 mb-2 break-words')


        with open("output.txt", "w") as f:
            
            for question in questions:
                    if question.text.strip() in repeats:
                        continue
                    else:
                        print(question.text, '\n')  
                        f.write(question.get_text() + ('\n' * 2)) 
    
    def open_file(self):

        path = "/Users/khorifrancis/Documents/Web Scraping/Real Website Example/output.txt"
        #path = os.path.realpath(path) 
        #os.startfile(path) 
        subprocess.call(['open',path])
        
            

 
if __name__ == '__main__':
    scrape = Scraper()  

    scrape.find_questions() 
    scrape.open_file()

    while True:
        next_set = input('Do you want to load the next set of questions? (y/n): ')
        if next_set == 'y':
            scrape.find_questions()
            scrape.open_file()
        elif next_set == 'n': 
            break


