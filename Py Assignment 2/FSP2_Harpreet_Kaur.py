import random
import os

#funtion to print game instructions and category hint
def game_start(max_chances,word_len):
    word_len = 1
    print "Welcome to Hangman."
    print "You have 9 chances to guess the mystery word."
    print "You are only allowed to enter a letter, one at at time."
    print
    print "Category:",topic

#function to get letter from user
def get_letter():
    print
    letter = str(raw_input("Guess a letter in the mystery word:"))
    letter = letter.strip() # removes whitespaces
    letter = letter.lower() # changes uppercase letters to lowercase
    print
    return letter

#funtion to check if user wins or loses, after check ends the game
def end_game():
    if incorrect_guess == max_chances:
        print
        print "You Lose!"
        print "The word was",word
        print "Thank you for playing"
    if correct_guess == word_len:
        print
        print "You Win!"
        print "Thank you for playing"
        
#funtion to print graphics
def display_graphics(incorrect_guess):
    hangman = [
    """
         +--------+
         |
         |
         |
         |
         |
     ====================
    """,
    """
        +--------+
        |        o
        |
        |
        |
        |
    ====================
    """,
    """
        +--------+
        |        o
        |      --+
        |
        |
        |
    ======================
    """,
    """
        +--------+
        |        o
        |      --+--
        |       
        |    
        |  
    =====================
    """,
    """
        +--------+  
        |        o
        |      --+--
        |        |
        |       
        |       
        |
    =====================
    """,
    """
        +--------+
        |        o
        |      --+--
        |        |
        |        |  
        |        
        |           
    =====================
    """,
      """
        +--------+
        |        o
        |      --+--
        |        |
        |        | 
        |       /
        |            
    =====================
    """,
      """
        +--------+
        |        o
        |      --+--
        |        |
        |        |
        |       / \
        |        
    =====================
    """,
      """
        +--------+
        |        o
        |      --+--
        |        |
        |        |
        |       / \
        |      / 
    =====================
    """,
      """
        +--------+
        |        o
        |      --+--
        |        |
        |        |
        |       / \
        |      /   \ 
    =====================
    """
,]
 
    print hangman[incorrect_guess]
    return
      

myDict = {"Animals":["donkey","horse","snake","cat","monkey"],
          "Sports":["soccer","basketball","volleyball", "tennis","gymnastics"],
          "Cities":["singapore","london","paris","rome","boston"],
          "Countries":["malaysia","indonesia","india","germany","spain"]} 


topic = random.choice(myDict.keys()) #random topic
word = random.choice(myDict[topic])  #random word from topic


word_len = len(word)     #counts len in word 
guess = word_len * [' _ '] #replaces word with underscore(_)

max_chances = 9     #number of chances 

used = ""           #used letters 
correct_guess = 0   #correct letter guessed
incorrect_guess = 0 #incorrect letter guessed


game_start(max_chances,word_len)

while (incorrect_guess != max_chances) and (correct_guess != word_len):
    letter = get_letter()
    
    #checks if user input letter consists of alphabetic characters only
    if len(letter)== 1 and letter.isalpha(): 
        
        if used.find(letter) != -1:
            print "You already picked the letter",letter
            print
        else:
            used = used + letter
            first_index = word.find(letter)
            
            #checks if letter is in word
            if  first_index == -1:
                incorrect_guess = incorrect_guess + 1 
                print "The Letter",letter,"is not in the mystery word." 
                #calls function and prints out hangman when word is guessed incorrectly
                display_graphics(incorrect_guess) 
                print
            else:
                print"The Letter",letter,"is in the mystery word."
                print
                for i in range(word_len):
                    if letter == word[i]:
                       guess[i] = letter
                       correct_guess = correct_guess + 1

    else:
        print "Please guess a single letter in the alphabet."
        print

    #prints used letters from previous guesses
    print ''.join(guess)
    print
    print "Letters you have tried so far: ", used
    
    end_game()


