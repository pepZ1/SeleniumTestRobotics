from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from projectonliner.base.base_class import Base


class Main_page(Base):

    def __init__(self, driver_g):
        super().__init__(driver_g)
        self.driver_g = driver_g

    # Locators
    main_page_logo_click = "//*[@id='main-header']/div/div/div[1]/a/img"
    computers_click = "//*[@id='navbar']/ul[1]/li[5]"
    notebook_click = "//*[@id='cat-list']/ul/li[1]/a"
    # select_product_2 = "//*[@id='add-to-cart-sauce-labs-bike-light']"
    # select_product_3 = "//*[@id='add-to-cart-sauce-labs-bolt-t-shirt']"
    # cart = "//*[@id='shopping_cart_container']/a"
    # menu = "//*[@id='react-burger-menu-btn']"
    # link_about = "//*[@id='about_sidebar_link']"
    # Getters
    def get_main_page_logo_click(self):
        return WebDriverWait(self.driver_g, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.main_page_logo_click)))

    def get_computers_click(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.computers_click)))

    def get_notebook_click(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.notebook_click)))
    #
    # def get_cart(self):
    #     return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart)))
    #
    # def get_menu(self):
    #     return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.menu)))
    #
    # def get_link_about(self):
    #     return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.link_about)))
    # Actions

    def main_logo_click(self):
        self.get_main_page_logo_click().click()
        print("Click logo button move to main page")

    def click_computer(self):
        self.get_computers_click().click()
        print("Click computer button")
    #
    def click_notebook(self):
        self.get_notebook_click().click()
        print("Click notebook button")
    #
    # def click_cart(self):
    #     self.get_cart().click()
    #     print("Click move to cart")
    #
    # def click_menu(self):
    #     self.get_menu().click()
    #     print("Click menu")
    #
    # def click_link_about(self):
    #     self.get_link_about().click()
    #     print("Click Link about")

    # Methods

    def select_notebooks_button(self):
        self.main_logo_click()
        self.click_computer()
        self.click_notebook()
        self.get_current_url()
        self.assert_url('https://mobistore.by/noutbuki')

    # def select_products_2(self):
    #     self.get_current_url()
    #     self.click_select_product_2()
    #     self.click_cart()
    #
    # def select_products_3(self):
    #     self.get_current_url()
    #     self.click_select_product_3()
    #     self.click_cart()
    #
    # def menu_select_about(self):
    #     self.get_current_url()
    #     self.click_menu()
    #     self.click_link_about()
    #     self.assert_url('https://saucelabs.com/')
