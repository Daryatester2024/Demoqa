import time

from pages.tables import Tables

def test_tables(browser):
    page_tables=Tables(browser)
    page_tables.visit()
    assert not page_tables.no_data.exist()
    while page_tables.btn_delete_row.exist():
        page_tables.btn_delete_row.click()
    time.sleep(5)
    assert page_tables.no_data.exist()

def test_tables_add(browser):
    page_tables=Tables(browser)
    page_tables.visit()
    page_tables.btn_add_new_record.click()
    page_tables.user_form_modal_tbl.exist()
    page_tables.btn_submit_modal_tbl.click()
    assert page_tables.user_form_modal_tbl.get_dom_attribute('class') == 'was-validated'
    page_tables.first_name_modal_tbl.send_keys('Ivan')
    page_tables.last_name_modal_tbl.send_keys('Ivanov')
    page_tables.user_email_modal_tbl.send_keys('rrrrrr@rr.rr')
    page_tables.user_age_modal_tbl.send_keys('25')
    page_tables.salary_modal_tbl.send_keys('90000')
    page_tables.department_modal_tbl.send_keys('tester')
    page_tables.btn_submit_modal_tbl.click()
    time.sleep(2)
    assert not page_tables.user_form_modal_tbl.exist()
    assert not page_tables.new_row_1_tbl.get_dom_attribute('class') == 'rt-tr -padRow -even'
    assert page_tables.first_name_tbl.get_text() == 'Ivan'
    assert page_tables.last_name_tbl.get_text() == 'Ivanov'
    assert page_tables.user_email_tbl.get_text() == 'rrrrrr@rr.rr'
    assert page_tables.user_age_tbl.get_text() == '25'
    assert page_tables.salary_tbl.get_text() == '90000'
    assert page_tables.department_tbl.get_text() == 'tester'
    page_tables.btn_edit_record_4.click()
    page_tables.first_name_modal_tbl.clear()
    page_tables.first_name_modal_tbl.send_keys('Petr')
    page_tables.btn_submit_modal_tbl.click()
    assert page_tables.first_name_tbl.get_text() == 'Petr'
    page_tables.btn_delete_record_4.click()
    time.sleep(2)
    assert page_tables.new_row_1_tbl.get_dom_attribute('class') == 'rt-tr -padRow -even'

def test_tables_next_previous(browser):
    page_tables=Tables(browser)
    page_tables.visit()
    page_tables.btn_select_page.scroll_to_element()
    page_tables.btn_select_page.click()
    page_tables.btn_row_len_5.click()
    time.sleep(2)
    page_tables.btn_next.click()
    assert page_tables.page_row_number.get_dom_attribute('value') == '1'
    page_tables.btn_previous.click()
    assert page_tables.page_row_number.get_dom_attribute('value') == '1'
    assert page_tables.btn_next.get_dom_attribute('disabled')
    assert page_tables.btn_previous.get_dom_attribute('disabled')
    page_tables.btn_add_new_record.click()
    page_tables.first_name_modal_tbl.send_keys('Ivan')
    page_tables.last_name_modal_tbl.send_keys('Ivanov')
    page_tables.user_email_modal_tbl.send_keys('rrrrrr@rr.rr')
    page_tables.user_age_modal_tbl.send_keys('25')
    page_tables.salary_modal_tbl.send_keys('90000')
    page_tables.department_modal_tbl.send_keys('tester')
    page_tables.btn_submit_modal_tbl.click()
    page_tables.btn_add_new_record.click()
    page_tables.first_name_modal_tbl.send_keys('Ivan1')
    page_tables.last_name_modal_tbl.send_keys('Ivanov1')
    page_tables.user_email_modal_tbl.send_keys('krrrrrr@rr.rr')
    page_tables.user_age_modal_tbl.send_keys('26')
    page_tables.salary_modal_tbl.send_keys('80000')
    page_tables.department_modal_tbl.send_keys('tester')
    page_tables.btn_submit_modal_tbl.click()
    page_tables.btn_add_new_record.click()
    page_tables.first_name_modal_tbl.send_keys('Ivan2')
    page_tables.last_name_modal_tbl.send_keys('Ivanov2')
    page_tables.user_email_modal_tbl.send_keys('kkrrrrrr@rr.rr')
    page_tables.user_age_modal_tbl.send_keys('28')
    page_tables.salary_modal_tbl.send_keys('90000')
    page_tables.department_modal_tbl.send_keys('tester')
    page_tables.btn_submit_modal_tbl.click()
    page_tables.btn_next.click()
    assert page_tables.page_row_number.get_dom_attribute('value') == '2'
    page_tables.btn_previous.click()
    assert page_tables.page_row_number.get_dom_attribute('value') == '1'







