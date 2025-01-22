from pages.demoqa import DemoQa

from pages.elements_page import ElementsPage

def test_get_text(browser):

    demo_qa_page=DemoQa(browser)
    demo_qa_page.visit()
    demo_qa_page.text_1.get_text()
    assert demo_qa_page.text_1.get_text() == '© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.'
    demo_qa_page.visit()
    demo_qa_page.btn_elements.click()
    demo_qa_page.text_element_1.get_text()
    assert demo_qa_page.text_element_1.get_text() =='Please select an item from left to start practice.'

def test_page_elements (browser):
    el_page=ElementsPage(browser)
    el_page.visit()
    # assert el_page.text_elements.get_text() == 'Please select an item from left to start practice.'
    assert el_page.icon.exist()
    assert el_page.btn_sidebar_first.exist()
    assert el_page.btn_sidebar_first_textbox.exist()