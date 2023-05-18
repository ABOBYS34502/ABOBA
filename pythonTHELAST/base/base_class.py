import datetime


class Base:
    def __init__(self, driver):
        self.driver = driver

    # """"method get current url"""
    def get_current_url(self):
        get_url = self.driver.current_url
        print("current url " + get_url)

    """method assert words"""

    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print("good word")

    """method screen shot"""

    def screenshot(self):
        now_date = datetime.datetime.utcnow().strftime("%Y,%m,%d,%H,%M,%S")
        photo = "photos " + now_date + ".png"
        self.driver.save_screenshot('/Users/hellway/PycharmProjects/pythonTHELAST/screen/' + photo)

    """method assert url"""
    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print("value url")
