#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import numpy as np
import random

class BoardBreakerException(Exception):
    """
    exceptions relating to The Scoreboard Broke
    """
    pass

class ComputerPlayException(Exception):
    """
    exceptions relating to computer attempting to place symbols on the board
    """
    pass

class CompsciPowerException(Exception):
    """
    exceptions relating to compsci power levels
    """
    pass

class CoffeeException(Exception):
    """
    exceptions relating to the presence of coffee
    """
    pass


class Player:
    name = ""
    symbol = 0
    score = -1 

    
    def __init__(self):
        """
        this will change later - if we have a login and it recognizes the name then
        it should set the score according to the database or wherever the score is stored
        for now it's not doing anything
        """
        self.score = 0
        
        
    def __repr__(self):
        return "Player Name: {}\nSymbol: {}\nScore: {}".format(self.name, self.symbol, self.score)
        
        
    def promptName(self):
        """
        prompts user for string input for playername
        returns true if mysterious conditions are met :>
        returns false otherwise
        does not throw an exception itself because it is handled elsewhere
        (because it's funnier that way)
        """
        self.name = input("Input your name :>  ")
        return (self.name.lower() == "asad") or (self.name.lower() == "umberto")
    
    
    def promptSymbol(self):
        """
        prompts user for string input whether they would play as cross or circle
        repeats itself until either cross or circle is input
        """
        check = input("Would you like to play as cross or circle? ==>  ")
        if check.lower() == "cross" or check.lower() == "x":
            self.symbol = -1
        elif check.lower() == "circle" or check.lower() == "o":
            self.symbol = 1
        else:
            print("Not a valid input! Please try again:")
            self.promptSymbol()
        
        
    def setName(self, nameput):
        """
        method for forcing player name
        """
        self.name = nameput
    
    
    def setSymbol(self, choose):
        """
        method for forcing player symbol
        this sets directly to symbol, so it should always be -1 or 1, not "cross" or "circle"
        """
        self.symbol = choose
        
    
    def confirmPlay(self):
        """
        prints name and symbol
        does not return anything
        different from playerCheck because it doesn't print score
        """
        if self.symbol < 0:
            sym = "Cross"
        elif self.symbol > 0:
            sym = "Circle"
        else:
            sym = "Neither symbol has been selected."
        print("-----\nPlayer Name: {}\nSymbol: {}\n-----".format(self.name, sym))
        
    
    def playerCheck(self):
        if self.symbol < 0:
            sym = "Cross"
        elif self.symbol > 0:
            sym = "Circle"
        print("Player Name: {}\nSymbol: {}\nScore: {}".format(self.name, sym, self.score))


