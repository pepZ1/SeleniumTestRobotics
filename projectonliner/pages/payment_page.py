from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from mainproject.base.base_class import Base


class Payment_page(Base):


    def __init__(self, driver_g):
        super().__init__(driver_g)
        self.driver_g = driver_g

    # Locators
    finish_button = "//*[@id='finish']"



    # Getters
    def get_finish_button(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.finish_button)))




    # Actions



    def click_finish_button(self):
        self.get_finish_button().click()
        print("Click finish_button")



    # Methods

    def select_product(self):
        self.get_current_url()
        self.click_finish_button()


