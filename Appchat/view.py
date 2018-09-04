from controller_user import User
def main():
    us = User()
    while True:
        print(  "1. Dang ky!\n"
                "2. Dang nhap!\n"
                "3. Hien thi ban be!\n"
                "4.Hien thi tin nhan da gui!\n"
                "5.Gui tin nhan\n"
                "6.Them ban be\n"
                "7.Hien thi tin nhan da nhan!\n"
                "8.Dang xuat\n"
                "****************************\n"
                "****************************\n")
        print("Nhap vao lua chon: \n")
        choose = int(input())
        if choose == 1:
            us.SignUp()
        if choose == 2:
            us.SignIn()
        if choose == 3:
            us.ShowFriend(id) 
        if choose == 4:
            us.Showmessen(id)
        if choose == 5:
            us.SenMess(id)
        if choose == 6:
            us.AddFriend(id)
        if choose == 7:
            us.Showmesdrec(id)  
        if choose == 8:
            us.SignOut()
            
        
if __name__ == '__main__':
    main()