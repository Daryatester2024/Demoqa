import time

from pages.tables import Tables

def test_sort_tables(browser):
    page_table=Tables(browser)
    page_table.visit()
    page_table.heading_first_name.click()
    time.sleep(3)
    assert page_table.heading_first_name.get_dom_attribute('class') == 'rt-th rt-resizable-header -sort-asc -cursor-pointer'
    page_table.heading_last_name.click()
    time.sleep(3)
    assert page_table.heading_last_name.get_dom_attribute('class') == 'rt-th rt-resizable-header -sort-asc -cursor-pointer'
    page_table.heading_age.click()
    time.sleep(3)
    assert page_table.heading_age.get_dom_attribute('class') == 'rt-th rt-resizable-header -sort-asc -cursor-pointer'
    page_table.heading_email.click()
    time.sleep(3)
    assert page_table.heading_email.get_dom_attribute('class') == 'rt-th rt-resizable-header -sort-asc -cursor-pointer'
    page_table.heading_salary.click()
    time.sleep(3)
    assert page_table.heading_salary.get_dom_attribute('class') == 'rt-th rt-resizable-header -sort-asc -cursor-pointer'
    page_table.heading_department.click()
    time.sleep(3)
    assert page_table.heading_department.get_dom_attribute('class') == 'rt-th rt-resizable-header -sort-asc -cursor-pointer'




