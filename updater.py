from um import BOT
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import time
from gspread.exceptions import APIError


class CpfSearch(object):
    def __init__(self, spreadsheet_name):
        self.cpf_col = 1
        self.nome_col = 2
        self.age_col = 3
        self.qnt_benef_col = 4
        self.beneficio_col = 5
        self.concessao_col = 6
        self.salario_col = 7
        self.bancos_col = 8
        self.bancocard_col = 10
        self.consig_col = 11
        self.card_col = 17

        scope = ['https://www.googleapis.com/auth/spreadsheets',
                 'https://www.googleapis.com/auth/drive.readonly']

        creds = ServiceAccountCredentials.from_json_keyfile_name('CONSULTAS.json', scope)

        client = gspread.authorize(creds)

        self.sheet = client.open(spreadsheet_name).sheet1

    def process_cpf_list(self):

        # SKIP OVER COLUMN HEADING IN THE SPREADSHEET
        cpfs = self.sheet.col_values(self.cpf_col)[1:]
        bot_url = BOT()

        for row, cpf in enumerate(cpfs):
            nome, idade, qntbenef, beneficio, concessao, salario, bancos, bancocard, consig, card = bot_url.search_cpfs(cpf)

            # UPDATE THE SHEET
            print("Atualizando...")
            max_retries = 3
            row = row + 2
            while max_retries:
                try:
                    self.sheet.update_cell(row, self.nome_col, nome)
                    self.sheet.update_cell(row, self.age_col, idade)
                    self.sheet.update_cell(row, self.qnt_benef_col, qntbenef)
                    self.sheet.update_cell(row, self.beneficio_col, beneficio)
                    self.sheet.update_cell(row, self.concessao_col, concessao)
                    self.sheet.update_cell(row, self.salario_col, salario)
                    self.sheet.update_cell(row, self.bancos_col, bancos)
                    self.sheet.update_cell(row, self.bancocard_col, bancocard)
                    self.sheet.update_cell(row, self.consig_col, consig)
                    self.sheet.update_cell(row, self.card_col, card)
                    print('Cliente atualizado!')
                    break
                except APIError:
                    max_retries -= 1
                    print('Esperando para atualizar...')
                    time.sleep(50)


cpf_updater = CpfSearch('TESTE')
cpf_updater.process_cpf_list()
