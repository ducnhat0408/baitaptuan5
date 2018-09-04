from controller_cnsql import ConnectSQL as cn 
import time
class User:
    def __init__(self):
        self.id = 1
        self.username = ""
        self.password = ""
        self.fullname = ""
        self.city = ""
        self.birthday = 1
        self.flag = None
    
    ''    
    def SignUp(self):
        print("*******>>>nhap thong tin dang ki<<******")
        print("username:")
        username = input()
        print("password:")
        password = input()
        print("fullname:")
        fullname = input()
        print("city:")
        city =  input()
        print("birthday")
        birthday = input()
        print(username)
        print(password)
        print(fullname)
        print(city)
        print(birthday)
        conOb = cn()
        conOb.Open()
        with cn.con:
            
            conOb.SignUp(username, password, fullname, birthday, city)
    ''
           
    #===================================================================================
    ''
    #dang nhap
    def SignIn(self):
        print("Nhap vao username: \n")
        username = input()
        print("Nhap vao password: \n")
        password = input()
        conOb = cn()
        conOb.Open()
        with cn.con:
            if conOb.CheckSignIn(username,password) > 0:
                print ("Dang nhap thanh cong!\n")
                self.id = conOb.CheckSignIn(username, password)
                self.flag = 1
            else:
                print ("Dang nhap that bai!\n")
                self.flag = 0
    ''
    
     #===================================================================================
    ''
    #dang suat
    def SignOut(self):
        self.flag = 0
        print ("Ban da dang xuat!\n")
    ''
        
     #===================================================================================
    ''
    #kiem tra dang nhap
    def isSignIn(self):
        """"""
        if self.flag == 1:
            return 1
        return 0
    ''
    
     #===================================================================================
    ''
    #hien thi ban be
    def ShowFriend(self,id):
        if self.isSignIn():
            conOb = cn()
            conOb.Open()
            conOb.Showfriend(self.id)
        else:
            print("*****>>>Ban chua dang nhap<<<*****\n")
    ''
            
    #===================================================================================
    ''
    #gui tin nhan
    def SenMess(self,id):
        if self.isSignIn():
            conOb = cn()
            conOb.Open()
            #conOb.Showfriend(self.id)
        print("Chon nguoi dung: \n")
        name = input()
        id2 = conOb.TranNameToId(name)
        dt = time.ctime()
        #print(dt)
        if id2 > 0:
            print("To  :  ",name)
            print("soan tin nhan:\n")
            mess = input()
            with cn.con:
                if conOb.Checkfriend(self.id, id2) != 0:
                    conOb.WriteToMess(self.id,id2,mess,dt)
    ''        
    
    def Showmesdrec(self, id):
        if self.isSignIn():
            conOb = cn()
            conOb.Open()
            print('danh sach friend: \n')
            conOb.Showfriend(self.id)
            print("nhap ten ban muon ...:\n")
            frien = input()
            id2 = conOb.TranNameToId(frien)
            print(id2,self.id)
            conOb.ShowMessRec(id2, self.id)
            with cn.con:
                conOb.Statusmes(id2, self.id)
            
    #===================================================================================
    
    def Showmessen(self, id):
        if self.isSignIn():
            conOb = cn()
            conOb.Open()
            print('danh sach friend: \n')
            conOb.Showfriend(self.id)
            print("nhap ten ban muon ...:\n")
            frien = input()
            id2 = conOb.TranNameToId(frien)
            conOb.ShowMessSen(self.id, id2)
            
    #==================================================================================
    ''
    #them ban be
    def AddFriend(self,id):
        if self.isSignIn() == 1:
            print(self.id)
            print("Nhap ten ban muon them: ")
            name = input()
            conOb = cn()
            conOb.Open()
            id2 = conOb.TranNameToId(name)
            #print(id2)
            if id2 > 0:
                if conOb.Checkfriend(self.id,id2) != 0:
                    with cn.con:
                        conOb.WriteToFriend(self.id, id2)  
                        #conOb.Showfriend(self.id)
                else:
                    print(">>>Ban da bi nguoi nay chan hoac ban nhap ten cua minh<<<\n\n")
            else:
                print("*******>>>Tai khoan khong ton tai<<<***********\n")
        else:
            print("*****>>>Ban chua dang nhap<<<*****\n")
    ''   
    
    #===============================================================================
     
        