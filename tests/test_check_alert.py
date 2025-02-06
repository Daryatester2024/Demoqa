import time

from pages.alerts import Alerts

def test_check_time_alert(browser):
    alert_page=Alerts(browser)
    alert_page.visit()
    alert_page.btn_alert_time.click()
    assert not alert_page.alert()
    time.sleep(6)
    assert alert_page.alert()