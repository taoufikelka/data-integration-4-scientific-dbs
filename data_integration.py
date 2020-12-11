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
    #we should to wait for the page ( slow internet :'( )
    time.sleep(30)
    #entred to web_of_science
    main_selector = driver.find_element_by_xpath('//*[@id="select2-select1-container"]').click()
    search = driver.find_element_by_xpath('/html/body/span[37]/span/span[1]/input')
    search.send_keys("Enhanced")
    selector = driver.find_element_by_xpath('/html/body/span[37]/span/span[2]').click()
    search_bar = driver.find_element_by_xpath('//*[@id="value(input1)"]')
    search_bar.send_keys(name_of_school)
    button_in_web_of_science = driver.find_element_by_xpath("/html/body/form[1]/div[1]/div/div/div/table/tbody/tr/td[3]/span/span[1]/button")
    button_in_web_of_science.submit()
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
