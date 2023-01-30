import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from projectonliner.pages.cart_page import Cart_page
from mainproject.pages.client_information_page import Client_information_page
from mainproject.pages.finish_page import Finish_page
from projectonliner.pages.login_page import Login_page
from projectonliner.pages.main_page import Main_page
from mainproject.pages.payment_page import Payment_page


# @pytest.mark.run(order=2)
def test_buy_product_1():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    g = Service('D:\\Stepik\\pythonProject\\chromedriver.exe')
    driver_g = webdriver.Chrome(options=options, service=g)
    driver_g.implicitly_wait(100)
    print("Start test 1")

    login = Login_page(driver_g)
    login.authorisation()

    mp = Main_page(driver_g)
    mp.select_notebooks_button()
    # #
    # cp = Cart_page(driver_g)
    # cp.click_checkout_button()

    # ci = Client_information_page(driver_g)
    # ci.client_information()
    #
    # pp = Payment_page(driver_g)
    # pp.click_finish_button()
    #
    # fp = Finish_page(driver_g)
    # fp.finish()

    # time.sleep(10)
    # driver_g.quit()

# @pytest.mark.run(order=1)
# def test_buy_product_2():
#     options = webdriver.ChromeOptions()
#     options.add_experimental_option("detach", True)
#     g = Service('D:\\Stepik\\pythonProject\\chromedriver.exe')
#     driver_g = webdriver.Chrome(options=options, service=g)
#
#     print("Start test 2")
#
#     login = Login_page(driver_g)
#     login.authorisation()
#
#     mp = Main_page(driver_g)
#     mp.select_products_2()
#
#     cp = Cart_page(driver_g)
#     cp.click_checkout_button()
#
#     time.sleep(10)
#     driver_g.quit()

# @pytest.mark.run(order=3)
# def test_buy_product_3():
#     options = webdriver.ChromeOptions()
#     options.add_experimental_option("detach", True)
#     g = Service('D:\\Stepik\\pythonProject\\chromedriver.exe')
#     driver_g = webdriver.Chrome(options=options, service=g)
#
#     print("Start test 3")
#
#     login = Login_page(driver_g)
#     login.authorisation()
#
#     mp = Main_page(driver_g)
#     mp.select_products_3()
#
#     cp = Cart_page(driver_g)
#     cp.click_checkout_button()
#
#     time.sleep(10)
#     driver_g.quit()
