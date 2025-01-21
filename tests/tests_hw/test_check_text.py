from pages.demoqa import DemoQa

def test_get_text(browser):

    demo_qa_page=DemoQa(browser)
    demo_qa_page.visit()
    demo_qa_page.text.get_text()
    assert demo_qa_page.text.get_text() == '© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.'
    demo_qa_page.visit()
    demo_qa_page.btn_elements.click()
    demo_qa_page.text_element.get_text()
    assert demo_qa_page.text_element.get_text() =='Please select an item from left to start practice.'
