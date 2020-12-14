#import the libraries
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

#get scopus data
def scopus():

    return 1


#get web of science data
def web_of_science(name_of_school):
    infos = {}
    data = []
    #auteurs = []
    #keywords = []
    #it needs a geckodriver 'installed from github'
    driver = webdriver.Firefox(executable_path="/home/x-raiden/Downloads/geckodriver")
    driver.get("https://eressources.imist.ma/login?url=https://www.webofknowledge.com")
    #login to imist eressources
    login = driver.find_element_by_xpath("/html/body/div[1]/form/div[2]/input")
    password = driver.find_element_by_xpath("/html/body/div[1]/form/div[3]/input")
    #personal infos
    login.send_keys("ayoub.er-rkhis@usms.ac.ma")
    password.send_keys("@0000")
    button = driver.find_element_by_xpath("/html/body/div[1]/form/input")
    button.submit()
    #we should wait for the page to load ( slow internet :'( )
    time.sleep(60)
    #entred to web_of_science
    main_selector = driver.find_element_by_xpath('//*[@id="select2-select1-container"]').click()
    search = driver.find_element_by_xpath('/html/body/span[37]/span/span[1]/input')
    search.send_keys("Enhanced")
    selector = driver.find_element_by_xpath('/html/body/span[37]/span/span[2]').click()
    search_bar = driver.find_element_by_xpath('//*[@id="value(input1)"]')
    search_bar.send_keys(name_of_school)
    button_in_web_of_science = driver.find_element_by_xpath("/html/body/form[1]/div[1]/div/div/div/table/tbody/tr/td[3]/span/span[1]/button")
    button_in_web_of_science.submit()
    #articles page
    time.sleep(30)
    driver.find_element_by_xpath('/html/body/div[1]/div[26]/div[2]/div/div/div/div[2]/div[3]/div[5]/form[2]/div/div[1]/div/span/div[2]/div[1]/div[3]/div/div[1]/div/a/value').click()
    time.sleep(15)
    for k in range (1,100):
        try:
            infos['titre'] = driver.find_element_by_xpath('/html/body/div[1]/div[26]/form[3]/div/div/div/div[1]/div/div[1]/value').text
            infos['date_publication'] = driver.find_element_by_xpath('/html/body/div[1]/div[26]/form[3]/div/div/div/div[1]/div/div[3]/p[4]/value').text
            infos['type'] = driver.find_element_by_xpath('/html/body/div[1]/div[26]/form[3]/div/div/div/div[1]/div/div[3]/p[5]').text
            infos['auteurs'] = driver.find_element_by_xpath('/html/body/div[1]/div[26]/form[3]/div/div/div/div[1]/div/div[2]/p').text
            infos['auteur_mail'] = driver.find_element_by_xpath('/html/body/div[1]/div[26]/form[3]/div/div/div/div[1]/div/div[6]/p[7]/a').text
            infos['abstract'] = driver.find_element_by_xpath('/html/body/div[1]/div[26]/form[3]/div/div/div/div[1]/div/div[4]/p').text
            infos['keywords'] = driver.find_element_by_xpath('/html/body/div[1]/div[26]/form[3]/div/div/div/div[1]/div/div[5]/p[1]').text
            infos['cited'] = driver.find_element_by_xpath('/html/body/div[1]/div[26]/form[3]/div/div/div/div[2]/div[1]/div/div[6]/a/span').text
            infos['organization'] = 'Sultan Moulay Slimane University of Beni Mellal'
            data.append(infos)
            driver.find_element_by_xpath('/html/body/div[1]/div[26]/div/form/span/a[2]').click()
        except Exception as e:
            driver.find_element_by_xpath('/html/body/div[1]/div[26]/div/form/span/a[2]').click()
            pass
    print(data)
    return 1

#get google scholar data
def google_scholar():

    return 1

#get science direct data
def science_direct():

    return 1

#main function
if __name__ == "__main__":
    name_of_school = "Sultan Moulay Slimane University of Beni Mellal "
    web_of_science(name_of_school)
