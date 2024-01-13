from PhoneBook import PhoneBook

phonebook = PhoneBook()

while True:
    command = input("What Do you want to do ? ")
    if command == 'add':
        name = input("What is Name : ")
        phonenumber = input("What is phonenumber : ")
        phonebook.add_phonebook(name, phonenumber)
    elif command == 'show':
        phonebook.show_phonebook()
    elif command == 'delete':
        name = input('Enter a name to delete :')
        phonebook.delete_phonebook(name)
    elif command == 'exit':
        break
