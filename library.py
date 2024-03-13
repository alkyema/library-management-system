import mysql.connector


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="satwik890",
  database="library"
)

mycursor = mydb.cursor()

def show_admin():
    sql = "select name from ad_id"
    mycursor.execute(sql)
    names = (mycursor.fetchall())
    for i in range(len(names)) :
        print(names[i][0])
    aa = input("press any key to continue : ")

        
def show_student():
    sql = "select name from st_id"
    mycursor.execute(sql)
    names = (mycursor.fetchall())
    for i in range(len(names)):
        print(names[i][0])
    aa = input("press any key to continue : ")


def delete_student():
    print("delete by NAME or ID ")
    print("1)By name")
    print("2)By ID")
    print("3)Exit")
    a = input("Your choice(1-3) : ")
    
    if(a == '1'):
        user = input("Enter the username of student : ")
        sql = "delect from st_id where name = \"{}\""
        query = sql.fromat(user)
        
    elif(a == '2'):
        try:
            id = int(input("Enter the student id : "))
        except ValueError:
            print("Wrong entry")
        sql = "delete from st_id where id = {}"
        query = sql.format(id)
        
    else:
        return
    
    print("Press 1 to continue\nPress any key to exit")
    b = input("Your choice : ")
    
    if(b == '1'):
        try:
            mycursor.execute(query)
            print("Deleted successfully!!")
            aa = input("press any key to continue : ")
        except:
            print("Error!!!")
    else:
        print("Exiting...")
        return

    
def add_admin():
    sql = "select id from ad_id order by id desc limit 1"
    mycursor.execute(sql)
    id = (mycursor.fetchall()[0][0]) + 1
    username=input("Enter username : ")
    password = input("Enter password :")
    sql = "insert into ad_id(id,name,password) values ({},\"{}\",\"{}\")"
    query = sql.format(id,username,password)
    a = input("Press 1 to confirm\nPress any key to exit\nYour choice : ")
    if(a=='1'):
        try:
            mycursor.execute(query)
            print("ID created successfully")
            print("Your admin ID is",id)
            aa = input("press any key to continue : ")
        except:
            print("Something went wrong !!")
    else :
        return


def show_books():
    sql = "select name from books"
    mycursor.execute(sql)
    names = mycursor.fetchall()
    for i in range(len(names)):
        print(i,names[i][0])
    aa = input("press any key to continue : ")
        

def add_book():
    sql = "select Book_id from books order by Book_id desc limit 1"
    mycursor.execute(sql)
    id = mycursor.fetchall()[0][0] + 1
    sql = "insert into books(Book_id,Name,Author,Price,Quantity) values ({},\"{}\",\"{}\",{},{})"
    name = input("Enter the book name : ")
    author = input("Enter the Author's name : ")
    try :
        price = int(input("Enter the price : "))
    except ValueError:
        print("Wrong")
        return
    try:
        quantity = int(input("Enter the quantity : "))
    except ValueError:
        print("Wrong")
        return
    try:
        query = sql.format(id,name,author,price,quantity)
    except UnboundLocalError:
        print("Wrong entry !!!")
        return
    print("Press 1 to continue\nPress any key to cancel")
    a = input("Your choice : ")
    
    if (a == '1'):
        try:
            mycursor.execute(query)
            print("Book added successfully")
            print("Book_id :",id)
            print("name :",name)
            print("Author :",author)
            print("Price :",price)
            print("Quantity :",quantity)
            aa = input("press any key to continue : ")
        except :
            print("Wrong entry !!!")
    else:
        print("Exiting...") 
    
    
def delete_admin():
    print("Delete\n1)By ID\n2)By name")
    a = input("Your choice : ")
    if (a == '1'):
        try:
            id = int(input("Enter the student id : "))
        except ValueError:
            print("Wrong entry")
        sql = "delete from ad_id where id = {}"
        query = sql.format(id)
        
    elif(a == '2'):
        name = input("Enter the Name : ")
        sql = "delete from ad_id where name = \"{}\""
        query = sql.format(name)
    
    else :
        print("Exiting...")
        return
    
    print("Press 1 to confirm\nPress any key to exit")
    b = input("Your choice : ")
    if b == '1':
        try:
            mycursor.execute(query)
            print("Deleted successfully!!")
            aa = input("press any key to continue : ")
        except:
            print("Wrong input !!!")
    else:
        return

    
