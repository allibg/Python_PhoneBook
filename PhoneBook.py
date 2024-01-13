import pandas as pd


class PhoneBook:
    def __init__(self):
        self.phonebook = pd.DataFrame()
        self.load_phon_book()

    def send_data_to_json(self):
        self.phonebook.to_json('phonebook.json', orient='records')

    def load_phon_book(self):
        self.phonebook = pd.read_json('phonebook.json')

    def add_phonebook(self, name, phoneNumber):
        new_record = pd.DataFrame({"name": name, "phonenumber": phoneNumber}, index=[0])
        self.phonebook = pd.concat([self.phonebook, new_record], ignore_index=True)
        self.send_data_to_json()

    def show_phonebook(self):
        print(self.phonebook.to_string(index=False, col_space=50))

    def delete_phonebook(self, name):
        self.phonebook = self.phonebook.drop(self.phonebook[self.phonebook['name'] == name].index)
        self.send_data_to_json()
    def help_phonebook(self):
        print("\n show : show the phonebook \n add : add a phone number \n delete : delete the phone number \n exit : exit the program")
