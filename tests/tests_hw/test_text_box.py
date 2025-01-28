from pages.text_box import TextBox


def test_text_box(browser):
    text_box=TextBox(browser)

    text_box.visit()
    text_box.name.send_keys('Darya')
    text_box.current_address_text_box.send_keys('Piter')
    text_box.btn_submit_text_box.click()

    assert text_box.output_check_name.get_text() == 'Name:Darya'
    assert text_box.output_check_address.get_text() == 'Current Address :Piter'



