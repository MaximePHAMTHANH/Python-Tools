from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import random



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
	get_url = driver.current_url
	sleeping=random.randint(30, 180)
	print("Pass N°"+str(n+1)+" / Sleeping for:"+str(sleeping)+"sec / The current url is:"+str(get_url))
	driver.close()
	
	time.sleep(sleeping)


nb_of_scraps=10
scrap_url="***"


for n in range(nb_of_scraps):scraping(n,scrap_url)
