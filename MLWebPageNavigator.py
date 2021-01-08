import selenium as se
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
from datetime import date


class MercadoDeLiniersNavigator:

    @staticmethod
    def go_to_initial_resumen_de_precios():

        options = se.webdriver.ChromeOptions()
        options.add_argument('headless')

        driver = webdriver.Chrome(executable_path='/Users/carloscaraccia/Downloads/chromedriver', options=options)

        # Open driver and go to beginning of page
        driver.get('http://www.mercadodeliniers.com.ar/dll/hacienda1.dll/haciinfo000001')
        # Wait until a desired element appears
        wait = WebDriverWait(driver, 10)
        men_menu = wait.until(
            ec.visibility_of_element_located((By.XPATH, "//*[@id='TituloMenu2']/table/tbody/tr/td/a")))
        men_menu.click()

        # Wait until the second menu element appears
        second_menu = men_menu = wait.until(ec.visibility_of_element_located((By.XPATH,
                                                                              '//*[@id="RC11_0"]/a')))
        second_menu.click()

        return driver

    @staticmethod
    def get_cattle_prices_for_a_date(driver: webdriver, date_to_pick: date):

        # wait for the first date picker item to appear, click it and send the date
        wait = WebDriverWait(driver, 10)
        first_date_picker = wait.until(
            ec.visibility_of_element_located((By.XPATH, '//*[@id="datepicker1"]')))
        first_date_picker.click()
        first_date_picker.clear()
        first_date_picker.send_keys(date_to_pick.strftime('%d/%m/%Y'))

        # wait for the second date picker item to appear, click it and send the date
        wait = WebDriverWait(driver, 10)
        second_date_picker = wait.until(
            ec.visibility_of_element_located((By.XPATH, '//*[@id="datepicker2"]')))
        second_date_picker.click()
        second_date_picker.clear()
        second_date_picker.send_keys(date_to_pick.strftime('%d/%m/%Y'))

        # find the execute query button and press enter
        # Find the query button and press enter
        query_button = driver.find_element_by_xpath('//*[@id="Aceptar"]')
        query_button.send_keys(Keys.ENTER)

        page_source = driver.page_source

        return page_source


