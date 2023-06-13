
def sal_cal():
    n=input("Enter Employee name: ")
    n_id=int(input("Enter Employee ID: "))
    s=int(input("Enter Employee monthly salary: "))
    tds=(6/100)*s
    leave=int(input("Enter your leave: "))
    b=200
    d=int(input("Enter Month: "))
    print("-----------------------------Output-------------------------------")
    if (d==1):
      print("Date: Jan/2023")
    elif (d==2):
      print("Date: Feb/2023")
    elif (d==3):
      print("Date: March/2023")
    elif (d==4):
      print("Date: April/2023")
    elif (d==5):
      print("Date: May/2023")
    elif (d==6):
      print("Date: June/2023")
    elif (d==7):
      print("Date: July/2023")
    elif (d==8):
      print("Date: Aug/2023")
    elif (d==9):
      print("Date: Sept/2023")
    elif (d==10):
      print("Date: Oct/2023")
    elif (d==11):
      print("Date: Nov/2023")
    elif (d==12) :
      print("Date: Dec/2023")
    else:
      print("Enter valid month")
    
    print("Employee name:",n)
    print("Employee id:",n_id)
    print("Employee salary:",s)
    print("TDS:6%:",tds)
    print("Leave: ",leave*1000)
    print("Bonus: ",b)
    
    return s-(tds+leave)+b

print(" The final salary is : ",sal_cal())




