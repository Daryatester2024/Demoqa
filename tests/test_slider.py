from selenium.webdriver import Keys

from pages.slider import Slider

def test_slider(browser):
    slider=Slider(browser)
    slider.visit()
    assert slider.input_slider.exist()
    assert slider.slider.exist()

    while not slider.input_slider.get_dom_attribute('value') == '50':
        slider.slider.send_keys(Keys.ARROW_RIGHT)
    assert slider.input_slider.get_dom_attribute('value') == '50'