class comPlayer:
    """
    a modified class for playing against a computer
    not a subclass of player because there are like 90% methods that i do not want computer to inherit
    level (1, 2, 3) is the difficulty level
    """
    name = "the computer"
    level = -1
    symbol = 0
    
    
    def __init__(self, play1):
        """
        when you create the computer you don't actually need to know what level it is yet
        however, passing it an opponent will let it know how to set its symbol
        """
        if play1.symbol > 0:
            self.symbol = -1
        else: self.symbol = 1
        
    
    def setName(self):
        self.name = input("Aww, you want to nickname the computer? Sure! ==>  ")
        
        
    def setSymbol(self, play1):
        """
        sets the computer's symbol based on its opponent
        """
        if play1.symbol > 0:
            self.symbol = -1
        else: self.symbol = 1
        
    
    def setLevel(self, typ):
        """
        sets level to arg
        must be 1, 2, or 3
        does absolutely no error checking, this is a backend method only and i don't want to write custom error methods for
            things that aren't objectively fun
        for user input see changeDifficulty
        """
        level = typ
    
    
    def changeDifficulty(self):
        """
        prompts user to choose computer difficulty
        internally represented as 1, 2, or 3
        accepts either that or string inputs
        calls itself again if input is invalid
        does not return anything
        """
        lev = input("Select a difficulty: Novice, Intermediate, or Difficult."
                    +"\nYou can type either the difficulty names or 1, 2, or 3 to choose. ==>  ")
        if lev.lower() == "novice" or (lev.isdigit() and int(lev) == 1):
            self.level = 1
        elif lev.lower() == "intermediate" or (lev.isdigit() and int(lev) == 2):
            self.level = 2
        elif lev.lower() == "difficult" or (lev.isdigit() and int(lev) == 3):
            self.level = 3
        else:
            print("That isn't a valid input! Please try again:")
            self.changeDifficulty()
            
            
    def printDifficulty(self):
        """
        prints out what difficulty name and level the computer is currently set to
        does not return anything
        """
        typ = ""
        if self.level == 1:
            typ = "novice"
        elif self.level == 2:
            typ = "intermediate"
        elif self.level == 3:
            typ = "difficult"
        print("The computer is set to level {}, {}.".format(self.level, typ))
    
    
    def computerPlay(self, board, turn):
        """
        single function that returns the appropriate play level based on difficulty
        """
        if self.level == 1:
            return self.novicePlay(board, turn)
        elif self.level == 2:
            return self.intermediatePlay(board, turn)
        elif self.level == 3:
            return self.difficultPlay(board, turn)
        else:
            print("The computer doesn't seem to have a level set.")
            raise ComputerPlayException(
                "The computer attempted to select a difficulty function without having an appropriate level set."
            )
    
    
    def novicePlay(self, board, turn):
        """
        returns a list length 2 with row, column ints for its next move
        turn is the board's turncounter - how many turns have passed since the beginning of the game
        
        board should be the numpy array, not the actual board object
        
        the computer looks at the board and randomly picks an empty space, with chance being one out of how many empty tiles
        theoretically, this can take a really long time 
        assumes the board is exactly 9 squares
        i'm sure there's a way to look at board and calculate its dimensions but i don't know how to do that rn
        i'm also sure there's a better way to iterate through an array when you specifically want its indices but idk that too
        """
        ans = []
        chance = 1/(9 - turn)
        while len(ans) < 2:
            for x in range(0,3):
                for y in range(0,3):
                    if board[x,y] == 0:
                        if (random.random() < chance):
                            ans.append(x)
                            ans.append(y)
                            return ans
    
    
    def intermediatePlay(self, board, turn):
        """
        responds as novice half the time and difficult half the time
        calls other functions depending on random outcome, which means it should also output the same thing:
            a list length 2 with row, column ints for its next move
        
        must be passed turn count because it needs to be able to pass that to the difficult method if it decides that
        """
        if random.random() > 0.5:
            print("The computer is thinking like a beginner...")
            return self.novicePlay(board, turn)
        else: 
            print("The computer is thinking a little harder...")
            return self.difficultPlay(board, turn)
    
    
    def difficultPlay(self, board, turn):
        """
        responds intelligently
        returns a tuple with row, column ints for its next move
        turn is the board's turncounter - how many turns have passed since the beginning of the game
        
        i'm having too much fun to look up how to win in tictactoe but if i was doing this for a grade i would do that
        this algorithm is based on my experience as a small child with those restaurant kids menus activity booklets
        
        """
        if turn == 0:
            return (1,1)
            ## always go in the middle if computer goes first
        elif turn == 1 and board[1,1] == self.symbol * -1:
            truth = True
            for x in range(0,3):
                for y in range(0,3):
                    if board[x,y] == self.symbol:
                        truth = False
            if truth:
                return (0,2) 
            ## if this is the first turn and you didn't go first and there's something in the middle, then go in the top right
            
        else:
            ## run modified version of checkwin algorithm
            selfwin = self.findWin(board, self.symbol * 2)
            if len(selfwin) >= 1:
                return selfwin[0]
                ## if it sees one away from wins and it's your symbol, win 
            else:
                defender = self.findWin(board, self.symbol * -2)
                if len(defender) >= 1:
                    return defender[0]
                    ## if it sees one away from wins and that's opponent symbol, defend
        
        
        ## the computer should pin when possible
        if turn == 2 and board[1,1] == self.symbol:
            for acro in range (0,2):
                if board[acro, acro+1] == self.symbol * -1:
                    return (0,2)
                if board[acro+1, acro] == self.symbol * -1:
                    return (2,0)
            ## on the second turn, if computer is centered and computer sees opponent in horizontals,
            ## proceed to pin
        
        if turn == 4 and board[1,1] == self.symbol:
            if board[0,2] == self.symbol and board[2,0] == self.symbol * -1:
                return (1,2)
            elif board[2,0] == self.symbol and board[0,2] == self.symbol * -1:
                return (1,0)
            ## on the fourth turn, if the computer is centered and computer sees its own position in previous pin output,
            ## and if opponent has filled the last diagonal in the pin output,
            ## complete the pin
        
        if board[1,1] == 0:
            return (1,1)
            ## if by now the middle is empty go in the middle
        
        return self.novicePlay(board, turn)
            ## otherwise go randomly idk
        
    
    
    def findWin(self, board, con):
        """
        runs checkWin on the passed np array board but checks con instead of 3/-3 by default
            (raises an exception if there is no winning move in the board passed to it)
        con must be -2 or 2
            con should not be -1 or 1
        returns a list of tuples - length 2 tuples of indices row,col where there are winning moves for con
        if the list is empty, there are no winning moves for con
        """
        if not isinstance(con, int): raise ComputerPlayException(
            "The computer was passed an incorrect argument for checking winnable states before making its move."
        )
        else:
            ans = []
            rowsum = board.sum(axis = 1)
            colsum = board.sum(axis = 0)

            diag1 = board.diagonal().sum()
            diag2 = np.fliplr(board).diagonal().sum()

            if con in rowsum:                
                for x in range(0,3):
                    temp = self.zeroFinder(board[x])
                    if temp > 0 and rowsum[x] == con:
                        ans.append((x,temp))
            ## if you find a winnable row,
            ## iterate through the rows of the board,
            ## and if one of the rows of the board has exactly one zero and the same index in rowsum == con,
            ## add the resulting tuple to answer list

            if con in colsum:
                for y in range(0,3):
                    tymp = self.zeroFinder(board[:,y])
                    if tymp > 0 and colsum[y] == con:
                        ans.append((tymp, y))
            ## above algorithm flipped for columns

            if con == diag1:
                for z in range(0,3):
                    if board[z,z] == 0:
                        ans.append((z,z))

            if con == diag2:
                for a in range(0,3):
                    imp = abs(a-2)
                    if board[a,imp] == 0:
                        ans.append((a,imp))

        return list(dict.fromkeys(ans))
        ## deduplicates
        ## thank you w3schools
    
    
    def zeroFinder(self, sliced):
        """
        function that takes a single-dimensional list/array and returns the index of a single zero 
        if there is more than one zero, the function returns -1
        """
        ans = []
        for count, item in enumerate(sliced):
            if item == 0:
                ans.append(count)
        if len(ans) == 1:
            return ans[0]
        else:
            return -1