def search_book():
    print("1)Search by Book Name")
    print("2)Search by ID")
    print("3)Search by Author's Name")
    print("4)Search by Price range")
    print("5)Exit")
    a = input("Your choice(1-5) : ")
    match a:
        case '1':
            sql = "select * from books where Name = \"{}\""
            name = input("Enter the book name : ")
            query = sql.format(name)
            try:
                mycursor.execute(query)
                detail = mycursor.fetchall()
                print("\nBook Found\nBook_id :",detail[0][0])
                print("Name :",detail[0][1])
                print("Author's name :",detail[0][2])
                print("Price :",detail[0][3])
                print("Quantity :",detail[0][4])
                aa = input("press any key to continue : ")
            except:
                print("Book Not Found")
                
        case '2':
            sql = "select * from books where Book_id = {}"
            try:
                ID = int(input("Enter the book id : "))
            except ValueError:
                print("Wrong entry!!")
            query = sql.format(ID)
            try:
                mycursor.execute(query)
                detail = mycursor.fetchall()
                print("\nBook Found\nBook_id :",detail[0][0])
                print("Name :",detail[0][1])
                print("Author's name :",detail[0][2])
                print("Price :",detail[0][3])
                print("Quantity :",detail[0][4])
                aa = input("press any key to continue : ")
            except:
                print("Book Not Found")

        case '3':
            sql = "select * from books where Author = \"{}\""
            name = input("Enter the Author's name : ")
            query = sql.format(name)
            try:
                mycursor.execute(query)
                detail = mycursor.fetchall()
                print("\nBook Found\nBook_id :",detail[0][0])
                print("Name :",detail[0][1])
                print("Author's name :",detail[0][2])
                print("Price :",detail[0][3])
                print("Quantity :",detail[0][4])
                aa = input("press any key to continue")
            except:
                print("Book Not Found")

        case '4':
            sql = "select * from books where Price <{} and Price >{}"
            minprice = input("Enter the min price : ")
            maxprice = input("Enter the max price : ")
            query = sql.format(minprice,maxprice)
            try:
                mycursor.execute(query)
                detail = mycursor.fetchall()
                print("\nBook Found\nBook_id :",detail[0][0])
                print("Name :",detail[0][1])
                print("Author's name :",detail[0][2])
                print("Price :",detail[0][3])
                print("Quantity :",detail[0][4])
                aa = input("press any key to continue : ")
            except:
                print("Book Not Found")
        
        case '5':
            print("Exiting...")
            return
        
        case default:
            print("Wrong input !!")
            return


def change_password(Id):
    sql = "update ad_id set password = \"{}\" where id = {}"
    password = input("Enter new password : ")
    query  = sql.format(password,Id)
    print("Press 1 to continue\nPress any to exit")
    a = input("Your input : ")
    if a == '1':
        try:
            mycursor.execute(query)
            print("changed successfull!!")
            aa = input("press any key to continue : ")
        except:
            print("Wrong input!!")
    else:
        print("Exiting...")
        return


def change_name(Id):
    sql = "update ad_id set name = \"{}\" where id = {}"
    password = input("Enter new name : ")
    query  = sql.format(password,Id)
    print("Press 1 to continue\nPress any to exit")
    a = input("Your input : ")
    if a == '1':
        try:
            mycursor.execute(query)
            print("changed successfully")
            aa = input("press any key to continue : ")
        except:
            print("Wrong input!!")
    else:
        print("Exiting...")
        return


