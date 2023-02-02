from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from projectonliner.base.base_class import Base


class Finish_page(Base):


    def __init__(self, driver_g):
        super().__init__(driver_g)
        self.driver_g = driver_g

    # Locators




    # Getters




    # Actions







    # Methods

    def finish(self):
        self.get_current_url()
        self.assert_url('https://mobistore.by/cart')
        self.get_screenshot()


