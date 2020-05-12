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
        self.bot_url = 'http://www.3kplus.net/'

        self.profile = webdriver.FirefoxProfile()
        self.options = Options()
        self.driver = webdriver.Firefox(firefox_profile=self.profile,
                                        executable_path='C:\\Users\MOISA\Documents\geckodriver.exe',
                                        options=self.options)
        self.driver.maximize_window()

        # NAVIGATE TO URL
        self.driver.get(self.bot_url)

        login_box = self.driver.find_element_by_xpath('//*[@id="login"]/div[3]/div[2]/div[2]/input')
        login_box.send_keys('edivania')

        pass_box = self.driver.find_element_by_xpath('//*[@id="login"]/div[3]/div[2]/div[3]/input')
        pass_box.send_keys('789456')

        login_btn = self.driver.find_element_by_xpath('//*[@id="login"]/div[3]/div[2]/button')
        login_btn.click()

        time.sleep(2)



    def search_cpfs(self, cpf):

        # SEARCH THROUGH THE LIST OF CLIENT CODES (1ST COLLUM OF THE SPREADSHEET), AND OBTAIN THESE INFOS

        print(f"Procurando {cpf}.")
        self.driver.get(self.bot_url)
        qntbenef = ''

        # SEARCH CLIENT CODE
        # CLIENT CODE IS VALID
        try:
            cpf_input = self.driver.find_element_by_xpath('//*[@id="search"]/div/div[1]/input')
            cpf_input.send_keys(cpf)

            cpf_btn = self.driver.find_element_by_xpath('//*[@id="search"]/div/div[2]/button')
            cpf_btn.click()

            print('CPF Valido')

            time.sleep(2)

            # CLIENT CODE HAVE NOTIFICATION
            if self.driver.find_element_by_xpath('//*[@id="notification"]').is_displayed():

                nome = self.driver.find_element_by_xpath(
                    "/html/body/main[1]/div[1]/div[1]/div[1]/div[2]/h2").text
                idade = self.driver.find_element_by_xpath(
                    "/html/body/main[1]/div[1]/div[1]/div[1]/div[2]/ul/li[2]").text
                age = re.search(r'\((.*?)Anos', idade).group(1)
                qntbenef = ''
                beneficio = self.driver.find_element_by_xpath(
                    "/html/body/main[1]/div[1]/div[1]/div[1]/div[3]/div[5]/span/b   ").text
                concessao = self.driver.find_element_by_xpath(
                    "/html/body/main[1]/div[1]/div[1]/div[1]/div[3]/div[2]/span").text
                salario = self.driver.find_element_by_xpath(
                    "/html/body/main[1]/div[1]/div[2]/div/div[3]/div[1]/div[1]/span").text
                bancos = self.driver.find_element_by_xpath('//*[@id="loans"]').text
                bancosw = re.findall(r'(?<=Banco )(\w+)', bancos)
                bankslist = ', '.join(bancosw)
                bancocard = self.driver.find_element_by_xpath('//*[@id="cards"]').text
                bcardw = re.findall(r'(?<=Banco )(\w+)', bancocard)
                bcardlist = ', '.join(bcardw)
                consig = self.driver.find_element_by_xpath(
                    "/html/body/main[1]/div[1]/div[1]/div[3]/div[2]/span").text
                card = self.driver.find_element_by_xpath(
                    "/html/body/main[1]/div[1]/div[1]/div[3]/div[3]/span").text

                print('NOTIFICACAO')
                print(nome, age, beneficio, concessao, salario, bankslist, bcardlist, consig, card)

            # CLIENT CODE DOESN'T HAVE NOTIFICATION
            else:
                nome = self.driver.find_element_by_xpath(
                    "/html/body/main[1]/div[1]/div[1]/div[1]/div[1]/h2").text
                idade = self.driver.find_element_by_xpath(
                    "/html/body/main[1]/div[1]/div[1]/div[1]/div[1]/ul/li[2]").text
                age = re.search(r'\((.*?)Anos', idade).group(1)
                qntbenef = ''
                beneficio = self.driver.find_element_by_xpath(
                    "/html/body/main[1]/div[1]/div[1]/div[1]/div[2]/div[5]/span/b").text
                concessao = self.driver.find_element_by_xpath(
                    "/html/body/main[1]/div[1]/div[1]/div[1]/div[2]/div[2]/span").text
                salario = self.driver.find_element_by_xpath(
                    "/html/body/main[1]/div[1]/div[2]/div/div[3]/div[1]/div[1]/span").text
                bancos = self.driver.find_element_by_xpath('//*[@id="loans"]').text
                bancosw = re.findall(r'(?<=Banco )(\w+)', bancos)
                bankslist = ', '.join(bancosw)
                bancocard = self.driver.find_element_by_xpath('//*[@id="cards"]').text
                bcardw = re.findall(r'(?<=Banco )(\w+)', bancocard)
                bcardlist = ', '.join(bcardw)
                consig = self.driver.find_element_by_xpath(
                    "/html/body/main[1]/div[1]/div[1]/div[3]/div[2]/span").text
                card = self.driver.find_element_by_xpath(
                    "/html/body/main[1]/div[1]/div[1]/div[3]/div[3]/span").text

                print(nome, age, beneficio, concessao, salario, bankslist, bcardlist, consig, card)

                # IF THE DROPDOWN IS SHOWED
                if self.driver.find_element_by_xpath('/html/body/main[1]/nav/ul/li[1]/span').is_displayed():
                    qntbenef = 'SIM'
                    print('Mais de um beneficio')

                    # DROPDOWN CLICK TO MAKE ITEMS VISIBLE
                    self.driver.find_element_by_xpath('/html/body/main[1]/nav/ul/li[1]/span').click()

                    dropd = self.driver.find_elements_by_xpath('/html/body/main[1]/nav/ul/li[1]/ul/li')

                    # PRINT THE ITEMS OF THE DROPDOWN

                    for item in dropd:

                        print(item.text)

                        item.click()

                        beneficio1 = self.driver.find_element_by_xpath(
                            "/html/body/main[1]/div[@id='dashboard'][not(contains(@class, 'left hide'))]"
                            "/div[1]/div[1]/div[2]/div[5]/span/b").text

                        print(beneficio1)

                        self.driver.find_element_by_xpath('/html/body/main[1]/nav/ul/li[1]/span').click()

        # IF THE CLIENT CODE IS WRONG
        except (NoSuchElementException, UnexpectedAlertPresentException):
            nome = ''
            idade = ''
            age = ''
            beneficio = ''
            concessao = ''
            salario = ''
            bancos = ''
            bancosw = ''
            bankslist = ''
            bancocard = ''
            bcardw = ''
            bcardlist = ''
            consig = ''
            card = ''
            print('CPF Invalido')

        return nome, age, qntbenef, beneficio, concessao, salario, bankslist, bcardlist, consig, card