def edit_book():
    print("1)Change book name")
    print("2)Change Author's name")
    print("3)Change book price")
    print("4)change book quantity")
    print("5)Exit")
    choice = input("Your choice(1-5) : ")
    match choice :
        case '1':
            sql = "update books set Name = \"{}\" where Book_id = {}"
            try:
                Id = int(input("Enter the book_id : "))
            except ValueError:
                print("Wrong input")
            name = input("Enter the new name : ")
            query = sql.format(name,Id)
            print("Press 1 to confirm\nPress any key to exit")
            a = input("Your choice : ")
            if a == '1':
                try:
                    mycursor.execute(query)
                    print("Changed successfully!")
                    aa = input("press any key to continue : ")
                except:
                    print("Error!!")
            else :
                print("Exiting...")
                
        case '2':
            sql = "update books set Author = \"{}\" where Book_id = {}"
            try:
                Id = int(input("Enter the book_id : "))
            except ValueError:
                print("Wrong input")
            name = input("Enter the new name : ")
            query = sql.format(name,Id)
            print("Press 1 to confirm\nPress any key to exit")
            a = input("Your choice : ")
            if a == '1':
                try:
                    mycursor.execute(query)
                    print("Changed successfully!")
                    aa = input("press any key to continue : ")
                except:
                    print("Error!!")
            else :
                print("Exiting...")
                
        case '3':
                sql = "update books set Price = \"{}\" where Book_id = {}"
                try:
                    Id = int(input("Enter the book_id : "))
                except ValueError:
                    print("Wrong input")
                try:
                    price = int(input("Enter the new price : "))
                except ValueError:
                    print("Wrong input")
                query = sql.format(price,Id)
                print("Press 1 to confirm\nPress any key to exit")
                a = input("Your choice : ")
                if a == '1':
                    try:
                        mycursor.execute(query)
                        print("Changed successfully!")
                        aaa = input("press any key to continue : ")
                    except:
                        print("Error!!")
                else :
                    print("Exiting...")
            
        case '4':
                sql = "update books set Quantity = \"{}\" where Book_id = {}"
                try:
                    Id = int(input("Enter the book_id : "))
                except ValueError:
                    print("Wrong input")
                try:
                    quantity = int(input("Enter the quantity : "))
                except ValueError:
                    print("Wrong input")
                query = sql.format(quantity,Id)
                print("Press 1 to confirm\nPress any key to exit")
                a = input("Your choice : ")
                if a == '1':
                    try:
                        mycursor.execute(query)
                        print("Changed successfully!")
                        aa = input("press any key to continue : ")
                    except:
                        print("Error!!")
                else :
                    print("Exiting...")
            
        case '5':
            print("exiting...")
            return
        
        case default:
            print("Wrong input")
            return


def admin(Id):
    print("Welcome admin")
    while True:
        print("1)Show admin")
        print("2)Show students")
        print("3)Delete student")
        print("4)Add student")
        print("5)Add admin")
        print("6)show Books")
        print("7)Add Book")
        print("8)Delete admin")
        print("9)search book")
        print("10)Edit book")
        print("11)change password")
        print("12)change admin name")
        print("13)Exit")
        choice = input("Your choice(1-13) : ")
        match choice:
            case '1':
                print()
                show_admin()
            
            case '2':
                print()
                show_student()
            
            case '3':
                print()
                delete_student()
            
            case '4' :
                print()
                create()
            
            case '5':
                print()
                add_admin()
            
            case '6':
                print()
                show_books()
            
            case '7':
                print()
                add_book()
                
            case '8':
                print()
                delete_admin()
            
            case '9':
                search_book()
            
            case '10':
                print()
                edit_book()
            
            case '11':
                print()
                change_password(Id)
            
            case '12':
                print()
                change_password(Id)
            
            case '13':
                return
            
            case default:
                print("Wrong input")
                pass
    

