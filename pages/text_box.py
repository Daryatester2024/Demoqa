from pages.base_page import BasePage

from components.components import WebElement

class TextBox(BasePage):
    def __init__(self,driver):
        self.base_url='https://demoqa.com/text-box'
        super().__init__(driver,self.base_url)

        self.name=WebElement(driver,'#userName')
        self.current_address_text_box=WebElement(driver,'#currentAddress')
        self.btn_submit_text_box=WebElement(driver,'#submit')
        self.output_check_name=WebElement(driver,'#name')
        self.output_check_address = WebElement(driver, 'p#currentAddress')




