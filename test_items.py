from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def test_add_to_cart_button_is_displayed(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    browser.get(link)
    WebDriverWait(browser, 5).until(ec.visibility_of_element_located((By.XPATH, '//*[@id="add_to_basket_form"]/button')))
    assert browser.find_element(By.XPATH, '//*[@id="add_to_basket_form"]/button'), 'button is not found'
