from selenium.webdriver.common.by import By


def test_icon_exist(browser):

   browser.get('https://demoqa.com/')

   icon=browser.find_element(By.CSS_SELECTOR,'#app > header > a')

   if icon is None:
        print("не найден")
   else:
        print("найден")