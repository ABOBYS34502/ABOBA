import pytest


@pytest.fixture()
def set_up():
    print("start test")
    yield
    print("finish test")


@pytest.fixture(scope='module')
def set_group():
    print("start test")
    yield
    print("finish test")

# def set_up():
#     print("start test")
#     driver = webdriver.Chrome(executable_path='\\Users\\hallway\\PycharmProjects\\resource\\chromedriver')
#     url = 'https://www.saucedemo.com/'
#     self.driver.get(self.url)
#     yield
#     driver.quit()
#     print("finish test")
