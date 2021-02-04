"""
Program Info Comment
Date: 02/04/21
Program Name: bulls_cows.py
Description: Given a 4-digit code, ask the user to take the first turn and
enter a guess. The program will then print out both the code and the guess.
In addition, the bull count and cow count will be displayed for the turn.
"""


#-------------------------------------------------------------------------------------
# Functions
#-------------------------------------------------------------------------------------
# DEFINITION gameCodeString( code ) :

#      GAME MODE: (code printed),
#      print a line of dashes.
#-------------------------------------------------------------------------------------
def gameCodeString ( code ) :

    dashes = dashLine()
    
    stars = starLine()
    
    print()

    print( stars )

    print( '%12s' % 'GAME CODE:' , code )

    print( dashes )
    




#-------------------------------------------------------------------------------------
# DEFINITION enterGuessString( guess ) :
# DESCRIPTION: Will print the string 'Enter Guess: ' in proper alignment,
# then pull the guess from the getInput function.
# PRE: will pull in guess and dashLine.
# POST: Enter Guess: ( guess printed ),
#       print a line of dashes.
#-------------------------------------------------------------------------------------
def enterGuessString( guess ) :

    dashes = dashLine()

    print( '%12s' % 'Enter Guess:' , guess )

    print( dashes )





#-------------------------------------------------------------------------------------
# DEFINITION codeBullsAndCowsHeaderString( code ) :
# DESCRIPTION: Will print the string 'CODE: ' in proper alignment, then pull
# the code from the getInput function followed by the string 'BULLS COWS'.
# PRE: will pull in code.
# POST: CODE: ( code printed ) BULLS COWS
#-------------------------------------------------------------------------------------
def codeBullsAndCowsHeaderString( code ) :

    print( '%31s' % 'BULLS   COWS' )





#-------------------------------------------------------------------------------------
# DEFINITION guessBullsAndCowsOutputString( guess, bullCount, cowCount ) :
# DESCRIPTION: Will print the string Enter Guess: in proper alignment,
# then pull the guess from the getInput function. Finally printing a star line
# underneath the string.
# PRE: will pull in guess, bullCount, cowCount, and starLine
# POST: Guess: ( print guess ) ( print bullCount ) ( print cowCount ),
#       print a line of stars
#-------------------------------------------------------------------------------------
def guessBullsAndCowsOutputString( guess , bullCount , cowCount ) :

    stars = starLine()

    print( '%12s' % 'Guess:' , guess , '%4s' % bullCount , '%6s' % cowCount )

    print( stars )





#-------------------------------------------------------------------------------------
# DEFINITION starLine() :
# DESCRIPTION: This function will print a line of 35 stars (*) when used
# with the print function
# PRE: set the variable stars as 35 stars
# POST: ***********************************
#-------------------------------------------------------------------------------------
def starLine() :

    stars = ( '*' * 35 )

    return stars





#-------------------------------------------------------------------------------------
# DEFINITION dashLine() :
# DESCRIPTION: This function will print a line of 35 dashes (-) when used
# with the print function
# PRE: set the variable dashes as 35 dashes
# POST: -----------------------------------
#-------------------------------------------------------------------------------------
def dashLine() :

    dashes = ( '-' *35 )

    return dashes





#-------------------------------------------------------------------------------------
# DEFINITION exitGame( guess ) :
# DESCRIPTION: This function will allow user to exit the program by entering X or x
# PRE: will pull in guess
# POST: ( if x is entered ) Goodbye
#-------------------------------------------------------------------------------------
def exitGame( guess ) :
    
    while guess == 'X' or guess == 'x'  :

        print()

        print( 'Goodbye' )

        exit( 'Goodbye' ) 





