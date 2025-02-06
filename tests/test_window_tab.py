from pages.links import Links

def test_window_tab(browser):
    page_links=Links(browser)
    page_links.visit()
    assert page_links.link_home.exist()
    assert page_links.link_home.get_text() == 'Home'
    assert page_links.link_home.get_dom_attribute('href') == 'https://demoqa.com'
    assert len(browser.window_handles) == 1
    page_links.link_home.click()
    assert len(browser.window_handles) == 2