def issue_book(Id):
    sql1 = "select book1,book2,book3 from st_id where id = {}"
    query = sql1.format(Id)
    mycursor.execute(query)
    data = mycursor.fetchall()
    if data[0][0] == 0:
        sql = "update st_id set book1 = {} where id = {}"
        bid = input("Enter the Bookid of the book you want to issue : ")
        sql2 = "select found,Name from books where Book_id = {}"
        check = sql2.format(bid)
        try: 
            mycursor.execute(check)
            value = mycursor.fetchall()
        except:
            print("No book found")
        if value[0][0] == 1:
            print("Are you sure you want to issue this book ?")
            print(value[0][1])
            print("Press 1 to confirm\nPress any key to exit")
            choice = input("Your choice : ")
            if choice == '1':
                query = sql.format(bid,Id)
                try :
                    mycursor.execute(query)
                    print("Issued successfully")
                except:
                    print("Something went wrong!!")
        
    elif data[0][1] == 0:
        sql = "update st_id set book2 = {} where id = {}"
        bid = input("Enter the Bookid of the book you want to issue : ")
        sql2 = "select found,Name from books where Book_id = {}"
        check = sql2.format(bid)
        try: 
            mycursor.execute(check)
            value = mycursor.fetchall()
        except:
            print("No book found")
        if value[0][0] == 1:
            print("Are you sure you want to issue this book ?")
            print(value[0][1])
            print("Press 1 to confirm\nPress any key to exit")
            choice = input("Your choice : ")
            if choice == '1':
                query = sql.format(bid,Id)
                try :
                    mycursor.execute(query)
                    print("Issued successfully")
                except:
                    print("Something went wrong!!")
    elif data[0][2] == 0:
        sql = "update st_id set book3 = {} where id = {}"
        bid = input("Enter the Bookid of the book you want to issue : ")
        sql2 = "select found,Name from books where Book_id = {}"
        check = sql2.format(bid)
        try: 
            mycursor.execute(check)
            value = mycursor.fetchall()
        except:
            print("No book found")
        if value[0][0] == 1:
            print("Are you sure you want to issue this book ?")
            print(value[0][1])
            print("Press 1 to confirm\nPress any key to exit")
            choice = input("Your choice : ")
            if choice == '1':
                query = sql.format(bid,Id)
                try :
                    mycursor.execute(query)
                    print("Issued successfully")
                except:
                    print("Something went wrong!!")
    else :
        print("You have already issued maximum number of books")


def return_book(Id):
    try:
        bid = int(input("Enter the bookid of the book you want to return : "))
    except ValueError:
        print("Wrong input!!")
    sql1 = "select book1,book2,book3 from st_id where id = {}"
    query = sql1.format(Id)
    mycursor.execute(query)
    data = mycursor.fetchall()
    if data[0][0] == bid:
        sql = "update st_id set book1 = 0 where id = {}"
        query = sql.format(Id)
        sql1 = "select Name from books where Book_id = {}"
        query1 = sql1.format(bid)
        mycursor.execute(query1)
        name = mycursor.fetchall()
        print("Are you sure you want to return book ?")
        print(name[0][0])
        print("Press 1 to confirm\nPress any any to cancel")
        a = input("your choice : ")
        if a == '1':
            try:
                mycursor.execute(query)
                print("Returned sucessfully")
            except:
                print("unexpected error")
    elif data[0][1] == bid:
        sql = "update st_id set book2 = 0 where id = {}"
        query = sql.format(Id)
        sql1 = "select Name from books where Book_id = {}"
        query1 = sql1.format(bid)
        mycursor.execute(query1)
        name = mycursor.fetchall()
        print("Are you sure you want to return book ?")
        print(name[0][0])
        print("Press 1 to confirm\nPress any any to cancel")
        a = input("your choice : ")
        if a == '1':
            try:
                mycursor.execute(query)
                print("Returned sucessfully")
            except:
                print("unexpected error")
    elif data[0][2] == bid:
        sql = "update st_id set book2 = 0 where id = {}"
        query = sql.format(Id)
        sql1 = "select Name from books where Book_id = {}"
        query1 = sql1.format(bid)
        mycursor.execute(query1)
        name = mycursor.fetchall()
        print("Are you sure you want to return book ?")
        print(name[0][0])
        print("Press 1 to confirm\nPress any any to cancel")
        a = input("your choice : ")
        if a == '1':
            try:
                mycursor.execute(query)
                print("Returned sucessfully")
            except:
                print("unexpected error")
    else:
        print("Book not found")


def show_issue(Id):
    sql ="select book1,book2,book3 from st_id where id = {}"
    query = sql.format(Id)
    mycursor.execute(query)
    data = mycursor.fetchall()
    
    if data[0][1] == 0 and data[0][0] == 0 and data[0][2] == 0:
        print("No book are issued")

    else:
        if data[0][0] != 0 :
            sql1 = "select Name from books where Book_id = {}"
            query1 = sql1.format(data[0][0])
            try:
                mycursor.execute(query1)
                name1 = mycursor.fetchall()[0][0]
                print(name1)
            except:
                pass
        
        if data[0][1] != 0:
            sql1 = "select Name from books where Book_id = {}"
            query1 = sql1.format(data[0][1])
            try:
                mycursor.execute(query1)
                name1 = mycursor.fetchall()[0][0]
                print(name1)
            except:
                pass
            
        if data[0][2] != 0:
                sql1 = "select Name from books where Book_id = {}"
                query1 = sql1.format(data[0][2])
                try:
                    mycursor.execute(query1)
                    name1 = mycursor.fetchall()[0][0]
                    print(name1)
                except:
                    pass