#-------------------------------------------------------------------------------------
# DEFINITION generateCode() :
# DESCRIPTION: This function will create a random 4-digit code.
# first randint will import from the random library, then code will be initialized
# to 0. A random int in the range of 1000 - 9999 will be created and assigned
# to code. Then code will go through a while loop to assure no digits are the same
# helping create a code with 4 unique digits. If there is a duplicate number
# the function will print 'Bad GAME CODE: ' then print the code.
# If the code passes the loop then the function will turn code into a string
# and return code.
# PRE: Will import randint from random, initialize code to 0, then pull a random
# number
# POST: Will store the code as a string.
#-------------------------------------------------------------------------------------
def generateCode() :

    from random import randint

    code = 0

    code = randint ( 999 , 9999 )

    code0 = int( code // 1000 )

    code1 = int( ( code // 100) % 10 )

    code2 = int( ( code // 10 ) % 10 )

    code3 = int( code % 10 )

    while ( code0 == code1 or code0 == code2 or code0 == code3 or code1
           == code2 or code1 == code3 or code2 == code3 ) :

        print( 'Bad GAME CODE:', code ) 
        
        code = randint( 999 , 9999 )

        code0 = int( code // 1000 )

        code1 = int( ( code // 100) % 10 )

        code2 = int( ( code // 10 ) % 10 )

        code3 = int( code % 10 )    

    else:

        code = str( code )
    
    return code





#-------------------------------------------------------------------------------------
# DEFINITION getInput() :
# DESCRIPTION: This function will first initialize guess to 0 then print asking
# the user to 'Enter 4 digit Guess: '. Then will take that input run it through
# a while loop. The loop will make sure it is exactly 4 digits long, contains no
# letters, and will make sure there are no duplicate numbers.
# otherwise if the loop fails will print 'INVALID guess must be 4 unique
# digits  Enter Guess: '. If the input passes then the function
# will return the guess.
# PRE: Will initialize guess to 0, ask for user input
# POST: Will store the guess as a string
#-------------------------------------------------------------------------------------
def getInput() :

    guess = 0
                
    guess = input( 'Enter 4 digit Guess or X to exit: ' )

    goodBye = exitGame( guess )
    
    while ( len(guess) != 4 or guess[0] == guess[1] or  guess[0] == guess[2] or  guess[0] == guess[3] or
            guess[1] == guess[2] or guess[1] == guess[3] or guess[2] == guess[3] or
            guess.isalpha() ) : #NEED TO FIX INPUT!!!!

        goodBye = exitGame( guess )

        guess = input( 'INVALID guess must be 4 unique digits \n\n\nEnter Guess or X to exit: ' )
#PLAY WITH ERROR MESSAGE!!
    return guess 





#-------------------------------------------------------------------------------------
# DEFINITION checkBulls( code, guess )
# DESCRIPTION: This function will initialize bullCount to 0. Then pull the code and guess
# from the generateCode and the getInput functions and run it through an if
# statement. The if statement will check to see if any of the guess numbers
# align with the code. For each digit that aligns, +1 will be added to the
# bull count.
# PRE: will pull in code, and guess. Will initialize bullCount to 0
# POST: Will store bullCount
#-------------------------------------------------------------------------------------
def checkBulls( code , guess ) :

    bullCount = 0

    if code[0] == guess[0] :
        
        bullCount = bullCount + 1

    if code[1] == guess[1] :

        bullCount = bullCount + 1

    if code[2] == guess[2] :

        bullCount = bullCount + 1

    if code[3] == guess[3] :

        bullCount = bullCount + 1

    return bullCount





#-------------------------------------------------------------------------------------
# DEFINITION checkCows( code, guess ) :
# DESCRIPTION: This function will initialize cowCount to 0. Then pull the code and guess
# from the generateCode and the getInput functions and run it through a series
# of it statements. The if statements will check to see if any of the guess
# numbers match any of the code numbers that are not in the index. For each
# digit that matches, +1 will be added to the cow count.
# PRE: will pull in code, and guess. Will initialize cowCount to 0
# POST: Will store cowCount
#-------------------------------------------------------------------------------------
def checkCows( code , guess ) :

    cowCount = 0

    
    if code[0] == guess[1] or code[0] == guess[2] or code[0] == guess[3] :
        
        cowCount =  cowCount + 1

    if code[1] == guess[0] or code[1] == guess[2] or code[1] == guess[3] : 

        cowCount =  cowCount + 1

    if code[2] == guess[0] or code[2] == guess[1] or code[2] == guess[3] :

        cowCount =  cowCount + 1

    if code[3] == guess[0] or code[3] == guess[1] or code[3] == guess[2] :

        cowCount =  cowCount + 1
        
    return cowCount





#-------------------------------------------------------------------------------------
# DEFINITION gameLoop( guess , bullCount , cowCount , code ) :
# DESCRIPTION: Will pull from functions guess, bullCount, cowCount, code, gameCode, userGuess,
# codeBullCow, and guessBullsCowsOutput. Running a loop until the user correctly guesses the
# GAME CODE, also keeping track of the number of times the loop runs for the turnCount.
# Once the user wins, the loop will print 'Congratulations  you won in: ( number of turns ) turns!'
# PRE: pull in guess, bullCount, cowCount, code, gameCode, userGuess, codeBullCow,
# and guessBullsCowsOutput.
# POST:Blank line,
#      Enter 4 digit Guess or X to exit:
#      Blank line
#      print a line of stars
#      GAME MODE: (code printed),
#      print a line of dashes.
#      Enter Guess: ( guess printed ),
#      print a line of dashes.
#      CODE: ( code printed ) BULLS COWS
#      Guess: ( print guess ) ( print bullCount ) ( print cowCount ),
#      print a line of stars
#      Congratulations  you won in: ( turnCount printed ) turns!
#-------------------------------------------------------------------------------------
def gameLoop( guess , bullCount , cowCount , code ) :

    turnCount = 1

    while bullCount != 4 : 

        turnCount += 1

        print()

        guess = getInput()

        bullCount = checkBulls( code , guess )

        cowCount = checkCows( code , guess )

        gameCode = gameCodeString( code )
    
        userGuess = enterGuessString( guess )
    
        codeBullCow = codeBullsAndCowsHeaderString( code )

        guessBullsCowsOutput = guessBullsAndCowsOutputString( guess , bullCount , cowCount )

    else :

        print( ' Congratulations  you won in: ' , turnCount , ' turns!')
#-------------------------------------------------------------------------------------
# DEFINITION OF THE MAIN PROGRAM - 
#-------------------------------------------------------------------------------------
def main():

#-------------------------------------------------------------------------------------
# This will play one full turn of bulls_cows by calling functions.
# The output will create the gameboard.
# first will call generateCode, getInput, checkBulls, and checkCows. Next it
# will call and print the gameCodeString. Next it will call and print the
# enterGuessString. Finally, it will call and print the
# codeBullsAndCowsHeaderString, and guessBullsAndCowsOutputString.
#-------------------------------------------------------------------------------------
# Output - Results to the user in the console
#-------------------------------------------------------------------------------------
# Calling functions
#-------------------------------------------------------------------------------------
# To generate random code.
#-------------------------------------------------------------------------------------
    code = generateCode()
    
#-------------------------------------------------------------------------------------
# To retrieve user input.
#-------------------------------------------------------------------------------------
    guess = getInput()

#-------------------------------------------------------------------------------------
# To check for Bull count.
#-------------------------------------------------------------------------------------
    bullCount = checkBulls( code , guess )
    
#-------------------------------------------------------------------------------------
# To check for Cow count.
#-------------------------------------------------------------------------------------
    cowCount = checkCows( code , guess )
   
#-------------------------------------------------------------------------------------
# Calling Function to print the Game Code string.
#-------------------------------------------------------------------------------------
    gameCodeString( code )
    
#-------------------------------------------------------------------------------------
# Calling function to print the Enter Guess string.
#-------------------------------------------------------------------------------------
    enterGuessString( guess )
    
#-------------------------------------------------------------------------------------    
# Calling function to print 'Code' then 'Bulls Cows'.
#------------------------------------------------------------------------------------
    codeBullCow = codeBullsAndCowsHeaderString( code )

#-------------------------------------------------------------------------------------
# Calling function to print 'Guess' then user input, bull number, cow number.
#-------------------------------------------------------------------------------------
    guessBullsCowsOutput = guessBullsAndCowsOutputString( guess , bullCount , cowCount )

#-------------------------------------------------------------------------------------
# Calling function to run the Game loop until user wins or exits.
#-------------------------------------------------------------------------------------
    gamePlay = gameLoop( guess , bullCount , cowCount , code )

main()


   





#-------------------------------------------------------------------------------------
# Test Cases
#-------------------------------------------------------------------------------------
"""
Test Run #1

Enter 4 digit Guess or X to exit: 1234

***********************************
  GAME CODE: 4123
-----------------------------------
Enter Guess: 1234
-----------------------------------
      CODE:  4123 BULLS   COWS
     Guess:  1234    0      4
***********************************

Enter 4 digit Guess or X to exit: ad
INVALID guess must be 4 unique digits 


Enter Guess or X to exit: 4123

***********************************
  GAME CODE: 4123
-----------------------------------
Enter Guess: 4123
-----------------------------------
      CODE:  4123 BULLS   COWS
     Guess:  4123    4      0
***********************************
 Congratulations  you won in:  2  turns!

 
-------------------------------


Test Run #2

Enter 4 digit Guess or X to exit: 1234

***********************************
  GAME CODE: 4690
-----------------------------------
Enter Guess: 1234
-----------------------------------
      CODE:  4690 BULLS   COWS
     Guess:  1234    0      1
***********************************

Enter 4 digit Guess or X to exit: X

Goodbye


-------------------------------


Test Run #3


Enter 4 digit Guess or X to exit: 111
INVALID guess must be 4 unique digits 


Enter Guess or X to exit: 12
INVALID guess must be 4 unique digits 


Enter Guess or X to exit: 2222
INVALID guess must be 4 unique digits 


Enter Guess or X to exit: 1234

***********************************
  GAME CODE: 3904
-----------------------------------
Enter Guess: 1234
-----------------------------------
      CODE:  3904 BULLS   COWS
     Guess:  1234    1      1
***********************************

Enter 4 digit Guess or X to exit: 3901

***********************************
  GAME CODE: 3904
-----------------------------------
Enter Guess: 3901
-----------------------------------
      CODE:  3904 BULLS   COWS
     Guess:  3901    3      0
***********************************

Enter 4 digit Guess or X to exit: 3940

***********************************
  GAME CODE: 3904
-----------------------------------
Enter Guess: 3940
-----------------------------------
      CODE:  3904 BULLS   COWS
     Guess:  3940    2      2
***********************************

Enter 4 digit Guess or X to exit: 3904

***********************************
  GAME CODE: 3904
-----------------------------------
Enter Guess: 3904
-----------------------------------
      CODE:  3904 BULLS   COWS
     Guess:  3904    4      0
***********************************
 Congratulations  you won in:  4  turns!
"""

