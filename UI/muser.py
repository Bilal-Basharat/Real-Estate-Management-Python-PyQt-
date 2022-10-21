# users (either customer or admin ) BL Class
from operator import truediv


class MUser:
    userName = ""
  
    userPassword = ""
    UserEmail =""   
    def __init__(self, userName, userMobile, userPassword, UserEmail):
        self.userName = userName
      
        self.userPassword = userPassword
       
        self.UserEmail = UserEmail
    
    def isAdmin(self):
        if(self.userRole == "Admin"):
            return True
        else:
            return False
        
