import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from base.base_class import Base
from utilities.logger import Logger


class Login_page(Base):
    url = 'https://www.saucedemo.com/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    user_name = "//input[@id ='user-name']"
    user_password = "//input[@id='password']"
    button_login = "//input[@id='login-button']"
    main_word = "//*[@id='header_container']/div[2]/span"

    # Getters
    def get_user_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_name)))

    def get_user_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_password)))

    def get_button_login(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_login)))

    def get_main_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_word)))

    # Actions
    def input_user_name(self, user_name):
        self.get_user_name().send_keys(user_name)
        print("input user name")

    def input_password(self, user_password):
        self.get_user_password().send_keys(user_password)
        print("input password")

    def click_button_login(self):
        self.get_button_login().click()
        print("CLICK login button")

    # METHODS
    def authorization(self):
        with allure.step("authorization"):
            Logger.add_start_step(method='authorization')
            self.driver.get(self.url)
            self.get_current_url()
            self.input_user_name('standard_user')
            self.input_password('secret_sauce')
            self.click_button_login()
            self.assert_word(self.get_main_word(), "Products")
            Logger.add_end_step(url=self.driver.current_url, method='authorization')

        # error_button = WebDriverWait(self.driver, 30).until(
        #     EC.element_to_be_clickable((By.XPATH, "//*[@id='login_button_container']/div/form/div[3]")))
        # error_button1 = error_button.text
        # assert error_button1 == 'Epic sadface: Sorry, this user has been locked out.'
        # print('jopa')

        # if login == 'standard_user':
        #     user_name = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@id = "
        #                                                                                            "'user-name']")))
        #     user_name.send_keys(login)
        #
        # button_login = WebDriverWait(self.driver, 30).until(
        #     EC.element_to_be_clickable((By.XPATH, "//input[@id='login-button']")))
        # button_login.click()
