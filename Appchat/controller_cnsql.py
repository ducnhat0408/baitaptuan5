import sqlite3
import sys
import os
import time

class ConnectSQL:
    path = os.path.dirname(__file__) + "\\db.db"
    con = sqlite3.connect(path)    
    cur = con.cursor()
   
    ''
    #mo co so du lieu
    def  Open(self):
        ConnectSQL.path = os.path.dirname(__file__) + "\\db.db"
        ConnectSQL.con = sqlite3.connect(ConnectSQL.path)   
        ConnectSQL.cur = self.con.cursor()
        print("thanh cong!")
    ''
        
    #=========================================================================
    ''    
    #dang ki
    def SignUp(self,username, password, fullname, birthday, city):
        cur = ConnectSQL.con.cursor() 
        cur.execute("INSERT INTO user (username, password,fullname,birthday,city) values (?,?,?,?,?)", (username, password, fullname, birthday, city)) 
        print ("thanh cong\n")
    ''
        
    #=========================================================================
    ''
    #kiem tra dang nhap
    def CheckSignIn(self,user, passw):
        sql = "SELECT * FROM  user WHERE username = ? and password = ?"
        self.cur.execute(sql,(user,passw))
        row = self.cur.fetchone()
        if row == None :
            return -1
        return row[0]
    ''
    
    #=========================================================================
    ''
    #hien thi ban be
    def Showfriend(self,id):
        print ("************List Friends***********\n")
        print(id)
        sql = "SELECT DISTINCT user.username FROM (SELECT * FROM Friend where (id1 = ? OR id2 = ?) AND isblock = 0 )  as A LEFT JOIN user ON  (A.id2 = user.id)"
        self.cur.execute(sql,(id,id))
        row = self.cur.fetchone()
        while row != None:
            print (row[0])
            row= self.cur.fetchone()
    ''
            
    #=========================================================================
    ''
    #tim id theo ten
    def TranNameToId(self,frien):
        sql = "SELECT id FROM user WHERE username = ?"
        self.cur.execute(sql,(frien,))
        row = self.cur.fetchone()  
        if row == None:
            return -1
        return row[0]
    ''
    
    #=========================================================================
    '''
    #select tin nhan tu csdl
    def SelectMessenger(self, id):
        sql = "SELECT DISTINCT user.username FROM"
        "(SELECT * FROM messenger where (idsen = ? or idrec = ?) ) as A LEFT JOIN user ON (A.idrec = user.id OR A.idsen = user.id)"
        self.cur.execute(sql,(id))
        row = self.cur.fetchone()
        while row!= None:
            print (row[2])
            row= self.cur.fetchone()
    '''
        
    #=========================================================================    
    ''
    #hien thi tin nhan
    def ShowMessSen(self,id1,id2):
        sql = "SELECT * FROM (SELECT * FROM messenger WHERE (idsen = ? AND idrec = ?)  ) AS B LEFT JOIN  user ON (user.id = B.idrec )"
        self.cur.execute(sql,(id1,id2))
        row = self.cur.fetchone()
        while row!= None:
            print (row[6])
            print ("      ",row[2])
            print ("               ",row[3])
            status = row[4] 
            if status == 1:
                print("*************da xem************")
            if status == 0:
                print("*************chua doc**********")
            row= self.cur.fetchone()
    ''       
    #=========================================================================
    ''
    #hien thi chi tiet tin nhan
    def ShowMessRec(self,id1,id2):
        sql = "SELECT * FROM (SELECT * FROM messenger WHERE (idsen = ? AND idrec = ?)  ) AS B LEFT JOIN  user ON (user.id = B.idsen )"
        self.cur.execute(sql,(id1,id2))
        row = self.cur.fetchone()
        drec = ""
        while row!= None:
            print (row[6])
            print ("      ",row[2])
            print ("               ",row[3])
            status = row[4] 
            if status == 1:
                print("*************da xem************")
            row = self.cur.fetchone()
    ''   
    #=========================================================================
    ''
    #insert tin nhan
    def WriteToMess(self,id,id2,mess,dt):
        print(id,id2,mess,dt)
        sql = "INSERT INTO messenger (idsen, idrec, contend, time, sent) VALUES (?,?,?,?,0)"
        self.cur.execute(sql, (id,id2,mess,dt))
        print("Da gui\n")
    ''
          
    #=========================================================================
    #kiem tra block
    def CheckBlock(self,id1,id2):
        isblock = 0
        sql = "SELECT isblock FROM Friend WHERE (id1 = ? AND id2 = ?)"
        self.cur.execute(sql, (id1,id2))
        row = self.cur.fetchone()
        isblock = row[0]
        return isblock
    ''
        
    #=========================================================================

    ''
    #kiem tra ban be
    def Checkfriend(self, id, id2):  
        
        sql = "SELECT * FROM Friend WHERE  id1 = ? and id2 = ?"
        self.cur.execute(sql, (id,id2))
        row = self.cur.fetchone()
        if row == None:
            return 1
        return 0
    ''    
    
    #=========================================================================
    ''
    #insert ban be vao co so du lieu
    def WriteToFriend(self,id,id2):
        print(id, id2)   
        Sql = "INSERT INTO Friend (id1,id2,isblock) VALUES (?,?,0)"
        self.cur.execute(Sql,(id,id2))
        drec = "Thanh cong"
        return drec
    ''
    
    #========================================================================
    ''
    def Statusmes(self,id,id2):
        print(id,id2)
        sql = "UPDATE messenger SET sent = 1 WHERE (idsen = ? and idrec = ?)"
        self.cur.execute(sql,(id,id2))
        drec = "da xem"
        return drec
    ''
    ''
    #=========================================================================