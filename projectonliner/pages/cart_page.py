from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from projectonliner.base.base_class import Base


class Cart_page(Base):

    def __init__(self, driver_g):
        super().__init__(driver_g)
        self.driver_g = driver_g

    # Locators
    assert_check_word = "//*[@id='container']/div[2]/div[1]/h2"
    delivery_click = "//*[@id='deliveries_type_2']"
    delivery_adress_click = "//*[@id='deliveries_4']"
    payment_method_click = "//*[@id='payment_methods_11']"
    name_input = "//*[@id='submit_order']/div/div/div[2]/div/div[2]/div[1]/div/div[1]/div[1]/input"
    tel_number_input = "//*[@id='phoneNumberMask']"
    email_input = "//*[@id='submit_order']/div/div/div[2]/div/div[2]/div[1]/div/div[2]/div/input"
    comment_input = "//*[@id='order_comment']"
    # Getters
    def get_assert_word(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.assert_check_word)))

    def get_delivery_click(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.delivery_click)))

    def get_delivery_adress_click(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.delivery_adress_click)))

    def get_payment_method_click(self):
        return WebDriverWait(self.driver_g, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.payment_method_click)))

    def get_name_input(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.name_input)))

    def get_tel_number_input(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.tel_number_input)))

    def get_email_input(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.email_input)))

    def get_comment_input(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.comment_input)))
    # Actions

    def delivery_button(self):
        self.get_delivery_click().click()
        print("choose delivery")

    def delivery_adress_button(self):
        self.get_delivery_adress_click().click()
        print("choose delivery adress")

    def payment_method_button(self):
        self.get_payment_method_click().click()
        print("choose payment method")

    def input_name_button(self, username):
        self.get_name_input().send_keys(Keys.BACKSPACE*15)
        self.get_name_input().send_keys(username)
        print("Input username")

    def input_tel_number_button(self, tel):
        self.get_tel_number_input().click()
        self.get_tel_number_input().send_keys(tel)
        print("Input phone")

    def input_email_button(self, email):
        self.get_email_input().click()
        self.get_email_input().send_keys(Keys.BACKSPACE*25)
        self.get_email_input().send_keys(email)
        print("Input email")

    def input_comment_button(self, comment):
        self.get_comment_input().send_keys(comment)
        print("Input comment")


    # Methods

    def product_confirmation_info(self):
        self.get_current_url()
        self.assert_word(self.get_assert_word(), 'В корзине 1 товар')
        self.driver_g.execute_script("window.scrollTo(0, 1200)")
        self.delivery_button()
        self.delivery_adress_button()
        self.driver_g.execute_script("window.scrollTo(0, 2000)")
        self.payment_method_button()
        self.driver_g.execute_script("window.scrollTo(0, 2700)")
        self.input_name_button("Шамиль Дудаев")
        self.input_tel_number_button("295072213")
        self.input_email_button("testqaauto13@gmail.com")
        self.input_comment_button("Спасибо Алексу за курс ! Очень крутой курс !!")



