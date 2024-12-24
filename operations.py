from datetime import *
from time import *
def addBooks():
    print("Read data from user")
    try:
        fh = open('book.txt', 'a')
        B_id = int(input("Enter Book ID:"))
        name = input('Enter the book name')
        author = input('Enter the author name')
        publisher = input('Enter the publisher')
        category = input('Enter the category')
        count = int(input('enter the count of books'))
        data = '%3d,%15s,%15s,%15s,%15s,%3d \n' % (B_id,name,author,publisher,category,count)
        print(data)
        fh.write(data)
        fh.close()
    except FileNotFoundError:
        print('Error inopening a file')
    
    

def searchBook():
    print("Searching for Book:")
    try:
        fh=open('book.txt','r')
        name = input('enter the book name or category:')
        for line in fh:
            if name.lower() in line.lower():
                print(line)
        fh.close()
    except FileNotFoundError:
        print('Error opening a file')

def printList():
    header = '%5s,%15s,%20s,%15s,%15s,%3s' % ("Id","Name","Author","Publisher","Category","Copies")
    print(header)
    try:
        fh=open('book.txt','r')
        for line in fh:
            data = '%5s,%15s,%20s,%15s,%15s,%3s' % tuple(line.split(','))
            print(data)
        
    except FileNotFoundError:
        print('Error opening file')
    finally:
        fh.close()


def addUser():
        print('Adding you to Library')
        fh=open('user.txt','a')
        try:
            u_id = input('enter your user id:')
            pwd = input('enter your password:')
            contact = input('enter you contact details:')
            address = input('enter your address:')
            data = ('%5s,%10s,%12s,%10s\n' % (u_id,pwd,contact,address))
            print(data)
            fh.write(data)
        except FileNotFoundError:
            print('Error opening file')
        finally:
            fh.close()

def deleteUser():
    print('Removing you from library')
    fhr = open('user.txt','r')
    lines = []
    try:
        u_id = input('Enter your user id:')
        data = fhr.readlines()
        for line in data:
            if u_id in line:
                data.remove(line)
            
        else:
            print('User got removed from library')
        write_data = "".join(data)
        fhr.close()
        fhw = open('user.txt','w')
        fhw.write(write_data)
    except FileNotFoundError:
            print('Error opening file')
    finally:
            fhw.close()
def Borrowbooks():
    print('Borrowing Books')
    fh = open('Borrow.txt','a')
    fhu = open('user.txt','r')
    fhb = open('book.txt','r')
    u_id = input('enter user id')
    for lines in fhu:
        if u_id in lines:
            print(lines)
            break
    else:
        print('user not found')
        exit()
    Book_id = input('enter book id')
    books = []
    f = False
    for line in fhb:
        if Book_id in line:
            print(line)
            lst = line.split(',')
            copies = lst[5]
            f = True
            if int(copies.strip()) <= 0:
                print('Sorry!! None of the Copies available of: '+ lst[1])
                exit()
            else:
                lst[5] = str(int(lst[5])-1)
                line = ','.join(lst)
        books.append(line)
    fhb.close()
    fhb = open('book.txt','w')
    fhb.write(''.join(books))
    fhb.close()
    if f == False:
        print('Book not found')
        exit()
    Borrow_date = date.today()
    print( 'Borrow Date : ',Borrow_date)
    Return_date = timedelta(days = 15)
    print( 'Return Date : ',Borrow_date + Return_date)
    data = ('%10s,%5s,%15s,%15s\n' % (u_id,Book_id,Borrow_date,Borrow_date+Return_date))
    print(data)
    fh.write(data)
    fh.close()
    fhu.close()
    
def Returnbooks():
    print('Returning back your book')
    fhb = open('book.txt','r')
    fhB = open('Borrow.txt','r')
    u_id = input('enter user id')
    for lines in fhB:
        if u_id in lines:
            print(lines.split(',')[1])
    book_id = input('enter the book id')
    fhB.seek(0)
    for lines in fhB:
        if u_id in lines and book_id in lines:
            d = lines.split(',')[3].strip()
            
            return_date = date.fromisoformat(d)
            
            today = date.today()
        
            extra_days = today - return_date
            print(extra_days.days)
            if extra_days.days < 0:
                print('you have to pay the fine: ', (-1 * extra_days.days * 100))
            break
    else:
        print(u_id , 'Not found in Borrowed Section')
        exit()

    books = []
    for line in fhb:
        if book_id in line:
            print(line)
            lst = line.split(',')
            
            lst[5] = str(int(lst[5])+1)
            line = ','.join(lst)
            print(line)
        books.append(line)
    
    fhb.close()
    fhb = open('book.txt','w')
    fhb.write(''.join(books))
    fhb.close()
    fhB.close()

def readingSpace():
    fh = open('readingSpace.txt','a')
    fhb = open('book.txt','r')
    name = input('enter your name:')
    category = input('enter the category:')
    for line in fhb:
        if category in line:
            print(line)
    book_id = input('enter the book id:')
    #hours = int(input('enter the number of hours you want to spend:'))
    td = time()
    #time = td.strftime("%I-%M-%S")
    #print(time, type(time))
    data = ('%10s,%10s,%5s,%10d\n' % (name,category,book_id,int(td)))
    
    fh.write(data)
    fh.close()
def exitReadingSpace():
    with open('readingSpace.txt','r') as fh:
        book_id = input('enter the book_id')
        for line in fh:
            if book_id in line:
                entry_time = line.split(',')[3].strip()
                e_t = int(entry_time)
                exit_time = time()
                time1 = int(exit_time) - e_t
                charges = time1//(60*60)
                print("You have to Pay: ", charges*100)
                
        
            
    
    
    
            
            
    
    
    
  
    
        
