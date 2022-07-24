def odd_or_even():
    # 🚨 Don't change the code below 👇
    number = int(input("Which number do you want to check? "))
    # 🚨 Don't change the code above 👆

    # Write your code below this line 👇
    if number % 2 == 0:
        print("This is an even number.")
    else:
        print("This is an odd number.")


def bmi_classifier():
    # 🚨 Don't change the code below 👇
    height = float(input("enter your height in m: "))
    weight = float(input("enter your weight in kg: "))
    # 🚨 Don't change the code above 👆

    # Write your code below this line 👇
    bmi = weight/height**2
    if bmi <= 18.5:
        print(f"Your BMI is {round(bmi)}, you are underweight.")
    elif bmi <= 25:
        print(f"Your BMI is {round(bmi)}, you have a normal weight.")
    elif bmi <= 30:
        print(f"Your BMI is {round(bmi)}, you are slightly overweight.")
    elif bmi <= 35:
        print(f"Your BMI is {round(bmi)}, you are obese.")
    else:
        print(f"Your BMI is {round(bmi)}, you are clinically obese.")


def leap_year():
    # 🚨 Don't change the code below 👇
    year = int(input("Which year do you want to check? "))
    # 🚨 Don't change the code above 👆

    # Write your code below this line 👇
    if (year % 4 == 0):
        if(year % 100 != 0):
            print("Leap year.")
        elif (year % 100 == 0 & year % 400 == 0):
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Not leap year.")


def pizza_calculator():
    # 🚨 Don't change the code below 👇
    print("Welcome to Python Pizza Deliveries!")
    size = input("What size pizza do you want? S, M, or L ")
    add_pepperoni = input("Do you want pepperoni? Y or N ")
    extra_cheese = input("Do you want extra cheese? Y or N ")
    # 🚨 Don't change the code above 👆

    # Write your code below this line 👇
    bill = 0
    if (size == "S"):
        bill += 15
    elif (size == "M"):
        bill += 20
    elif (size == "L"):
        bill += 25
    if (add_pepperoni == "Y"):
        if (size == "S"):
            bill += 2
        else:
            bill += 3
    if (extra_cheese == "Y"):
        bill += 1
    print(f"Your final bill is: ${bill}.")


def love_calculator():
    # 🚨 Don't change the code below 👇
    print("Welcome to the Love Calculator!")
    name1 = input("What is your name? \n")
    name2 = input("What is their name? \n")
    # 🚨 Don't change the code above 👆

    # Write your code below this line 👇
    name1, name2 = name1.lower(), name2.lower()
    dec = name1.count("t") + name1.count("r") + name1.count("u") + name1.count(
        "e") + name2.count("t") + name2.count("r") + name2.count("u") + name2.count("e")
    uni = name1.count("l") + name1.count("o") + name1.count("v") + name1.count(
        "e") + name2.count("l") + name2.count("o") + name2.count("v") + name2.count("e")
    score = int(f"{dec}{uni}")
    if (score < 10 | score > 90):
        print(f"Your score is {score}, you go together like coke and mentos.")
    elif (score < 50 | score > 40):
        print(f"Your score is {score}, you are alright together.")
    else:
        print(f"Your score is {score}.")


def main():
    print('''
    
                   ____                  
                _.' :  `._               
            .-.'`.  ;   .'`.-.           
   __      / : ___\ ;  /___ ; \      __  
 ,'_ ""--.:__;".-.";: :".-.":__;.--"" _`,
 :' `.t""--.. '<@.`;_  ',@>` ..--""j.' `;
      `:-.._J '-.-'L__ `-- ' L_..-;'     
        "-.__ ;  .-"  "-.  : __.-"       
            L ' /.------.\ ' J           
             "-.   "--"   .-"            
            __.l"-:_JL_;-";.__           
         .-j/'.;  ;""""  / .'\"-.        
       .' /:`. "-.:     .-" .';  `.      
    .-"  / ;  "-. "-..-" .-"  :    "-.   
 .+"-.  : :      "-.__.-"      ;-._   \  
 ; \  `.; ;                    : : "+. ; 
 :  ;   ; ;                    : ;  : \: 
 ;  :   ; :                    ;:   ;  : 
: \  ;  :  ;                  : ;  /  :: 
;  ; :   ; :                  ;   :   ;: 
:  :  ;  :  ;                : :  ;  : ; 
;\    :   ; :                ; ;     ; ; 
: `."-;   :  ;              :  ;    /  ; 
 ;    -:   ; :              ;  : .-"   : 
 :\     \  :  ;            : \.-"      : 
  ;`.    \  ; :            ;.'_..--  / ; 
  :  "-.  "-:  ;          :/."      .'  :
   \         \ :          ;/  __        :
    \       .-`.\        /t-""  ":-+.   :
     `.  .-"    `l    __/ /`. :  ; ; \  ;
       \   .-" .-"-.-"  .' .'j \  /   ;/ 
        \ / .-"   /.     .'.' ;_:'    ;  
         :-""-.`./-.'     /    `.___.'   
               \ `t  ._  /            
                "-.t-._:'                
    ''')
    print("Welcome to Treasure Island.")
    print("Your mission is to find the treasure.")
    choice_1 = input("Do you want to go left or right?").lower()
    if choice_1 == "left":
        choice_2 = input("Do you want to swim or wait?").lower()
        if choice_2 == "wait":
            choice_3 = input(
                "You found 3 doors (Red, Blue and Yellow). Which one do you choose?").lower()
            if choice_3 == "red":
                print("Burned by the fire, you die.\nGame Over.")
            elif choice_3 == "blue":
                print("Eaten by beasts, you are dead.\nGames Over.")
            elif choice_3 == "yellow":
                print("You found the treasure!")
            else:
                print("Game Over.")
        else:
            print("Attacked by trout.\nGame Over.")
    else:
        print("Fall into a home.\nGame Over.")


main()
