
user_input = input("Hello, What is your name?: ")
print ("Hi" , user_input.upper())

def countdown(n):
    while n > 0:
        print(n)
        n -=1
    print("Blastoff")
        
while True:
    
    game = input("Would you like to play a game?: ")
    
    if game == 'y':
        
        print("Great!, Let's start the game")
        print("Try guessing a number so that you are not blasted off!!!")
        
        input1 = int(input("Pick a number between 0 and 50: "))

        if (input1) <= 40 and input1 >= 0:
            countdown(input1)
            print("You loose!,you were blasted off!")
            
        elif input1 >= 40 and input1 <= 50:
            print("You were not blasted off, you've won!")
            
        elif input1 > 50 or input1 < 0:
            print("Your number is out of range!")

        elif input1 == str:
            print("Please type an integer")
            
        input2 = input('Would you like to play again? y/n: ')
        if input2 == 'y':
            continue
        else:
            break
          
    elif game == 'n':
        print("Okay, bye" ,  user_input.lower())
        break        
    else:
        print("invalid input. please type y/n ")

while True:
    print("type homework if you want assistance or type QUIT to quit")
    
    input3 = str(input("Would you like assistance with algebra homework or Do you want to quit: "))
        
    if input3 == 'homework':
        print('l can help you with addition, multiplication, subtraction , division ', user_input.upper())
            
        
        inputw = str(input("type addition or, subtraction , or multiplication ,or division: "))
        if inputw == 'addition':
             

             num1 = int(input("What is the first number?: "))
             num2 = int(input("What is the second number?: "))
             final_answer = num1 + num2
             print("The answer is {}".format(final_answer))

        elif inputw == 'subtraction':
              num1 = int(input("What is the first number?: "))
              num2 = int(input("What is the second number?: "))
              final_answer = num1 - num2
              print("The answer is {}".format(final_answer))
              
        elif inputw == 'multiplication':
              num1 = int(input("What is the first number?: "))
              num2 = int(input("What is the second number?: "))
              final_answer = num1 * num2
              print("The answer is {}".format(final_answer))
              
        elif inputw == 'division':
              num1 = int(input("What is the first number?: "))
              num2 = int(input("What is the second number?: "))
              final_answer = num1 / num2
              print("The answer is {}".format(final_answer))

        elif inputw != 'division' or 'addition' or 'subtraction' or 'multiplication':
              print("That's a wrong response!")                    

                     
        
        
        
    elif input3 == 'QUIT':
        print ("Goodbye" , user_input.upper(), "see you next time!")
        break
    else:
        print("Please type homework or QUIT")
        
       
                            
 
                   
    
                   



        
    

        
   
        
 
        


       



