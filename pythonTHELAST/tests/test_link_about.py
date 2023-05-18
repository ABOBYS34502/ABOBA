import time

import allure
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


@allure.description("Test link about")
def test_link_about(set_group):
    driver = webdriver.Chrome(executable_path='\\Users\\hallway\\PycharmProjects\\resource\\chromedriver')

    login = Login_page(driver)
    login.authorization()

    mp = Main_page(driver)
    mp.select_menu_about()
    f = Finish_screen(driver)
    f.screenshot()
    time.sleep(3)