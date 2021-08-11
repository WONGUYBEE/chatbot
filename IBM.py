#//////DICTIONARIES
tool_dict = {
  "show me your selection of hammers": "Hammers",
  "show me your selection of screwdrivers": "Screwdrivers",
  "show me your selection of garden tools": "Garden tools"
}

pro_hammers = {
  "Wildslinger": 123,
  "Mjolnir": 32,
  "Maximma": 4
}

pro_screwdrivers = {
  "Screwyboy112": 0,
  "More Screw Less Do": 0,
  "SCREWMAX": 0,
  "ScrewYou": 0
}

pro_gardentools = {
  "Backet": 3,
  "BallBasket": 432,
  "Gard3nToolz": 1000
}


#//////BOT
cozy_talk = {
  "hi": "Hi friend :)",
  "hello": "A pleasure! :)",
  "tell me a joke": "What's the best thing about Switzerland? Well, the flag is a big plus",
  "what is life about?": "42",
  "how much wood could a woodchuck chuck If a woodchuck could chuck wood?": "IT CANT",
  "goodbye": "Goodbye, see you soon!"
}

product_questions = {
  "is a hammer and a screwdriver the same?": "yes",
  "can i become one with the garden tools?": "it depends",
  "i am building a boat. Will i need tools for that?": "that really depends",
  "do I have to pay?": "Yes. Yes you do.",
  "do you have a payment fee?" : "Yes. Its huge"
}

weather_location = {
  "Bornholm": "sol over gudhjem, you should go",
  "Florida": "stormy sun, hard to say",
  "the moon": "really cold, stay at home"
}



new_product_questions = ["where is this?", "can i come?", "the garden, is it here?"]
shopping_cart = ["Backet", "BallBasket"]


#//////Admin
user_logins = {
  "admin": "alpine",
  "great password": "1234",
  "": ""
}
    



#//////FUNCTIONS
#///USER

def tool_menu(tool):
    print("")
    print(tool_dict[start_input] + ", perfect. Here is our selection: \n")
    anyTools = 0
    
    if tool_dict[start_input] == "Hammers":
        for key in pro_hammers:
            if pro_hammers[key] > 0:
                anyTools = anyTools+1
                print(key)
                
    if tool_dict[start_input] == "Screwdrivers":
        for key in pro_screwdrivers:
            if pro_screwdrivers[key] > 0:
                anyTools = anyTools+1
                print(key)
                
    if tool_dict[start_input] == "Garden tools":
        for key in pro_gardentools:
            if pro_gardentools[key] > 0:
                anyTools = anyTools+1
                print(key)
                

    if anyTools == 0:
        print("Sorry! There are none of these tools available")

    
#///ADMIN
def enter_product():
    print("""
          
*NEW PRODUCT*

Please select the category for the new product from the following options:
(1) Hammers
(2) Screwdriver
(3) Garden tools

write 'back' to return to menu""")

    while True:           
        product_type = input("")
        if product_type == "back":            
            return
            

        if product_type == "1" or product_type == "2" or product_type == "3":
            break
        print("Try again")
        
    new_product_name = input("Please write the name of the new the product: ")
    while True:
        new_product_stock = input("Please enter stock for the product: ")
    
        try:
            new_product_stock = int(new_product_stock)
            break
        except ValueError:
            pass
    
    if product_type == "1":
        pro_hammers[new_product_name] = new_product_stock

    if product_type == "2":
        pro_screwdrivers[new_product_name] = new_product_stock
        
    if product_type == "3":
        pro_gardentools[new_product_name] = new_product_stock
        
    print("\nProducts in category now consists of: \n")
    display_products(product_type)



def update_stock():
    see_stock()
    while True:
        while True:
             print("write 'back' to return to menu")
             product_change_stock = input("Which product has changed in stock? ")
    
             if product_change_stock == "back":
                 return
    
             number_change_stock = input("How many is in stock ")
    
             try:
                 number_change_stock = int(number_change_stock)
                 break
    
             except ValueError:
                 print("Please write a number")

        if product_change_stock in pro_hammers:
            pro_hammers[product_change_stock] = number_change_stock
            break
    
        if product_change_stock in pro_screwdrivers:
            pro_screwdrivers[product_change_stock] = number_change_stock
            break
    
        if product_change_stock in pro_gardentools:
            pro_gardentools[product_change_stock] = number_change_stock
            break   
        print("Try again")
         


def see_stock():
    print("""

*STOCK*
          
Please select the category of the product from the following options:
(1) Hammers
(2) Screwdriver
(3) Garden tools""")
    
    while True:           
        product_type = input("")
    
        if product_type == "1" or product_type == "2" or product_type == "3":
            break
        print("Try again")
        
    print("You can pick from the following products. Select using numbers indicated: \n")
    display_products(product_type)
    
    return (product_type)



def display_products(number_in):
    i = 1
    if number_in == "1":
        for key in pro_hammers:
            print ("(%s): %s" % (i, key))
            print ("stock: %s\n" % pro_hammers[key])
            i = i+1

    if number_in == "2":
        for key in pro_screwdrivers:
            print ("(%s): %s" % (i, key))
            print (key)
            print ("stock: %s\n" % pro_screwdrivers[key])
            i = i+1

    if number_in == "3":
        for key in pro_gardentools:
            print ("(%s): %s" % (i, key))
            print ("stock: %s\n" % pro_gardentools[key])    
            i = i+1
    
    
    
