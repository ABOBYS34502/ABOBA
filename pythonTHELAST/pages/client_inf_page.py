import time

import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from utilities.logger import Logger


class Profile_info(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    first_name = "//*[@id='first-name']"
    last_name = "//*[@id='last-name']"
    postal_code = "//*[@id='postal-code']"
    continue_button = "//*[@id='continue']"

    # Getters
    def get_first_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.first_name)))

    def get_last_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.last_name)))

    def get_postal_code(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.postal_code)))

    def get_continue_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.continue_button)))

    # Actions
    def input_first_name(self, first_name):
        self.get_first_name().send_keys(first_name)
        print("input first name")

    def input_last_name(self, last_name):
        self.get_last_name().send_keys(last_name)
        print("input last name")

    def input_postal_code(self, postal_code):
        self.get_postal_code().send_keys(postal_code)
        print("CLICK postal code")

    def click_continue_button(self):
        self.get_continue_button().click()
        print("CLICK continue")

    # METHODS
    def check_out_fields(self):
        with allure.step("Check out fields"):
            Logger.add_start_step(method='check_out_fields')
            self.get_current_url()
            self.input_first_name('KOK')
            self.input_last_name('dick')
            self.input_postal_code("666")
            self.click_continue_button()
            Logger.add_end_step(url=self.driver.current_url, method='check_out_fields')

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
