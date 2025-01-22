import time
from pages.accordion import Accordian

def test_visible_accordion(browser):
    accordion_page=Accordian(browser)
    accordion_page.visit()
    assert accordion_page.lorem_1.visible()
    accordion_page.lorem_head.click()
    time.sleep(2)
    assert not accordion_page.lorem_1.visible()

def test_visible_accordion_default(browser):
    accordion_page = Accordian(browser)
    accordion_page.visit()
    assert not accordion_page.lorem_text_1.visible()
    assert not accordion_page.lorem_text_2.visible()
    assert not accordion_page.lorem_text_3.visible()


