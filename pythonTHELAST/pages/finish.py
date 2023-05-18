import time

import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from utilities.logger import Logger


class Finish_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    finish = "//*[@id='finish']"

    # Getters
    def get_finish(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.finish)))

    # Actions
    def click_finish(self):
        self.get_finish().click()
        print("CLICK finish")

    # METHODS
    def click_finish_button(self):
        with allure.step("Click finish button"):
            Logger.add_start_step(method='click_finish_button')
            self.get_current_url()
            self.click_finish()
            Logger.add_end_step(url=self.driver.current_url, method='click_finish_button')

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
