l=[];p=[];c=[];p_total=50
def sign():
    key=['Phone','email','password']
    phone=input('enter your phone number: ').lower()
    email=input('enter your email: ').lower()
    password=input('enter your password: ').lower()
    d={'phone':phone,'email':email,'password':password}
    l.append(d)
    print('Your user name is: ',d['email'])
def available_tickets():
    c.append(p_total)
    print("Available Ticket Now:", c[0])
def book_ticket(i):
    if c != []:
        nt=int(input("How many tickets you booked: "))
        p_id=i
        for i in range(nt):
            p_name=input("Enter Passenger name: ").lower()
            p_age=int(input("Enter Passenger age: "))
            p_address=input('Enter your address: ').lower()
            p_email=input("Enter your email: ").lower()
            p_ph=input('Enter your phone number: ').lower()
            p_status='waiting list'
            f={'p_name':p_name,'p_age':p_age,'p_address':p_address,'p_email':p_email,'p_ph':p_ph,'p_status':p_status,'p_id':p_id,'p_nt':nt}
            p.append(f)
            print(f"your booking detail is: {p[i]}")
    else:
        print("Ticket Not Available")
def show_status(i):
    if p != [] :
        print(f"Your Current status: {p[i]['p_status']}")
    else:
        print("You are no ticket booked")
def login():
    username=input('enter your username: ').lower()
    pwd=input('enter your password: ').lower()
    email_list = [e['email'] for e in l]
    i = email_list.index(username)
    if l[i]['email'] in username and l[i]['password'] in pwd:
        print('log in sucess')
        while True:
            n=int(input("1.book_ticket\n2.show_status\n3.available_tickets\n4.exit\n"))
            if n==4:
                break
            elif n==1:
                book_ticket(i)
            elif n==2:
                show_status(i)
            elif n==3:
                available_tickets()
    else:
        print('invalid login...\n     try again...')
def Passenger():
    while True:
        n=int(input("1.signup\n2.login\n3.exit\n"))
        if n==3:
            break
        elif n==1:
            sign()
        elif n==2:
            login()
def approve_remove():
    for i in range(len(l)):
        status=input("if you want accespt\cancel in this id(yes or no): ").lower()
        if status in 'yes':
            p[i]['p_status']='Approved'
            c[0]=c[0]-p[i]['p_nt']
        else:
            p[i]['p_status']='Cancelled'
def c_login():
    c_username=input("Enter Cashior username: ").lower()
    c_pwd=input("Enter Cashior pwd: ").lower()
    if c_username in 'cashior@gmail.com' and c_pwd in 'cash123':
        print("Cashior log in sucess!...")
        while True:
            n=int(input("1.approve_remove\n2.exit\n"))
            if n==2:
                break
            elif n==1:
                approve_remove()
    else:
        print('invalid login...\n     try again...')
def Cashior():
    while True:
        try:
            n=int(input("1.c_login\n2.exit\n"))
            if n==2:
                break
            elif n==1:
                c_login()
        except:
            print("\nINvalid input....\n")
p="\t Python Module \t"
print(p.expandtabs(40))
q="\n\t Welome Flight Reservation System \t"
print(q.expandtabs(35))
print(" \nMain Menu ") 
while True:
    try:
        n=int(input("1.Passenger\n2.Cashior\n3.exit\n"))
        if n==3:
            print('Thank you for using..')
            break
        elif n==1:
            Passenger()
        elif n==2:
            Cashior()
    except:
      print("\nINvalid input....\n")