def st_pass(Id):
    sql = "update st_id set password = \"{}\" where id = {}"
    password = input("Enter new password : ")
    query  = sql.format(password,Id)
    print("Press 1 to continue\nPress any to exit")
    a = input("Your input : ")
    if a == '1':
        try:
            mycursor.execute(query)
            print("changed successfull!!")
            aa = input("press any key to continue : ")
        except:
            print("Wrong input!!")
    else:
        print("Exiting...")
        return


def st_name(Id):
    sql = "update st_id set name = \"{}\" where id = {}"
    password = input("Enter new name : ")
    query  = sql.format(password,Id)
    print("Press 1 to continue\nPress any to exit")
    a = input("Your input : ")
    if a == '1':
        try:
            mycursor.execute(query)
            print("changed successfully")
            aa = input("press any key to continue : ")
        except:
            print("Wrong input!!")
    else:
        print("Exiting...")
        return

        
def student(Id):
    print("Welcome student")
    
    while True:
        print("1)Show books")
        print("2)Search books")
        print("3)Issue book")
        print("4)Return book")
        print("5)Show issued book")
        print("6)Change username")
        print("7)change password")
        print("8)Exit")
        choice  = input("Your choice(1-8) : ")
        
        match choice:
            case '1':
                show_books()
            
            case '2':
                search_book()
            
            case '3':
                issue_book(Id)
            
            case '4':
                return_book(Id)
            
            case '5':
                show_issue(Id)
            
            case '6':
                st_name(Id)
            
            case '7':
                st_pass(Id)
            
            case '8':
                print("Exiting...")
                return
            
            case default:
                print("wrong input try again")
                

def login():
    username=input("Enter username : ")
    password = input("Enter password :")
    sql = "SELECT found FROM ad_id WHERE name = \"{}\" and password = \"{}\""
    query = sql.format(username,password)
    mycursor.execute(query)
    userid = (mycursor.fetchall())
    try: 
        userid[0][0] == 1
        print("Acess Granted")
        sql = "SELECT id FROM ad_id WHERE name = \"{}\""
        query = sql.format(username)
        mycursor.execute(query)
        Id = mycursor.fetchall()[0][0]
        admin(Id)
        
    except :
        sql = "SELECT found FROM st_id WHERE name = \"{}\" and password = \"{}\""
        query = sql.format(username,password)
        mycursor.execute(query)
        userid = (mycursor.fetchall())
        try: 
            userid[0][0] == 1
            print("Acess Granted")
            sql = "SELECT id FROM st_id WHERE name = \"{}\""
            query = sql.format(username)
            mycursor.execute(query)
            Id = mycursor.fetchall()[0][0]
            student(Id)
        except:
            print("Acess Denied")


def create():
    sql = "select id from st_id order by id desc limit 1"
    mycursor.execute(sql)
    Id = (mycursor.fetchall()[0][0]) + 1
    username=input("Enter username : ")
    password = input("Enter password :")
    sql = "insert into st_id(id,name,password) values ({},\"{}\",\"{}\")"
    query = sql.format(Id,username,password)
    a = input("Press 1 to confirm\nPress any key to exit\nYour choice : ")
    if(a=='1'):
        try:
            mycursor.execute(query)
            print("ID created successfully")
            print("Your student ID is",Id)
        except:
            print("Something went wrong !!")
    else :
        return


__name__ == '__main__'
print("Library management system")
choice = input("\n1)Login\n2)Create ID\n3)Exit\nyour choice(1-3) : ")

match choice:
    case '1':
        login()
    
    case '2':
        create()
        
    case '3':
        print("Exiting...")
        
    case default:
        print("Wrong input !!!")

mydb.commit()

mycursor.close()
mydb.close()
