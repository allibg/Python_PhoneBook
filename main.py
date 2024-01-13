from PhoneBook import PhoneBook

phonebook = PhoneBook()

while True:
    command = input("What Do you want to do (if you need help , type: help) ? ")
    if command == 'add':
        name = input("What is Name : ")
        phonenumber = input("What is phonenumber : ")
        phonebook.add_phonebook(name, phonenumber)
    elif command == 'show':
        phonebook.show_phonebook()
    elif command == 'delete':
        name = input('Enter a name to delete :')
        phonebook.delete_phonebook(name)
    elif command == 'help':
        phonebook.help_phonebook()
    elif command == 'exit':
        break
