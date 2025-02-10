import pytest

from pages.demoqa import DemoQa
from pages.radio_button import RadioButton

@pytest.mark.skip
def test_decor_3(browser):
    demo=DemoQa(browser)
    demo.visit()
    assert demo.h_5_elem.check_count_elements(6)

    for element in demo.h_5_elem.find_elements():
        assert element.text !=''
@pytest.mark.skipif(True, reason='пропуск')
def test_decor_1(browser):
    radio=RadioButton(browser)
    radio.visit()
    radio.btn_yes.click_force()
    assert radio.text_radio.get_text() == 'You have selected Yes'
    radio.btn_impressive.click_force()
    assert radio.text_radio.get_text() == 'You have selected Impressive'
    assert 'disabled'in radio.btn_no.get_dom_attribute('class')
