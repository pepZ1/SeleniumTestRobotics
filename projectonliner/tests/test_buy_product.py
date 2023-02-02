import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from projectonliner.pages.cart_page import Cart_page
from projectonliner.pages.filters_notebook_page import Filters_notebook_page
from projectonliner.pages.finish_page import Finish_page
from projectonliner.pages.login_page import Login_page
from projectonliner.pages.main_page import Main_page




def test_buy_product_1():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    g = Service('D:\\Stepik\\pythonProject\\projectonliner\\utilities\\chromedriver.exe')
    driver_g = webdriver.Chrome(options=options, service=g)
    print("Start test ")

    login = Login_page(driver_g)
    login.authorisation()

    mp = Main_page(driver_g)
    mp.select_notebooks_button()

    fp = Filters_notebook_page(driver_g)
    fp.filter_click()

    cp = Cart_page(driver_g)
    cp.product_confirmation_info()

    fp = Finish_page(driver_g)
    fp.finish()
    print("Test finish")

    # time.sleep(10)
    # driver_g.quit()

