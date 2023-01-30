from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from mainproject.base.base_class import Base


class Login_page(Base):

    url = 'https://mobistore.by/'

    def __init__(self, driver_g):
        super().__init__(driver_g)
        self.driver_g = driver_g

    # Locators
    login_enter_click = "//*[@id='login']"
    email_login = "//*[@id='email']"
    password_login = "//*[@id='password']"
    login_click = "//*[@id='container']/div/div/div/div[2]/form/div[4]/input"

    # Getters
    # def get_cookie_accept_click(self):
    #     return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.cookie_accept_click)))

    # def get_login_window_click(self):
    #     return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_window_click)))

    def get_login_enter_click(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_enter_click)))

    def get_email_login(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.email_login)))

    def get_password_login(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.password_login)))

    def get_login_click(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_click)))
    # Actions

    # def input_email_login(self, email):
    #     self.get_email_login().send_keys(email)
    #     print("Input Email")
    #
    # def input_password(self, password):
    #     self.get_password_login().send_keys(password)
    #     print("Input password")

    # def cookie_accept_button(self):
    #     self.get_cookie_accept_click().click()
    #     print("Click cookie accept button")

    # def login_window_button(self):
    #     self.get_login_window_click().click()
    #     print("Click Login button")

    def login_enter_button(self):
        self.get_login_enter_click().click()
        print("Click Login button")

    def input_email_login(self, email):
        self.get_email_login().send_keys(email)
        print("Input email")

    def input_password_login(self, password):
        self.get_password_login().send_keys(password)
        print("Input password")

    def login_click_button(self):
        self.get_login_click().click()
        print("Click login button")




    # Methods

    def authorisation(self):
        self.driver_g.get(self.url)
        self.driver_g.maximize_window()
        self.get_current_url()
        # self.cookie_accept_button()
        # self.login_window_button()
        self.login_enter_button()
        self.input_email_login("testqaauto13@gmail.com")
        self.input_password_login("Testqa13!")
        self.login_click_button()
        # self.click_captcha_button()
        # self.assert_word(self.get_main_word(), 'PRODUCTS')
