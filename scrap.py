from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import random
import sys



chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--mute-audio")
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
chrome_options.add_argument("--disable-search-engine-choice-screen")
#chrome_options.add_argument("--headless=new")

def scraping(n,url):
	driver=webdriver.Chrome(options=chrome_options)
	driver.get("https://www.croxyproxy.com/")
	driver.find_element(By.CLASS_NAME,'fc-cta-consent').click()
	element=driver.find_element(By.ID,'url')
	element.send_keys(url)
	driver.find_element(By.ID,'requestSubmit').click()

	time.sleep(22)
	sleeping=random.randint(600, 1800)
	print("Pass N°"+str(n+1)+" of "+str(nb_of_scraps)+" // Sleeping for:"+str(sleeping)+"sec")
	driver.close()
	time.sleep(sleeping)


nb_of_scraps=int(sys.argv[1])
scrap_url=""

print("The scrapped url is: "+scrap_url+" // Doing "+str(nb_of_scraps)+" passes")
for n in range(nb_of_scraps):scraping(n,scrap_url)
