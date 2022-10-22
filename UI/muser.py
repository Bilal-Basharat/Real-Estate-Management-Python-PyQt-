# users (either customer or admin ) BL Class
from operator import truediv


class MUser:
    UserEmail =""
    UserName = ""
    UserPassword = ""
    UserRole = ""
    def __init__(self, UserEmail, UserName, UserPassword, UserRole):
        self.UserEmail = UserEmail
        self.UserName = UserName
        self.UserPassword = UserPassword
        self.UserRole = UserRole
    
    def isAdmin(self):
        if(self.userRole == "Admin"):
            return True
        else:
            return False
        
