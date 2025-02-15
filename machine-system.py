#for stopping program execution for some time
import time

print("Please insert your card password: ")

#for card processing
time.sleep(5)

password = 000
print("==============================")

#taking atm pin from user
pin = int(input("  Enter your ATM pin: "))

#user account balance
balance = 10000

#checking pin is valid or not 
if pin == password:
    #loop will run user get free 
    while True:

        #Showing  info to user

        print(""" 
            1 === your balance
            2 === withdraw balance
            3 === deposit balance
            4 === exit 
            """
              )        
        print("==============================")


        try:    
             #taking an option from user
            option = int(input("Please enter your choice: "))
        except:
            print("Please enter valid option: ")
        
        #for option 1        
        if option == 1:
            print("Your current balance is 10000")
          
          #for option 2                  
        if option == 2:

            withdraw_amount = int(input("Please enter withdraw_amount: "))
            

            balance = balance - withdraw_amount

            print(f"{withdraw_amount} is debited from your account")

            

            print(f"Your updated balance is {balance}")

         #for option 3   
        if option == 3:

            deposit_amount = int(input("Please enter deposit_amount: "))

            balance = balance + deposit_amount

            

            print(f"{deposit_amount} is credited to your account")



            print(f"Your updated balance is {balance}")


         #for option 4
        if option == 4:
           
           print("==============================")
         
           print("Thank you have a nice day!")
           
           break
       
else:
    print("AYUSIN MO TANGA TANGA")