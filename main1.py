from admin import Admin
from adminmgmt import Adminmgmt
import random
from user import User
opt=True
while(opt==True):
    print( "WELCOME ,DO You Want To Enter as an User or As Admin")


    
    print("""  
                +++++++++++++++++++++++++
                |                       |    
    \t\t|   1. for Admin menu   |
    \t\t|   2.  for User menu   |  
                |+++++++++++++++++++++++|    
         """)
               



    choice=int(input("Enter your choice:"))
    if(choice==1):
        sup=True
        n=0
        while(n!=3):
            x=random.randint(1000,9999)
            print("Please Re-Enter Captcha:",x)
            user=int(input("Enter Here Above Captcha:"))
            if(user==x):
                print("Congratulation ! You Are Login As a Admin")
                break
        else:
            print("you have Enter incorrect captcha")
        while(sup==True):
            print('''   
                        |+++++++++++++++++++++++++++++
                        |\t1. add New member    |
                        |\t2. search the member | 
                        |\t3. Edit the member   | 
                        |\t4. Delete the Member |  
                        |\t5. view all  Member  |
                        |\t6. create regimen    |
                        |\t7. view regimen      | 
                        |\t8. create package    |             
                        |\t9. Logout           |        
                        |+++++++++++++++++++++++++++++ ''')                                   
            
            num=int(input("Enter your choice:"))
        
            if(num==1):
                ch=0
                while(ch!=1):
                    try:
                        name=input("Enter member Name :")  
                    except (TypeError):
                        print("Enter valid Name..")
                        pass
                    else:
                        ch+=1

                        
                
                ch=0
                while(ch!=1):
                    try:    
                        age=int(input("Enter member Age :"))
                    except ValueError:
                        print("Age should be integer")
                    else:
                        ch+=1
                        
                gender=input("Enter member Gender(M/F/T) :")
                
                ch=0
                while(ch!=1):
                    try:
                        mobile_no=int(input("Enter Member Mobile_No :"))
                    except (ValueError):
                        print("Invalid Mobile Number..")
                    else:
                        ch+=1

                email=input("Enter Member Email Address :")
                
                ch=0
                while(ch!=1):
                    try:
                        bmi=int(input("Enter Member BMI(1.0-35.0) :"))
                    except ValueError:
                        print("Enter BMI in Between 1.0-35.0")
                    else:
                        ch+=1

                ch=0
                while(ch!=1):
                    try:
                        membership_duration=int(input("Enter Member  membership_duration(1/3/6/12month) :"))
                    except ValueError:
                        print("Enter Membership duration in between (1/3/6/12month) ")
                    else:
                        ch+=1
                e=Admin()
                e.create_member(name,age,gender,mobile_no,email,bmi,membership_duration)
                Adminmgmt.add_member(e)

            elif(num==2): 
                ch=0
                while(ch!=1):
                    try:            
                        mb=int(input("Enter Member Mobile_number:"))
                    except ValueError:
                        print("Invalid Mobile Number..")
                    else:
                        ch+=1
                Adminmgmt.search_member(mb)

            elif(num==3):
                ch=0
                while(ch!=1):
                    try:
                        mb=int(input("Enter Member Mobile_number:"))
                    except ValueError:
                        print("Invalid Mobile Number..")
                    else:
                        ch+=1
                Adminmgmt.edit_member(mb)

            elif(num==4):
                ch=0
                while(ch!=1):
                    try:
                        mb=int(input("Enter Member Mobile_number:"))
                    except ValueError:
                        print("Invalid Mobile Number..")
                    else:
                        ch+=1
                Adminmgmt.delete_member(mb)

            elif(num==5):
                Adminmgmt.showall_member()  

            elif(num==6):
                ch=0
                while(ch!=1):
                    try:
                        bmi=int(input("Enter Your BMI :"))
                    except ValueError:
                        print("Enter BMI in Between 1.0-35.0")
                    else:
                        ch+=1
                b=Admin()
                b.regimen(bmi)
                a=b.display_regimen()
                Adminmgmt.create_regimen(bmi,a)   

            elif(num==7):
               Adminmgmt.view_regimen() 

            elif(num==8):
                mb=int(input("Enter Member Mobile_number:"))
                pk=input("Enter Your Package(gold/platinum/silver):")
                a1=Admin()
                a1.create_package(pk)
                e=a1.show_package()
                Adminmgmt.add_package(mb,e) 
            #elif(num==9):
                #Adminmgmt.showinventoryprice() 
                
            elif(num==9):
               print("Logout Succesfully....")
               break
            
        else:
            print("Invalid Input")
        print("Want to Enter More(Y/N) ?")
        sup=input().lower()=="Y"


    
    elif(choice==2):         
        try:
            mobile_no=int(input("Enter Your Mobile No:"))    
        except FileNotFoundError:
            print("file not found")
        else:
            fp=open("ownerfile.txt","r")
            for line in fp:
                line = line.strip()
                line = line.split(",")
                if(mobile_no == int(line[3])):
                    print("|| =======  WELCOME TO FINESS MANTRA  ====== ||")  
        num=0
        while(num<=7):
            print('''
            
                        |++++++++++++++++++++++++++++++|
                        |\t1.view user Profile    |
                        |\t2.Show All Packages    | 
                        |\t3.view user regimen    | 
                        |\t4.view user package    |  
                        |\t5.update membership    |
                        |\t6.Logout               |       
                        |++++++++++++++++++++++++++++++| 
             ''')           
            num=int(input("Enter Your Choice"))           
            if(num==1):
                try:
                    id=input("Enter Your Id(Hint:Enter your mobile_no):")               
                    Adminmgmt.search_user_profile(id)
                except:
                    print("User Profile Not Present..")
            elif(num==2):
                try:
                    e=User.showall_package()
                    Adminmgmt.show_package(e)
                except:
                    print("Please Enter Valid Package..")
            elif(num==3): 
                try:
                    mb=int(input("Enter user mobile no. :"))
                    Adminmgmt.view_user_regimen(mb)
                except ValueError:
                    print("User regimen not present..")
            elif(num==4):  
                try:
                    mb=int(input("Enter user mobile no. :"))
                    Adminmgmt.view_user_package(mb)
                except ValueError:
                    print("User package not present..")

                

            elif(num==5):
                mb=int(input("Enter Member Mobile_number:"))
                Adminmgmt.edit_member(mb)
          
            elif(num==6):
                print("Logout Successfully....")
                print("....THANK YOU BEING OUR VALUED CUSTOMER....")

                break
        
            else:               
                print("invalid Number")
        
            sup=input().lower()=="Y"

            
        

        




            