class Scoreboard:
    """
    this object represents the tic tac toe board used to play one game
    
    -- playerstate is whether this board is being used for a PvP game (true) or a PvE game (false)
    -- turnstate tracks whose turn it is (-1 for cross, 1 for circle) 
        -- turnstate is 0 by default so you know if something went wrong LOL it should always be set correctly by other methods
    -- turncounter tracks how many turns have occurred during this board's game
        -- turncounter is -1 by default so you know, again, if something went wrong
        -- (it should never go wrong because it's being set to 0 in the constructor but you never know)
        -- turncounter should only ever be between 0 and 9 (inclusive)
    -- board (the variable) is a 3x3 numpy array tracking who moved where
    """
    playerstate = False
    turnstate = 0
    turncounter = -1
    board = np.array([[0,0,0],[0,0,0],[0,0,0]])
    
    
    def __init__(self, playerstate):
        """
        half of its variables shouldn't be initialized -- do not initialize turnstate, do not mess with board
        playerstate should be known & set when the board is constructed
        """
        self.score = 0
        self.playerstate = playerstate
        self.turncounter = 0
    
    def stateString(self):
        """
        returns cross or circle depending on the board's current turnstate
        """
        if self.turnstate == -1:
            return "cross"
        elif self.turnstate == 1:
            return "circle"
        else:
            raise BoardBreakerException(
                "The board attempted to check its state string while the turnstate was neither 1 nor -1."
            )
    
    
    def printTurn(self, play1, play2):
        """
        prints out whose turn it is based on player args & the board's own turnstate
        depending on the playerstate, play2 may be a compPlayer 
        (needs player args so it knows the player names & symbols)
        """
        if (self.turnstate == play1.symbol):
            print("It is {}'s turn next.".format(play1.name))
        elif (self.playerstate and self.turnstate == play2.symbol):
            print("It is {}'s turn next.".format(play2.name))
        elif (not self.playerstate):
            print("It is the computer's turn next.")
        else:
            print("It doesn't seem to be anyone's turn!!")
        
        
    def setTurn(self, marker, play1, play2):
        """
        sets the board's turnstate to the according marker
        requires players as args so it can print out whose turn it is after the turn is set
        """
        self.turnstate = marker
        self.printTurn(play1, play2)
        
        
    def swapTurn(self):
        """
        changes turnstate between 1 and -1
        i'm sure there's a more elegant way to do this but i don't know it 
        """
        if self.turnstate == -1:
            self.turnstate = 1
        elif self.turnstate == 1:
            self.turnstate = -1
    
    
    def printBoard(self):
        """
        prints out information about the board
        i can't get __repr__ to work tbh that's why this is here
        prints whose turn it is and draws the current board state
        """
        self.printTurn()
        print("Score: {}".format(self.score))
        self.drawBoard()
        
        
    def drawBoard(self):
        """
        prints out a visual representation of the board numpy array according to how the game is going
        also prints out what turn number it is above the board
        """
        typesetter = []
        for sym in self.board.flat:
            if sym == -1:
                typesetter.append("x")
            elif sym == 1:
                typesetter.append("o")
            else:
                typesetter.append(" ")
        
        if self.turncounter >= 10:
            print("Last turn:")
        else:
            print("Turn {}:".format(self.turncounter))
            
        print(" {} | {} | {}".format(typesetter[0], typesetter[1], typesetter[2]))
        print("------------")
        print(" {} | {} | {}".format(typesetter[3], typesetter[4], typesetter[5]))
        print("------------")
        print(" {} | {} | {}\n".format(typesetter[6], typesetter[7], typesetter[8]))
        
    
    def placeParam(self, row = True):
        """
        method that prompts user for an input row or column and scolds them if they don't input correctly
        optional parameter boolean row is true if meant for a row and false if meant for a column
        returns int (user input row/column)
        """
        if row:
            placetype = "row"
        else: placetype = "column"
        
        place = input("What {} do you want to place at? ==>".format(placetype))

        while( (not(place.isdigit()) or (((place.isdigit()) and int(place) > 3) or (place.isdigit()) and int(place) < 0 ))):
        ## will cry if place is not a number,
        ## or if place is a number and it is greater than 3,
        ## or if place is a number and it is less than 0.
        ## i really really really don't want it to throw exceptions LOL i want you to be able to keep playing if you mistype!!
        ## so this is only being typecast if i am sure it is a number. that is why the statement is how it is.

            print("That isn't a valid input!\nPlease choose a {} from 1 to 3 to make your move.".format(placetype))
            place = input("What {} do you want to place at? ==> ".format(placetype))
            
        return int(place)
    
        
    def boardUpdate(self):
        """
        this is called when a player places a symbol
        updates board matrix based on a user given row and column input
        draws the board when the symbol is correctly placed
        calls itself again if the symbol is not correctly placed
        
        note: this method asks for the visual row & column, not for the python indices, so -1 these during matrix operations
        the board's turnstate decides which symbol it's going to place
            if it is -1, place cross
            if it is 1, place circle
        """
        
        row = self.placeParam(True)
        column = self.placeParam(False)
            
        print("Placing {} at row {}, column {}.".format(self.stateString(), row, column))
        
        if self.board[row-1, column-1] == 0:
            self.board[row-1, column-1] = self.turnstate
            self.turncounter += 1
            self.drawBoard()
        else:
            print("... Except something's there already! Please try again:")
            self.boardUpdate()
    
    
    def compBoardPlace(self, spots):
        """
        method for placing indices given by the computer decision methods
        the spots arg should always be a list (maybe a tuple?) of two ints & the inputs should be possible
        the indices given should be the python ones, not the visual ones
        """
        #### a little error catching as a treat
        ## looping instead of checking each item to scale better later
        ####
        if len(spots) != 2:
            print("Something has gone horribly wrong... Send help...")
            raise ComputerPlayException(
                "The computer passed a list to scoreboard with the incorrect number of arguments."
            )
        
        #### ok coding time
        row = spots[0]
        col = spots[1]
            
        print("Placing {} at row {}, column {}.".format(self.stateString(), row+1, col+1))
            
        if self.board[row, col] == 0:
            self.board[row, col] = self.turnstate
            self.turncounter += 1
            self.drawBoard()
        else:
            print("... Except something's there already! Something has gone horribly wrong, again!!")
            raise ComputerPlayException(
                "The computer attempted to place a symbol where one already exists."
            )
       
                  

    def checkWin(self):
        """
        returns 1 or -1 based on who won
        if no one won, winstate remains 0
        """
        winstate = 0
        
        rowsum = self.board.sum(axis = 1)
        colsum = self.board.sum(axis = 0)
        
        diag1 = self.board.diagonal().sum()
        diag2 = np.fliplr(self.board).diagonal().sum()
    
        if -3 in rowsum or -3 in colsum:
            winstate = -1
        elif diag1 == -3 or diag2 == -3:
            winstate = -1
        
        elif 3 in rowsum or 3 in colsum:
            winstate = 1
        elif diag1 == 3 or diag2 == 3:
            winstate = 1            
        
        return winstate


