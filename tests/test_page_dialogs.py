from pages.modal_dialogs import ModalDialogs

def test_modal_elements(browser):
    modal_elem=ModalDialogs(browser)
    modal_elem.visit()
    assert modal_elem.btns_modal_dialog.check_count_elements(count=5)

def test_navigation_modal(browser):
    modal_elem=ModalDialogs(browser)
    modal_elem.visit()
    modal_elem.refresh()
    modal_elem.icon_modal.click()
    browser.back()
    browser.set_window_size(900,400)
    browser.forward()
    modal_elem.equal_url()
    assert browser.title == 'DEMOQA'
    browser.set_window_size(1000, 1000)
