import time
import sys, getopt
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


browser = webdriver.Chrome(executable_path="./chromedriver-2-38")

def open_browser():    
    browser.get("https://gmail.com/")
    time.sleep(3)
    assert "Gmail" in browser.title

def gmail_login(email,password):
    print 'logando no gmail'
    username = browser.find_element_by_name('identifier')
    username.send_keys(email)
    next_page = browser.find_element_by_id('identifierNext')
    next_page.click()
    time.sleep(3)
    password = browser.find_element_by_name('password')
    password.send_keys(password)
    browser.find_element_by_id('passwordNext').click()

def main(argv):
   email = ''
   password = ''
   try:
      opts, args = getopt.getopt(argv,"he:p:",["email=","password="])
   except getopt.GetoptError:
      print 'error'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'test.py -e email -p password'
         sys.exit() 
      elif opt in ("-e", "--email"):
         email = arg
         print 'email usado', email
      elif opt in ("-p", "--password"):
         password = arg
   open_browser()
   gmail_login(email=email,password=password)

if __name__ == "__main__":
   main(sys.argv[1:])
   





