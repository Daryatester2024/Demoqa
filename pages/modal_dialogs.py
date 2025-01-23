from pages.base_page import BasePage

from components.components import WebElement

from pages.form_page import FormPage

class ModalDialogs(BasePage):

    def __init__(self,driver):
        self.base_url='https://demoqa.com/modal-dialogs'
        super().__init__(driver, self.base_url)
        self.btns_modal_dialog=WebElement(driver,'div:nth-child(5) > div > ul>li')
        self.icon_modal=WebElement(driver, '#app > header > a > img')