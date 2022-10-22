# users (either customers or admin) BL Class
from collections import UserList
import msvcrt
import os.path
from urllib.parse import uses_params
from muser import MUser
import csv
from csv import writer
import pandas as pd

class MUserDL:

    # all users accounts list ( customer + admin )
    userList = []

    # adding user (either customer or admin) into list
    @staticmethod
    def addUserIntoList(user):
        MUserDL.userList.append(user)

    # storing user (either admin or customer) into file
    @staticmethod
    def SignIn(user):
        for storedUser in MUserDL.userList:
            if(storedUser.UserName == user.UserName and storedUser.UserPassword == user.UserPassword):
                return storedUser
        return None
    
    # checking if user is already exists
    @staticmethod
    def checkIfUserAlreadyExists(verifyUser):
        for user in MUserDL.userList:
            if(user.UserEmail == verifyUser.UserEmail):
                return None
        return verifyUser

    # searching user from list
    @staticmethod
    def searchUserFromList(user):
        for storedUser in MUserDL.userList:
            if(storedUser.userMobile == user.userMobile):
                return storedUser
        return None

    # searching user for deposit money
    @staticmethod
    def searchUserForDepositMoney(user):
        for storedUser in MUserDL.userList:
            if(storedUser.userMobile == user.depositerNo):
                return storedUser
        return None

    # updating user account after editing
    @staticmethod
    def updateListAfterEditingUser(editedUser, editUser, path):
        count = 0

        # Replacing User Details with new details provided
        editUser.userName = editedUser.userName
        editUser.userMobile = editedUser.userMobile
        editUser.userPassword = editedUser.userPassword
        editUser.userMoney = editedUser.userMoney
        editUser.userRole = editedUser.userRole

        # Updating record in the file after editing User Details 
        updateFile = open (path, 'w')
        for user in MUserDL.userList:
            if(count == 0):
                updateFile.write(user.userName + "," + user.userMobile + "," + user.userPassword +","+ str(user.userMoney) +"," + user.userRole)
            else:
                updateFile.write("\n" + user.userName + "," + user.userMobile + "," + user.userPassword +","+ str(user.userMoney) +"," + user.userRole)
            count += 1
        updateFile.close()

    # depositing money into user account
    @staticmethod
    def addMoneyIntoUserAccount(user, amountToDeposit, path):
        count = 0
        userTotalMoney = int(user.userMoney)
        userTotalMoney = userTotalMoney + amountToDeposit
        user.userMoney = str(userTotalMoney)
        updateFile = open (path, 'w')
        for user in MUserDL.userList:
            if(count == 0):
                updateFile.write(user.userName + "," + user.userMobile + "," + user.userPassword +","+ str(user.userMoney) +"," + user.userRole)
            else:
                updateFile.write("\n" + user.userName + "," + user.userMobile + "," + user.userPassword +","+ str(user.userMoney) +"," + user.userRole)
            count += 1
        updateFile.close()

    # updating user accounts from file after exchange of money (transaction)
    @staticmethod
    def updateAccountAfterTransaction(sender, sendMoneyDetails, path):
        if(sendMoneyDetails != None):
            count = 0
            # performing operation for transfering money
            # sender info
            senderTotalMoney = int(sender.userMoney)
            senderTotalMoney = senderTotalMoney - sendMoneyDetails.moneySended
            sender.userMoney = str(senderTotalMoney)
            # searching receiver info
            for receiver in MUserDL.userList:
                if(receiver.userMobile == sendMoneyDetails.receiverNo):
                    receiverTotalMoney = int(receiver.userMoney)
                    receiverTotalMoney = receiverTotalMoney + sendMoneyDetails.moneySended
                    receiver.userMoney = str(receiverTotalMoney)
            # updating user data in the  file after transfering money
            updateFile = open (path, 'w')
            for user in MUserDL.userList:
                if(count == 0):
                    updateFile.write(user.userName + "," + user.userMobile + "," + user.userPassword +","+ str(user.userMoney) +"," + user.userRole)
                else:
                    updateFile.write("\n" + user.userName + "," + user.userMobile + "," + user.userPassword +","+ str(user.userMoney) +"," + user.userRole)
                count += 1
            updateFile.close()
            print("\t Transaction Happened Successfully!")
            msvcrt.getch()
        else:
            print("\t The transaction is not happened as there is nothing in the object")
            msvcrt.getch()

    # updating user accounts from file after paying bills
    @staticmethod
    def updateAccountAfterBill(payer, payBillsDetails, path):
        if(payBillsDetails != None):
            count = 0
            # performing operation for transfering money
            # payer info
            payerTotalMoney = int(payer.userMoney)
            payerTotalMoney = payerTotalMoney - payBillsDetails.billAmount
            payer.userMoney = str(payerTotalMoney)

            # updating user data in the  file after transfering money
            updateFile = open (path, 'w')
            for user in MUserDL.userList:
                if(count == 0):
                    updateFile.write(user.userName + "," + user.userMobile + "," + user.userPassword +","+ str(user.userMoney) +"," +user.userRole)
                else:
                    updateFile.write("\n" + user.userName + "," + user.userMobile + "," + user.userPassword +","+ str(user.userMoney) +"," + user.userRole)
                count += 1
            updateFile.close()
            print("\t Bill Paid Successfully!")
            msvcrt.getch()
        else:
            print("\t The pay bill operation is not happened as there is nothing in the object")
            msvcrt.getch()

    # updating users accounts from file after buying mobile load
    @staticmethod
    def updateAccountAfterMbLoad(buyer, MobileLoadInfo, path):
        if(MobileLoadInfo != None):
            count = 0
            # performing operation for transfering money
            # buyer info
            buyerTotalMoney = int(buyer.userMoney)
            buyerTotalMoney = buyerTotalMoney - MobileLoadInfo.loadAmount
            buyer.userMoney = str(buyerTotalMoney)

            # updating user data in the  file after buying load
            updateFile = open (path, 'w')
            for user in MUserDL.userList:
                if(count == 0):
                    updateFile.write(user.userName + "," + user.userMobile + "," + user.userPassword +","+ str(user.userMoney) +"," +user.userRole)
                else:
                    updateFile.write("\n" + user.userName + "," + user.userMobile + "," + user.userPassword +","+ str(user.userMoney) +"," + user.userRole)
                count += 1
            updateFile.close()
            print("\t Mobile Load bought Successfully!")
            msvcrt.getch()
        else:
            print("\t The Mobile load operation is not happened as there is nothing in the object")
            msvcrt.getch()

    # updating users accounts from file after buying mobile bundles
    @staticmethod
    def updateAccountAfterBoughtBundle(user, boughtBundleInfo, path):
        if(boughtBundleInfo != None):
            count = 0
            # performing operation for transfering money
            # buyer info
            buyerTotalMoney = int(user.userMoney)

            buyerTotalMoney = buyerTotalMoney - int(boughtBundleInfo.bBundlePrice)
            user.userMoney = str(buyerTotalMoney)

            # updating user data in the  file after buying load
            updateFile = open (path, 'w')
            for user in MUserDL.userList:
                if(count == 0):
                    updateFile.write(user.userName + "," + user.userMobile + "," + user.userPassword +","+ str(user.userMoney) +"," +user.userRole)
                else:
                    updateFile.write("\n" + user.userName + "," + user.userMobile + "," + user.userPassword +","+ str(user.userMoney) +"," + user.userRole)
                count += 1
            updateFile.close()
            print("\t Mobile Bundle Bought bought Successfully!")
            msvcrt.getch()
        else:
            print("\t The Mobile bundle operation is not happened as there is nothing in the object")
            msvcrt.getch()
    
    # reading users data from file
    @staticmethod
    def readDataFromFile(path):
        if(os.path.exists(path)):
            path = "users.csv"
            with open(path , 'r') as csvfile:
                # create the object of csv.reader()
                df = pd.read_csv(csvfile,delimiter=',')
            for row in csv_file_reader:
                UserEmail, UserName, UserPassword, userRole = MUserDL.perseData(row)
                user = MUser(UserEmail, UserName, UserPassword, userRole)
                MUserDL.addUserIntoList(user)
            return True
        else:
            return False
    
    # parsing users data
    @staticmethod
    def perseData(line):
        line = line.split(",")
        return line[0], line[1], line[2], line[3], line[4]

    # storing users data into file after registration
    @staticmethod
    def storedUserIntoFile(user):
        path = 'users.csv'
        with open(path,'a',encoding="utf-8",newline="") as fileInput:
            writer = csv.writer(fileInput)
            writer.writerow([user.UserEmail,user.UserName, user.UserPassword, user.UserRole])
            fileInput.close()