class Menu:
    """
    oversees general game functions
    creates & manages players and scoreboards as necessary
    tracks scores within an overall game session
    saves & loads player data from json files
    """
    
    def __init__(self):
        print("Welcome to a new round of tic-tac-toe!")
    

    def nameExceptionHandler(self, check):
        """
        makes sure a string (pass a player name) does not meet certain exceptional criteria
        raises errors if they do
        does not return anything otherwise
        """
        check = check.lower()
        if check == "asad":
            print("I sense your true power and fold immediately. You win!")
            raise CompsciPowerException(
                "The game has ended due to overwhelming power!"
            )
        elif check == "umberto":
            coffee = input("Hey, have you had coffee yet?  ")
            if (coffee.lower() == "yes" or coffee.lower() == "true"):
                print("Beautiful!!\nOkay, let's keep going.")
            else:
                print("That wasn't a yes! What are you doing trying to play tictactoe without coffee?!")
                raise CoffeeException(
                    "It's time for a coffee break!!"
                )
    
    
    ### game type select should go here eventually
    

## playing game!!

## ask for: player 1 name & symbol
    ## if name is asad: you win :>
## ask for: playing against another player? or computer?
    ## if player: ask for player 2 name
## confirm opponent symbol

## initialize scoreboard with playerstate (2p or pve)
## rand who goes first
    ## random: <0.5 is -1 (cross) first
    ## >0.5 is 1 (circle) first
