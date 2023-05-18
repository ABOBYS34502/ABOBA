import time

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.LOGIN_test import Login_page
from pages.cart_page import Check_out_page
from pages.client_inf_page import Profile_info
from pages.finish import Finish_page
from pages.finish_screenshot import Finish_screen
from pages.main_page import Main_page


@pytest.mark.run(order=1)
@allure.description("Test select product")
def test_select_product(set_group):
    driver = webdriver.Chrome(executable_path='\\Users\\hallway\\PycharmProjects\\resource\\chromedriver')

    login = Login_page(driver)
    login.authorization()

    mp = Main_page(driver)
    mp.select_product()
    cp = Check_out_page(driver)
    cp.check_out_button()
    cf = Profile_info(driver)
    cf.check_out_fields()
    fb = Finish_page(driver)
    fb.click_finish_button()
    f = Finish_screen(driver)
    f.finish_screen_shot()
    time.sleep(3)


@pytest.mark.run(order=3)
def test_select_product_2():
    driver = webdriver.Chrome(executable_path='\\Users\\hallway\\PycharmProjects\\resource\\chromedriver')

    login = Login_page(driver)
    login.authorization()

    mp = Main_page(driver)
    mp.select_product_2()
    cp = Check_out_page(driver)
    cp.check_out_button()
    cf = Profile_info(driver)
    cf.check_out_fields()
    fb = Finish_page(driver)
    fb.click_finish_button()
    f = Finish_screen(driver)
    f.finish_screen_shot()
    time.sleep(3)


@pytest.mark.run(order=2)
def test_select_product_3():
    driver = webdriver.Chrome(executable_path='\\Users\\hallway\\PycharmProjects\\resource\\chromedriver')

    login = Login_page(driver)
    login.authorization()

    mp = Main_page(driver)
    mp.select_product_3()
    cp = Check_out_page(driver)
    cp.check_out_button()
    cf = Profile_info(driver)
    cf.check_out_fields()
    fb = Finish_page(driver)
    fb.click_finish_button()
    f = Finish_screen(driver)
    f.finish_screen_shot()
    time.sleep(3)
