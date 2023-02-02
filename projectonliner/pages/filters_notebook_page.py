import time

from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from projectonliner.base.base_class import Base



class Filters_notebook_page(Base):

    def __init__(self, driver_g):
        super().__init__(driver_g)
        self.driver_g = driver_g

    # Locators
    price_min = "//*[@id='min_price']"
    price_max = "//*[@id='max_price']"
    brand_hp_click = "//*[@id='products_filter']/ul[2]/li[3]/label/span"
    year_of_release_click = "//*[@id='products_filter']/ul[3]/li[2]/label/span"
    os_windows_click = "//*[@id='products_filter']/ul[4]/li[5]/label/span"
    ram_click = "//*[@id='products_filter']/ul[6]/li[5]/label/span"
    type_click = "//*[@id='products_filter']/ul[7]/li[3]/label/span"
    ssd_click = "//*[@id='products_filter']/ul[10]/li[4]/label/span"
    order_click = "//*[@id='products-table']/div/div/div/form/div/div[2]/input"
    order_confirm_click = "/html/body/div[14]/div/div[3]/div[2]/button"

    # Getters

    def get_price_min(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_min)))

    def get_price_max(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_max)))

    def get_brand_hp_click(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.brand_hp_click)))

    def get_year_of_release_click(self):
        return WebDriverWait(self.driver_g, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.year_of_release_click)))

    def get_os_windows_click(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.os_windows_click)))

    def get_ram_click(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.ram_click)))

    def get_type_click(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.type_click)))

    def get_ssd_click(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.ssd_click)))

    def get_order_click(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.order_click)))

    def get_order_confirm_click(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.order_confirm_click)))



    # Actions

    def price_min_button(self, min_price):
        self.get_price_min().send_keys(Keys.BACKSPACE)
        self.get_price_min().send_keys(min_price)
        print("Min price choose")

    def price_max_button(self, max_price):
        self.get_price_max().send_keys(Keys.BACKSPACE*5)
        self.get_price_max().send_keys(max_price)
        print("Max price choose")

    def brand_hp_button(self):
        self.get_brand_hp_click().click()
        print("Brand samsung choose")

    def year_of_release_button(self):
        self.get_year_of_release_click().click()
        print("Year of release choose")

    def os_windows_button(self):
        self.get_os_windows_click().click()
        print("Windows OS choose")

    def ram_button(self):
        self.get_ram_click().click()
        print("Ram 16gb choose")

    def type_button(self):
        self.get_type_click().click()
        print("Type classic choose")

    def ssd_button(self):
        self.get_ssd_click().click()
        print("ssd choose")

    def order_button(self):
        self.get_order_click().click()
        print("Order click")

    def order_confirm_button(self):
        self.get_order_confirm_click().click()
        print("Order confirm click")

    # Methods

    def filter_click(self):
        self.driver_g.maximize_window()
        self.get_current_url()
        time.sleep(5)
        self.driver_g.execute_script("window.scrollTo(0, 1000)")
        self.price_min_button("2000")
        self.price_max_button("4000")
        self.brand_hp_button()
        self.year_of_release_button()
        self.driver_g.execute_script("window.scrollTo(0, 1400)")
        self.os_windows_button()
        self.driver_g.execute_script("window.scrollTo(0, 1800)")
        self.ram_button()
        self.driver_g.execute_script("window.scrollTo(0, 2000)")
        self.type_button()
        self.driver_g.execute_script("window.scrollTo(0, 2500)")
        self.ssd_button()
        self.driver_g.execute_script("window.scrollTo(0, 200)")
        self.order_button()
        self.order_confirm_button()


