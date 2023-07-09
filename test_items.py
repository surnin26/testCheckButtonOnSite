from selenium.webdriver.common.by import By


def test_add_to_cart_button_is_displayed(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    browser.get(link)
    assert browser.find_element(By.XPATH, '//*[@id="add_to_basket_form"]/button'), 'button is not found'
