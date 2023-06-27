class passenger:
    def __init__(self,na,a,g,p,uid):
        self.na=na
        self.a=a
        self.g=g
        self.p=p
        self.uid=uid
        self.bd=0
        self.st=False
        self.cost=0
class detail:
    def __init__(self):
        self.l=[]
        self.id=101
d=detail()
class Ticket:
    def __init__(self):
        self.tn=50
t=Ticket()
class Booked:
    def __init__(self,bd):
        pass
def signup():
    na=input("Enter Name:")
    a=input("Enter Age:")
    if a >="18":
        g=input("Enter Gender:")
        pwd=input("Enter Password:")
        e=passenger(na,a,g,pwd,d.id)
        d.l.append(e)
        print('Your passenger id:',d.id)
        d.id+=1
    else:
        print('...Incorrect...')
def check():
    print("Total no of tickets:",50)
    print("Available Ticket:",t.tn)
    print("Price per ticket:",2000)
def bookticket(x):
    tc=int(input("Enter no of ticket booked:"))
    d.l[x-101].cost=tc*2000
    print("cost of your ticket is:",d.l[x-101].cost)
    d.l[x-101].bd=tc
def status(x):
    if d.l[x-101].st==True:
        print("...your ticket is Approve...")
    elif d.l[x-101].st==101:
        print("...your ticket is Cancelled...")
    else:
        print('...your ticket is waiting...')   
def cashier():
    x="csh1001"
    y="123"
    u=input("Enter cashier id:")
    pd=input("Enter cashier pd:")
    if x in u and y in pd:
        print("...Log in Success...")
        while True:
            opt=int(input("1.Approve\n2.Cancel\n3.logout\n"))
            if opt==3:
                break
            elif opt==1:
                Approve()
            elif opt==2:
                Cancel()
    else:
        print(".....Incorrect.....")
def Approve():
    x=int(input("Enter passenger id you want to Approve:"))
    if d.l[x-101].uid==x:
        print(".....Your Ticket is approved.....")
    t.tn=t.tn-d.l[x-101].bd
    d.l[x-101].st=True
def Cancel():
    x=int(input("Enter passenger id you want to cancelled:"))
    if d.l[x-101].uid==x:
        print(".....Your Ticket is cancelled.....")
        d.l[x-101].st=101
def login():
    x=int(input('Enter your Id:'))
    pw=input('Enter your Password:')
    if d.l[x-101].uid==x and d.l[x-101].p==pw:
        print(".....success.....")
        while True:
            opt=int(input('1.check\n2.bookticket\n3.status\n4.logout\n'))
            if opt==4:
                break
            elif opt==1:
                check()
            elif opt==2:
                bookticket(x)
            elif opt==3:
                status(x)
            else:
                print('...Invalid...')
    else:
        print("...Incorrect...")
p="\t Python Module \t"
print(p.expandtabs(40))
q="\n\t Flight Reservation System \t"
print(q.expandtabs(35))
print(" \nMain Menu ")        
while True:
    n=int(input('1.passenger\n2.cashier\n3.exit\n'))
    if n==3:
        break
    elif n==1:
        while True:
            opt=int(input('1.signup\n2.login\n3.exit\n'))
            if opt==3:
                break
            elif opt==1:
                signup()
            elif opt==2:
                login()
            else:
                print('....Invalid options....')
    elif n==2:
        cashier()
        









