import time

from pages.progress_bar import ProgressBar

def test_progress_bar(browser):
    progress=ProgressBar(browser)

    progress.visit()
    time.sleep(2)
    progress.btn_start_stop.click()
    while True:
        if progress.progress_bar.get_dom_attribute('aria-valuenow') == '51':
            progress.btn_start_stop.click()
            break


