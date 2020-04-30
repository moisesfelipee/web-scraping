from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.webdriver.support.ui import Select

import re
import time


class BOT(object):
    def __init__(self):

        # SETUP FOR URL
        self.bot_url = 'http://www.sitepessoal.net/'

        self.profile = webdriver.FirefoxProfile()
        self.options = Options()
        self.driver = webdriver.Firefox(firefox_profile=self.profile,
                                        executable_path='C:\\Users\MOISA\Documents\geckodriver.exe',
                                        options=self.options)
        self.driver.maximize_window()

        # NAVIGATE TO URL
        self.driver.get(self.bot_url)

        login_box = self.driver.find_element_by_xpath('//*[@id="login"]/div[3]/div[2]/div[2]/input')
        login_box.send_keys('teste')

        pass_box = self.driver.find_element_by_xpath('//*[@id="login"]/div[3]/div[2]/div[3]/input')
        pass_box.send_keys('123456')

        login_btn = self.driver.find_element_by_xpath('//*[@id="login"]/div[3]/div[2]/button')
        login_btn.click()

        time.sleep(2)

        # fechar = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/button')
        # fechar.click()


    def search_cpfs(self, cpf):

        # SEARCH THROUGH THE LIST OF CLIENT CODES (1ST COLLUM OF THE SPREADSHEET), AND OBTAIN THESE INFOS

        print(f"Procurando {cpf}.")
        self.driver.get(self.bot_url)
        qntbenef = ''

        # SEARCH CLIENT CODE / CLIENT CODE IS VALID
        try:
            cpf_input = self.driver.find_element_by_xpath('//*[@id="search"]/div/div[1]/input')
            cpf_input.send_keys(cpf)

            cpf_btn = self.driver.find_element_by_xpath('//*[@id="search"]/div/div[2]/button')
            cpf_btn.click()
            cpf_btn.click()

            print('CPF Valido')

            time.sleep(2)

            # IF CLIENT CODE HAVE NOTIFICATION
            if self.driver.find_element_by_xpath('//*[@id="notification"]').is_displayed():

                nome = self.driver.find_element_by_xpath(
                    "/html/body/main[1]/div[1]/div[1]/div[1]/div[2]/h2").text

                print('NOTIFICACAO')
                print(nome)

                # IF THE DROPDOWN IS SHOWED FOR THIS CLIENT
                if self.driver.find_element_by_xpath('/html/body/main[1]/nav/ul/li[1]/span').is_displayed():
                    qntbenef = 'SIM'
                    print('Mais de um beneficio')

                    # DROPDOWN CLICK TO MAKE ITEMS LIST VISIBLE
                    self.driver.find_element_by_xpath('/html/body/main[1]/nav/ul/li[1]/span').click()
                    
                    # DROPDOWN LIST = DROPD
                    dropd = self.driver.find_elements_by_xpath('/html/body/main[1]/nav/ul/li[1]/ul')

                    # PRINT THE ITEMS OF THE DROPDOWN
                    for item in dropd:
                        print(item.text)

                        item.click()

                        nome = self.driver.find_element_by_xpath(
                            "/html/body/main[1]/div[@id='dashboard'][not(contains(@class, 'left hide'))]"
                            "/div[1]/div[1]/div[1]/h2").text

                        print(nome)

            # IF CLIENT CODE DOESN'T HAVE NOTIFICATION
            else:
                nome = self.driver.find_element_by_xpath(
                    "/html/body/main[1]/div[1]/div[1]/div[1]/div[1]/h2").text

                print(nome)

                # IF THE DROPDOWN IS SHOWED FOR THIS CLIENT
                if self.driver.find_element_by_xpath('/html/body/main[1]/nav/ul/li[1]/span').is_displayed():
                    qntbenef = 'SIM'
                    print('Mais de um beneficio')

                    # DROPDOWN CLICK TO MAKE ITEMS LIST VISIBLE
                    self.driver.find_element_by_xpath('/html/body/main[1]/nav/ul/li[1]/span').click()
                    
                    # DROPDOWN LIST = DROPD
                    dropd = self.driver.find_elements_by_xpath('/html/body/main[1]/nav/ul/li[1]/ul')

                    # PRINT THE ITEMS OF THE DROPDOWN
                    for item in dropd:
                        print(item.text)

                        item.click()

                        nome = self.driver.find_element_by_xpath(
                            "/html/body/main[1]/div[@id='dashboard'][not(contains(@class, 'left hide'))]"
                            "/div[1]/div[1]/div[1]/h2").text

                        print(nome)

        # IF THE CLIENT CODE IS WRONG
        except (NoSuchElementException, UnexpectedAlertPresentException):
            nome = ''
            print('CPF Invalido')

        return nome, age, qntbenef, beneficio, concessao, salario, bankslist, bcardlist, consig, card
