from selenium.common.exceptions import NoSuchElementException

from pages.base_page import BasePage

from components.components import WebElement

class Accordian(BasePage):
    def __init__(self, driver):
        self.base_url='https://demoqa.com/accordian'
        super().__init__(driver, self.base_url)

        self.lorem_1=WebElement(driver,'#section1Content >p')
        self.lorem_head=WebElement(driver,'#section1Heading')
        self.lorem_text_1=WebElement(driver,'#section2Content > p:nth-child(1)')
        self.lorem_text_2=WebElement(driver,'#section2Content > p:nth-child(2)')
        self.lorem_text_3=WebElement(driver,'#section3Content > p')