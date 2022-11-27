class Admin:
   
    def create_member(self,name,age,gender,mobile_no,email,bmi,membership_dur):
        self.name=name
        self.age=age
        self.gender=gender
        self.mobile_no=mobile_no
        self.email=email
        self.bmi=bmi
        self.membership_dur=membership_dur # membership_duration 1,3,6 month only

    def __str__(self):
        data= str(self.name)+","+str(self.age)+","+self.gender+","+str(self.mobile_no)+","+self.email+","+str(self.bmi)+","+str(self.membership_dur)
        return data

    def regimen(self,bmi,chest="CHEST",biceps="BICEPS",rest="REST",back="BACK",triceps="TRICEPS",cardio="CARDIO",legs="LEGS"):
        self.bmi=bmi
        if(self.bmi<=18.5):
            self.MON =chest
            self.Tue=biceps
            self.Wed=rest
            self.Thu=back
            self.Fri=triceps
            self.Sat=rest
            self.Sun=rest

        elif(self.bmi>18.5 and bmi<=25):
            self.MON =chest
            self.Tue=biceps
            self.Wed=cardio
            self.Thu=back
            self.Fri=triceps
            self.Sat=legs
            self.Sun=rest 

        elif(bmi>25 and bmi<=30):
            self.MON =chest
            self.Tue=biceps
            self.Wed=cardio
            self.Thu=back
            self.Fri=triceps
            self.Sat=legs
            self.Sun=cardio
        
        elif(bmi>30 and bmi<=35):
            self.MON =chest
            self.Tue=biceps
            self.Wed=cardio
            self.Thu=back
            self.Fri=triceps
            self.Sat=cardio
            self.Sun=cardio
        
    def display_regimen(self) :
            data = "Mon:"+self.MON+","+"Thu :"+self.Tue+","+"Wed :"+self.Wed+","+"Thu :"+self.Thu+","+"Fri:"+self.Fri+","+"Sat:"+self.Sat+","+"Sun:"+self.Sun
            
            return data

    def create_package(self,pk,month=1,amount=1000,m=2,a=3000,gm=3,ga=5000):
        self.pk=pk      
        if(pk=="gold"):           
            self.month=gm
            self.amount=ga
        elif(pk=="platinum"):     
            self.month=m
            self.amount=a
        elif(pk=="silver"):
            self.month=month
            self.amount=amount
        
    def show_package(self):
        data= "package:"+str(self.pk)+","+"Month:"+str(self.month)+","+"Amount:"+str(self.amount)
        return data

    
   
        

            




         
        























































'''

    def (self,name,age,gender,mobile_no,email,bmi,membership_dur):
        self.member[mobile_no]={}
        self.member[mobile_no]["name"]=name
        self.member[mobile_no]["age"]=age
        self.member[mobile_no]["gender"]=gender
        self.member[mobile_no]["mobile_no"]=mobile_no
        self.member[mobile_no]["email"]=email
        self.member[mobile_no]["bmi"]=bmi
        self.member[mobile_no]["membership_dur"]=membership_dur

    def viewmember(self):
        for i in self.member.key():
            print("full Name:",self.member[i]["name"])
            print("Age:",self.member[i]["age"])
            print("Gender:",self.member[i]["gender"])
            print("mobile_no:",self.member[i]["mobile_no"])
            print("Email:",self.member[i]["email"])
            print("BMI:",self.member[i]["bmi"])
            print("Membership_duration:",self.member[i]["membership_dur"])

'''

