from pages.base_page import BasePage

from components.components import WebElement

class Tables(BasePage):
    def __init__(self,driver):
        self.base_url='https://demoqa.com/webtables'
        super().__init__(driver,self.base_url)
        self.no_data=WebElement(driver,'div.rt-noData')
        self.btn_delete_row=WebElement(driver,'[title="Delete"]')
        self.btn_add_new_record=WebElement(driver,'#addNewRecordButton')
        self.btn_submit_modal_tbl=WebElement(driver,'#submit')
        self.user_form_modal_tbl=WebElement(driver,'#userForm')
        self.first_name_modal_tbl=WebElement(driver,'#firstName')
        self.last_name_modal_tbl=WebElement(driver,'#lastName')
        self.user_email_modal_tbl=WebElement(driver,'#userEmail')
        self.user_age_modal_tbl=WebElement(driver,'#age')
        self.salary_modal_tbl=WebElement(driver,'#salary')
        self.department_modal_tbl=WebElement(driver,'#department')
        self.new_row_1_tbl=WebElement(driver, '#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.rt-table > div.rt-tbody > div:nth-child(4) > div')
        self.first_name_tbl=WebElement(driver,'#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.rt-table > div.rt-tbody > div:nth-child(4) > div > div:nth-child(1)')
        self.last_name_tbl=WebElement(driver,'#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.rt-table > div.rt-tbody > div:nth-child(4) > div > div:nth-child(2)')
        self.user_age_tbl=WebElement(driver,'#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.rt-table > div.rt-tbody > div:nth-child(4) > div > div:nth-child(3)')
        self.user_email_tbl=WebElement(driver,'#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.rt-table > div.rt-tbody > div:nth-child(4) > div > div:nth-child(4)')
        self.salary_tbl=WebElement(driver,'#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.rt-table > div.rt-tbody > div:nth-child(4) > div > div:nth-child(5)')
        self.department_tbl=WebElement(driver,'#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.rt-table > div.rt-tbody > div:nth-child(4) > div > div:nth-child(6)')
        self.btn_edit_record_4=WebElement(driver,'#edit-record-4')
        self.btn_delete_record_4=WebElement(driver,'#delete-record-4')
        self.btn_select_page=WebElement(driver,'#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.pagination-bottom > div > div.-center > span.select-wrap.-pageSizeOptions > select')
        self.btn_row_len_5=WebElement(driver, '#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.pagination-bottom > div > div.-center > span.select-wrap.-pageSizeOptions > select > option:nth-child(1')
        self.btn_next=WebElement(driver,'#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.pagination-bottom > div > div.-next > button')
        self.btn_previous=WebElement(driver, '#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.pagination-bottom > div > div.-previous > button')
        self.page_row_number=WebElement(driver,'#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.pagination-bottom > div > div.-center > span.-pageInfo > div > input[type=number]')

        self.heading_first_name=WebElement(driver,'div.rt-thead.-header > div > div:nth-child(1)')
        self.heading_last_name=WebElement(driver,'div.rt-thead.-header > div > div:nth-child(2)')
        self.heading_age=WebElement(driver,'div.rt-thead.-header > div > div:nth-child(3)')
        self.heading_email=WebElement(driver,'div.rt-thead.-header > div > div:nth-child(4)')
        self.heading_salary=WebElement(driver,'div.rt-thead.-header > div > div:nth-child(5)')
        self.heading_department=WebElement(driver,'div.rt-thead.-header > div > div:nth-child(6)')