def see_notifications():
    print("""
          
*NOTIFICATIONS*

Write 'back' to return to menu
The bot was not able to answer the  following questions. To answer the question, please select it, and write the answer.
""")

    while True:
        if len(new_product_questions) <= 0:
            input("There are no notifications! Return by pressing enter")
            return
        i = 1
        for elements in new_product_questions:
            print("%s - %s" % (i, elements))
            i = i + 1
        
        while True:
            selected_answer = input("")
    
            if selected_answer == "back":
                return
            
            try:
                selected_answer = int(selected_answer)
                break
    
            except ValueError:
                print("Please write a number")
            
        selected_answer = int(selected_answer) - 1
        
        if selected_answer < len(new_product_questions) and selected_answer > -1:
            print("Answering the questions: " + new_product_questions[selected_answer])
            answer_question = input("Please type the answer to the question: ")
        
            product_questions[new_product_questions[selected_answer]] = answer_question
            del new_product_questions[selected_answer]
            print("\nAnswer saved!\n")



#//////CHOOSE END USER OR ADMIN
session_open = True
while session_open:
    menu = input("""
    (0) For customer
    (1) For admin """)


#//////USER MENU
    
    if menu == "0":
        print("""\n\n*****************************\n
Helo, I'm the chatbot! :) how may i assist you?\n
If in doubt of what I can help you with, please type '?'

*****************************\n""")
        
        user = True
        while user:
            start_input = input("")#.lower()

            if start_input in tool_dict:
                tool_menu(start_input)
                
            elif start_input in cozy_talk:
                print(cozy_talk[start_input])
                
            elif start_input[0:12] == "let me buy a":
                initial_sentence = start_input.split()
                buying_choice = initial_sentence[-1]
                
                if buying_choice in pro_hammers:
                    if pro_hammers[buying_choice] > 0:
                        print("%s has been added to your cart"%buying_choice)
                        shopping_cart.append(buying_choice)
                elif buying_choice in pro_screwdrivers:
                    if pro_screwdrivers[buying_choice] > 0:
                        print("%s has been added to your cart"%buying_choice)
                        shopping_cart.append(buying_choice)
                elif buying_choice in pro_gardentools:
                    if pro_gardentools[buying_choice] > 0:
                        print("%s has been added to your cart"%buying_choice)
                        shopping_cart.append(buying_choice)
                
                else:
                    print("Sorry, I could not find the desired product. It might have run out of stock")
                
            elif start_input == "show me my cart":
                print("\nContent of cart:\n")
                for elements in shopping_cart:
                    print(elements)
                    
            elif start_input == "buy whats in the cart":
                print("Packing it immediately!")
                shopping_cart.clear()
            
            elif start_input == "empty my cart":
                print("Cart has been emptied.")
                shopping_cart.clear()
            
            elif start_input == "is the weather ok?":
                location = input("It depends on where you live. Where do you live? ")
                if location in weather_location:
                    print("\nThe weather is %s!"%weather_location[location])
                        
                else:
                    print("Im sorry, I have not heard about that place and cant tell :(")
            
            
    
            elif start_input == "?":

                print ("""\n*****************************\n
I can do the following:
    
    (1) Show you the products I have
        Write “show me your selection of [ ]” with 'hammers', 'screwdrivers' or 'garden tools' to see selection of avalable goods. 

   - Let you add them to your cart
   - Buy or clear what is in the cart
   - Tell you the weather
   - Answer general questions about the products
   ..and of course we can get some cozy talk
   
My devs are notified when answers are missing, so check back with your questions, if I could not answer them initially.


Also, if youre reading this code at IBM right now, see you soon! :)
Press 6 to stop the script
Press 7 to go back into the login menu""")
                    
            elif start_input.endswith('?'):
                if start_input in product_questions:
                    print(product_questions[start_input])
                else:
                    print("\nI dont know the answer to that question yet. I'll go look it up, come back later!\n")
                    new_product_questions.append(start_input)

            elif start_input == "6":
                user = False
                session_open = False
                
            elif start_input == "7":
                user = False
                                
            else:
                print("Im sorry, didn't get that, can you rephrase or ask something else? :)")
            
            print("\n*****************************\n\nIs there anything else I can help you with? \nIf in doubt of what I can help you with, please type '?'\n\n*****************************\n")
        
    #//////ADMIN DASHBOARD
    else:
        mercy_entry = 3
        while mercy_entry:
            print("Welcome to the admin dashboard")
            username = input("Please enter username: ")
            password = input("Please enter password: ")
            
            try:
                if user_logins[username] == password: 
                    print("\nWelcome back, " + username + "!")
                    break
                
            except KeyError:
                print("ERRR, does not exist, try again")
                mercy_entry = mercy_entry - 1
            
        admin = True
        while admin:
            notifications = len(new_product_questions)
            
            print("""\n\n*****************************\n
You now have the following options:
            
(1) See system status
(2) Add a new product
(3) Update stock
(4) See stock
(5) See notifications (%d)
(6) (For debugging, stops script)
(7) (Go to login menu)
\n*****************************\n
    """%notifications)
                
            while True:            
                admin_start = input("")
                if admin_start == "1":
                    print("""
                          
*SYSTEM STATUS*

System status is stable.""")
    
                elif admin_start == "2":
                    enter_product()
    
                elif admin_start == "3":
                    update_stock()
                    
                elif admin_start == "4":
                    see_stock()
                    
                elif admin_start == "5":
                    see_notifications()
                
                elif admin_start == "7":
                    admin = False

                elif admin_start == "6":
                    admin = False
                    session_open = False
                    
                else:
                    print("Invalid input, try again")
                break