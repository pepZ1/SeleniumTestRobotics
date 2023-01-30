from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from mainproject.base.base_class import Base


class Client_information_page(Base):



    def __init__(self, driver_g):
        super().__init__(driver_g)
        self.driver_g = driver_g

    # Locators
    first_name = "//*[@id='first-name']"
    last_name = "//*[@id='last-name']"
    zip_code = "//*[@id='postal-code']"
    continue_button = "//*[@id='continue']"


    # Getters
    def get_first_name(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.first_name)))

    def get_last_name(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.last_name)))

    def get_zip_code(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.zip_code)))

    def get_continue_button(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.continue_button)))

    # Actions

    def input_first_name(self, first_name):
        self.get_first_name().send_keys(first_name)
        print("Input First name")

    def input_last_name(self, last_name):
        self.get_last_name().send_keys(last_name)
        print("Input Last name")

    def input_zip_code(self, zip_code):
        self.get_zip_code().send_keys(zip_code)
        print("Input zip code")

    def click_continue_button(self):
        self.get_continue_button().click()
        print("Click Continue button")

    # Methods

    def client_information(self):
        self.driver_g.maximize_window()
        self.get_current_url()
        self.input_first_name("User1")
        self.input_last_name("Kozelov")
        self.input_zip_code("123")
        self.click_continue_button()

