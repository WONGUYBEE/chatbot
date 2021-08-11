# Welcome to the IBM Chatbot! 🚀

## Description
Hello!
Here is my IBM Case project. I chose to go with the chatbot, and it is ready to meet you. It is completely Backend with no GUI, and will run in the terminal.

## Justification of technology
I chose to use Python as the simplicity of the language made it possible for me to write code the fast, and implement as much as possible. Furthermore it is the language I am most familiar with.

## How to run
To get up and running simple clone this repository. 

```
git clone https://github.com/WONGUYBEE/chatbot.git
```

And they type 
```
python chatbot/IBM.py
```

Now you are up and running!


# Commands
NB: All commands are hardcoded and should be run exactly as seen below.

## Commands for navigation between user and admin side
When opening the chatbot initially, the user gets to choose to be the user or the admin.
It is possible to change between the two by writing ‘7’ in their respective main menu. This is important as changes on one side is reflected on the other.

*To login on the admin side, use the following credentials:*
- Username: admin
- Password: alpine<br/> Alternatively, leave login empty, that works as well :)

## Commands when on the admin side:


1. **See the system status** : This will tell if the system is running correctly

2. **Add a new product to a category** : Enter a new product and its stockage, to add it to the selection

3. **Update stock of product** : Change the stock of an existing product

4. **See the current stock of products** : See the current stock of each product

5. **See notifications** : Notifications notifies when questions have been asked, which the bot could not answer. The admin can write an answer to the question. The answer will be displayed if a user asks the question again.

*( ! ) it is possible to write ‘back’ in each submenu, to get back to the main menu*

## Commands when on the user side:

1. **"?"** : An explanation of what the bot is able to help with

2. **“show me your selection of [ ]”** : input ‘hammers’, ‘screwdrivers’ or ‘garden tools to display the current selection

3. **“hi”, “tell me a joke”, “goodbye”** : General conversation with the bot, see more in *'cozy talk commands'* below

4. **"do you have a payment fee?", "is a hammer and a screwdriver the same?**  : General questions for the bot to answer,

5. **“let me buy a [ ]”** : input ex. ‘Mjolnir’, ‘Backet’, ‘SCREWMAX’ to add the item to your cart. The item has to be in stock. Items in stock can be seen using (2)
	
6. **“show me my cart” / “buy whats in the cart” / “empty my cart”** : Manipulation of the cart. It is possible to show the content, buy it or clear the cart.

7. **“is the weather okay?”** : Tells how the weather is. Locations the bot understands are ‘Bornholm’, ‘Florida’ and ‘the moon’

8. **“[any question not in the database]?”** : When writing any other question with a ‘?’ behind it, the question is saved, and the admin can write an answer to it afterwards. This answer will be used when the question is asked again






 ### List of inputs for cozy talk and product questions. Add more by asking questions and answering on the admin side.
**Cozy talk**
- hi
- tell me a joke
- what is life about?
- how much wood could a woodchuck chuck If a woodchuck could chuck wood?
- hello
- goodbye

**Product questions**
- is a hammer and a screwdriver the same?
- can i become one with the garden tools?
- i am building a boat. Will i need tools for that?
- do I have to pay?
- do you have a payment fee?
