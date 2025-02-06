import time

from pages.modal_dialogs import ModalDialogs
from pages.alerts import Alerts

def test_check_modal(browser):
    page_modal=ModalDialogs(browser)
    page_modal.visit()
    assert page_modal.btn_small.exist()
    assert page_modal.btn_large.exist()
    page_modal.btn_small.click()
    time.sleep(2)
    assert page_modal.modal_window_small.exist()
    page_modal.btn_small_close.click()
    time.sleep(2)
    assert not page_modal.modal_window_small.exist()
    page_modal.btn_large.click()
    time.sleep(2)
    assert page_modal.modal_window_large.exist()
    page_modal.btn_large_close.click()
    time.sleep(2)
    assert not page_modal.modal_window_large.exist()

