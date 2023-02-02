from datetime import datetime


class Base():

    def __init__(self, driver_g):
        self.driver = driver_g

# Method get current url

    def get_current_url(self):
        get_url = self.driver.current_url
        print("Current url " + get_url)

# Method assert by word

    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print("Assert by word OK")

# Method screenshot

    def get_screenshot(self):
        now_date = datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        print(now_date)
        name_screenshot = 'test' + now_date + '.png'

        self.driver.save_screenshot('D:\\Stepik\\pythonProject\\HW\\projectonliner\\screen\\ ' + name_screenshot)

# Method assert url

    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print("Url assert OK")
