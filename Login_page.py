from operations import *
import os
print("Welcome to My Library")
uid = input("Enter User ID:")
pwd = input("Enter your Password:")
os.system('cls')
uid = 'admin'
pwd = 'library'
if uid=='admin' and pwd=='library':
    while(True):
        print('MAIN MENU:\n'+
              '1 Add books\n'
              + '2 Search books\n'
              + '3 List of all books\n'
              + '4 Add user \n'
              + '5 Delete user\n'
              + '6 Borrow Books\n'
              + '7 Return Books\n'
              + '8 Reading Space\n'
              + '9 exit reading space\n'
              + '10 Exit')
        choice = int(input("Enter your choice"))
        if choice == 1:
            addBooks()
        elif choice == 2:
            searchBook()
        elif choice == 3:
            printList()
        elif choice == 4:
            addUser()
        elif choice == 5:
            deleteUser()
        elif choice == 6:
            Borrowbooks()
        elif choice == 7:
            Returnbooks()
        elif choice == 8:
            readingSpace()
        elif choice == 9:
            exitReadingSpace()
        else:
            exit()
        
        yesNo = input('DO you want to continue(y or n):')
        if yesNo == 'n' or yesNo == 'N':
            break
