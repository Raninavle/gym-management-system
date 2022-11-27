
from admin import Admin
from user import User
class Adminmgmt:
    def add_member(e):
        with open("ownerfile.txt","a")as fp:
            fp.write(str(e))
            fp.write("\n")

    def showall_member():
        try:
            fp=open("ownerfile.txt","r")
        except(FileNotFoundError):
            print("File does not Exit")
        else:
            data=fp.read()
            print(data)
            fp.close

    def search_member( mobile_no):
        try:
            fp= open("ownerfile.txt","r")
        except FileNotFoundError:
            print("file dose not exit")
        else:
            for x in fp:
                line=x.strip()
                line=x.split(",")
                if(mobile_no==int(line[3])):
                    print(line)
                    break
            else:
                print("Member is not Found")

    def delete_member(mobile_no):
        try:
            fp= open("ownerfile.txt","r")
        except FileNotFoundError:
            print("file dose not exit")
        else:
            found=False
            allmember=[]
            for line in fp:
                line=line.strip()
                line=line.split(",")
                if(mobile_no==int(line[3])):
                   found=True
                else:
                    allmember.append(line) 

            fp.close()      
            if(found):
                fp= open("ownerfile.txt",'w')
                for x in allmember:
                    x=",".join(x)
                    x+="\n"
                    fp.write(x)
                fp.close()
                print("Member deleted successfully")    
            else:
                print("Member not found")

    def edit_member(mobile_no):
        try:
            fp = open("ownerfile.txt","r")            
        except FileNotFoundError:
            print("File does not exist")
        else:     
            found=False
            allmember = []
            for line in fp:
                line = line.strip()
                line = line.split(",")
                if(mobile_no == int(line[3])):
                    found = True 
                    ans=input("DO You want to change Membership_duration ?  ")    
                    if(ans.lower()=="y" or "yes"):
                        line[6]=input("Enter  new membership_duration: ")
                allmember.append(line)
            #print(allmember)
            fp.close()
            if(found):
                fp=open("ownerfile.txt",'w')
                for x in allmember:
                    x=",".join(x)
                    x+="\n"
                    fp.write(x)
                fp.close()
                print("Record update SuccessFully")
            else:
                print("Record Not Found")

    def create_regimen(bmi,a):
        try:
            fp=open("ownerfile.txt","r")
        except FileNotFoundError:
            print("file does not found")
        else:
            found=False
            new=[]
            for line in fp :
                line= line.strip()
                line = line.split(",")
                if(bmi==int(line[5])):
                    found=True
                    print("found")
                    line.append(str(a))  
                    new.append(line)             
            if (found):
                fp = open("Workout.txt","a") 
                for i in new:
                    i=",".join(i)   
                    i+="\n"
                    fp.write(i)
                #fp.write(str(line))
                #fp.write("\n")
                fp.close()
                
        fp.close()   
        

    def view_regimen():
        try:
            fp=open("workout.txt","r")          
        except(FileNotFoundError):
            print("File does not Exit")
        else:    
            data=fp.read()
            print(data)
            fp.close


    def add_package(mb,e):
        try:
            fp=open("ownerfile.txt","r")
        except FileNotFoundError:
            print("file does not found")
        else:
            found=False
            new=[]
            for line in fp :
                line= line.strip()
                line = line.split(",")
                if(mb==int(line[3])):
                    found=True
                    #print("found")
                    line.append(str(e)) 
                    new.append(line)    
                            
            if (found):
                fp = open("package.txt","a")
                for i in new:
                    i=",".join(i)
                    i+="\n"
                    fp.write(i) 
                fp.close()
            else:
                print("Mobile number Not Found") 
               
    '''def showinventoryprice():
        try:
            inf=open("owner.txt","r")
            amt = 0
        except (FileNotFoundError):
            print("File Does not exist...!")
        else:
            try:
                for line in inf:
                    line = line.strip()
                    line = line.split(",")
                    amt+=int(line[2][8:12])
                print(str(amt),"INR")
            except:
                print("Please check database and arrange it in format")'''
            

        


#user method      
    def show_package(e):
        with open ("owner.txt","w") as fp:
            data=fp.write(str(e))
        with open ("owner.txt","r") as fp:
            data=fp.read()
            print(data)
         

    def search_user_profile(id):
        try:
            fp = open("ownerfile.txt","r")            
        except FileNotFoundError:
            print("File does not exist")
        else:  
            for line in fp:
                line=line.strip()
                line=line.split(",")
                if(id==(line[3])):
                    print(line)
                    break
            else:
                print("Name not found")
    
    
    def view_user_regimen(mb):
        try:
            fp=open("workout.txt","r")          
        except(FileNotFoundError):
            print("File does not Exit")
        else: 
            
            for line in fp:
                line=line.strip()
                line=line.split(",")
                if (int(line[3]) == int(mb)):
                    print(line)
                    
        fp.close()       
    
    
    def view_user_package(mb):
        try:
            fp=open("package.txt","r")          
        except(FileNotFoundError):
            print("File does not Exit")
        else: 
            
            for line in fp:
                line=line.strip()
                line=line.split(",")
                if (int(line[3]) == int(mb)):
                    print(line)
                    
        fp.close()   


    

















    






