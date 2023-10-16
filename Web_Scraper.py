## This is the first project I'm working through by myself. My next goal was to loop finddirectory() somehow so that I'm not creating multiple functions that do the same thing. 
##  I'm honestly not sure how I'll do it yet.
##
##
##








import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
import time



# establish driver and define lists to be used
driver = webdriver.Chrome()
repolist = []
directorylist = []
directorylist2 = []








# iterate through sys.stdin and append the domain with the input. Each iteration is saved as in a variable and passed to the next function. This function also clears global lists with each iteration.
def githubtarget():
    for i in sys.stdin:
        driver.get(f"https://github.com/{i}")
        target = f"https://github.com/{i}"
        #time.sleep(2)
        repolist.clear()
        directorylist.clear()
        targetrepos(target)

#search the target domain for the class "repo" for each repo append a list with its parsed text. For each item on the list create a new target domain. 
# Pass new target domain to the next function.
def targetrepos(target):
    repos = driver.find_elements(By.CLASS_NAME, "repo")
    for j in repos:
        repolist.append(j.text)
#       print(target,"/",j.text)
    for k in repolist:
        repotarget = f"{target}/{k}"
        finddirectory(repotarget)

# http:get next target domain. For each js-navigation element, find its href value, save it as a variable, and use that variable to append a list.
# For each item in the list, visit the target, extract its raw html, save raw html as a variable, and search through that variable for a target string.
# if target string is found print target domain and a message indicating that the target string was found. 
# Another function is called to check for more js-navigation classes and href values.
def  finddirectory(repotarget):
    driver.get(repotarget)
    #print(repotarget)
    time.sleep(1)
    directory = driver.find_elements(By.CLASS_NAME, "js-navigation-open")
    for l in directory:
        finaltarget = l.get_attribute("href") 
        #print(finaltarget)
        #time.sleep(1)
        directorylist.append(finaltarget)
        #print(repotarget,"/",l.text)
    for m in directorylist:
       driver.get(m)
       raw = driver.page_source
       if "password" in raw:
           print(f"{m} *****There's a password here.*****")
       #time.sleep(2)
       #find_second_directory()
       
# def find_second_directory():
#     directory2 = driver.find_elements(By.CLASS_NAME, "js-navigation-open")
#     for n in directory2:
#         finaltarget2 = n.get_attribute("href")
#         print(finaltarget2)
#         #time.sleep(1)
#         directorylist2.append(finaltarget2)