## save that int as turnstate

#### while turncounter is <= 9:
## ask that player to place symbol (ask for row and column)
## board update returns true if input worked and false if it failed
    ## need a way to make sure board update worked exactly once
## check win: returns true if someone won based on that symbol, and false if not
## if not checkwin: change turn
## if checkwin: increment score and print a winning message


def checkName(name1, name2):
    return name1.lower() == name2.lower()

def gameTypeSelect():
    """
    asks for user input for whether they want to play vs a person (return true) or vs computer (returns false)
    case insensitive but not whitespace tolerant
    returns boolean because it's intended to be used with scoreboard's playerstate variable
    returns None if input isn't recognized
    """
    gametype = input("Do you want to play against another person, or against the computer?"
             +"\nInput Player or Computer to choose. ==>  ")
    if gametype.lower() == "player":
        return True
    elif gametype.lower() == "computer":
        return False
    else:
        print("That isn't a valid input! Please try again:")
        return None



#### GAME STARTUP
menu = Menu()


#### create player 1
player1 = Player()
if player1.promptName():
    menu.nameExceptionHandler(player1.name)
player1.promptSymbol()
player1.confirmPlay()

## SELECT GAME TYPE
state = gameTypeSelect()
while state == None:
    state = gameTypeSelect()

#### IF PVP: CREATE PLAYER 2
if state:
    player2 = Player()
    print("-----\nHello, player 2!")
    if player2.promptName():
        menu.nameExceptionHandler(player2.name)
    
    while checkName(player2.name, player1.name):
        print("These names are the same! Please enter another name:")
        if player2.promptName():
            menu.nameExceptionHandler(player2.name)
    
    if player1.symbol > 0:
        player2.setSymbol(-1)
    if player1.symbol < 0:
        player2.setSymbol(1)
    player2.confirmPlay()

#### ELSE: CREATE COMPUTER OPPONENT        
else:
    ## this should be the computer opponent
    computer = comPlayer(player1)
    computer.changeDifficulty()
    computer.printDifficulty()

