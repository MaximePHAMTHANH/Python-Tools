from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import random
import csv


def read_proxy_file(file_path):
    proxies = []
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter='\t')
        for row in reader:
            if row['Https'].strip().lower() == 'yes':
                proxies.append({'IP': row['IP Address'], 'Port': row['Port']})
    return proxies


def proxying(proxy,n):
    options = Options()
    options.add_argument(f"--proxy-server={proxy}")
    options.add_argument("--mute-audio")
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )
    driver.get("xxx")
    sleeping=random.randint(300, 1800)
    print("Pass N°"+str(n+1)+" / Sleeping for: "+str(sleeping)+"sec / The current IP is: "+str(proxy))
    #time.sleep(sleeping)
    time.sleep(3)
    driver.quit()


def main():
    file_path = 'proxylist.txt'
    proxies = read_proxy_file(file_path)
    for n,proxy in enumerate(proxies):
        proxying(f"{proxy['IP']}:{proxy['Port']}",n)

if __name__ == "__main__":
    main()