playboard = Scoreboard(state)


#### PLAYING THE GAME - TWO HUMAN PLAYERS
if state:
    ## random decides who goes first
    if random.random() > 0.5:
        playboard.setTurn(1, player1, player2)
    else:
        playboard.setTurn(-1, player1, player2)

    ## draw the board for the first time
    playboard.drawBoard()


    ## main gameplay loop
    while playboard.turncounter <= 9:
        playboard.boardUpdate()

        ####
        ## if checkwin determines someone won,
        ## update the turncounter so no more turns can occur & we know the game has ended
        ## check who actually won (which player)
        ## print out a win message
        ## if neither player has a symbol that matches the turncounter, print out something else lol.
        ####
        if playboard.checkWin() != 0:
            playboard.turncounter = 10
            if playboard.turnstate == -1: 
                if player1.symbol == playboard.turnstate:
                    print("YIPPEE! {} won!".format(player1.name))
            elif player2.symbol == playboard.turnstate:
                print("YIPPEE! {} won!".format(player2.name))
            else:
                print("Okay, idk how you did it but you sort of broke something and I don't know who won.")

        ####
        ## if the turn counter is 9,
        ## no one won and there have been 9 valid moves
        ## (we know no one won because if someone won the turncounter has been set to 10)
        ## print out a message indicating a draw,
        ## and set the turncounter to 10 so we know the game has ended
        ####
        if playboard.turncounter == 9:
                print("Neither of you won?! Come on! It's easy, right?!")
                playboard.turncounter = 10

        ####
        ## if the turn counter is not 10,
        ## no one has won and there are still valid moves to be made
        ## (we know the board is not full because it would have been stopped just above if it had)
        ## change whose turn it is, and print a message indicating that
        #### 
        elif playboard.turncounter != 10:
            playboard.swapTurn()
            playboard.printTurn(player1, player2)

    print("The game has ended. Thanks for playing!")


#### PLAYING AGAINST THE COMPUTER
if not state:
    if random.random() > 0.5:
        playboard.setTurn(1, player1, computer)
        computerEven = computer.symbol == 1
    else:
        playboard.setTurn(-1, player1, computer)
        computerEven = computer.symbol == -1
    
    playboard.drawBoard()
    
    ## main gameplay loop
    while playboard.turncounter <= 9:
        if computerEven and playboard.turncounter % 2 == 0:
            playboard.compBoardPlace(computer.computerPlay(playboard.board, playboard.turncounter))
        elif not computerEven and playboard.turncounter % 2 == 0:
            playboard.boardUpdate()
        elif computerEven and playboard.turncounter % 2 == 1:
            playboard.boardUpdate()
        elif not computerEven and playboard.turncounter % 2 == 1:
            playboard.compBoardPlace(computer.computerPlay(playboard.board, playboard.turncounter))
        

        ####
        ## if checkwin determines someone won,
        ## update the turncounter so no more turns can occur & we know the game has ended
        ## check who actually won (which player)
        ## print out a win message
        ## if neither player has a symbol that matches the turncounter, print out something else lol.
        ####
        if playboard.checkWin() != 0:
            playboard.turncounter = 10
            if player1.symbol == playboard.turnstate:
                    print("YIPPEE! {} won!".format(player1.name))
            elif computer.symbol == playboard.turnstate:
                print("You, uh, you lost to the computer!")
            else:
                print("Okay, idk how you did it but you sort of broke something and I don't know who won.")

        ####
        ## if the turn counter is 9,
        ## no one won and there have been 9 valid moves
        ## (we know no one won because if someone won the turncounter has been set to 10)
        ## print out a message indicating a draw,
        ## and set the turncounter to 10 so we know the game has ended
        ####
        if playboard.turncounter == 9:
                print("You didn't win against the computer?! Come on! It's easy, right?!")
                playboard.turncounter = 10

        ####
        ## if the turn counter is not 10,
        ## no one has won and there are still valid moves to be made
        ## (we know the board is not full because it would have been stopped just above if it had)
        ## change whose turn it is, and print a message indicating that
        #### 
        elif playboard.turncounter != 10:
            playboard.swapTurn()
            playboard.printTurn(player1, computer)

    print("The game has ended. Thanks for playing!")