#################################################################################
#project 11
#allows two players to play the game Gomoku
#Displays board and users input row and column values to place on the board
#Alernates players
#if user has five in a row or column or diagonally 
#game shows them as winner and ends
#raises errors for any incorrect moves
##################################################################################

class GoPiece(object):
    ''' Returns the piece corresponding with the player'''
    def __init__(self,color = 'black'):
        ''' Creates a gomoku piece and checks if the color is valid'''
        #if statement to raise error if color is not black or white
        if color != 'black' and color != 'white':
            raise MyError('Wrong color.')
        else:
            self.__color =  color #give value to color
    def __str__(self):
        ''' returns the correct piece based off of the color'''
        if self.__color == 'black':
            return ' ● '
        if self.__color == 'white':
            return ' ○ '
    def get_color(self):
        ''' returns the color to the user'''
        return self.__color
            
class MyError(Exception):
    def __init__(self,value):
        self.__value = value
    def __str__(self):
        return self.__value

class Gomoku(object):
    ''' Sets up the game, displays the board, and allows user to play the game '''
    def __init__(self,board_size = 15,win_count = 5,current_player = 'black'):
        ''' Checks four attribues, board size win count and current player, if correct then
        it creates the board'''
        #raise error if board size is not an integer
        if type(board_size) != int and isinstance(board_size, int) is False:
            raise ValueError
        else:
            self.__board_size = board_size #create value for board size 
        #raise error if win count is not an integer
        if type(win_count) != int and isinstance(win_count, int) is False:
            raise ValueError
        else:
            self.__win_count = win_count #create value for win count
        #raise error is current player is not a valid color
        if current_player != 'black' and current_player != 'white':
            raise MyError('Wrong color.')
        else:
            self.__current_player = current_player #create value for  current player
        #creates the board
        self.__go_board = [ [ ' - ' for j in range(self.__board_size)] for i in range(self.__board_size)]
         
    def assign_piece(self,piece,row,col):
        ''' places a given piece on the board if it is a valid point.'''
        #raises error if  row and column not in board dimensions
        if row > self.__board_size or col > self.__board_size:
            raise MyError('Invalid position.')
        #raises error if trying to place a piece where there is an existing piece
        if self.__go_board[row-1][col-1] != ' - ':
            raise MyError('Position is occupied.')
        else:
            self.__go_board[row-1][col-1] = piece #place piece on board
    def get_current_player(self):
        ''' returns the current player'''
        return self.__current_player #returns the current player
    
    def switch_current_player(self):
        ''' switches the current player'''
        #gives the white player if the player is black
        if self.__current_player == 'black': 
            self.__current_player = 'white'
        #gives the black player if player is white
        else:
            self.__current_player = "black"
    def __str__(self):
        s = '\n'
        for i,row in enumerate(self.__go_board):
            s += "{:>3d}|".format(i+1)
            for item in row:
                s += str(item)
            s += "\n"
        line = "___"*self.__board_size
        s += "    " + line + "\n"
        s += "    "
        for i in range(1,self.__board_size+1):
            s += "{:>3d}".format(i)
        s += "\n"
        s += 'Current player: ' + ('●' if self.__current_player == 'black' else '○')
        return s
    def current_player_is_winner(self):
        ''' checks if the current player has any winning rows'''
        #for loop the check horizontal winners returns true if there is one
        for row in range(0, self.__board_size):
            for col in range(0, self.__board_size - self.__win_count +1):
                for p in range(0, self.__win_count):
                    if type(self.__go_board[row][col + p]) == GoPiece and self.__go_board[row][col+ p].get_color() == self.__current_player:
                        continue
                    else:
                        break
                else:
                    return True
        #for loop to check vertical winnters returns true if there is one
        for row in range(0, self.__board_size - self.__win_count + 1 ):
                for col in range(0, self.__board_size ):
                    for p in range(0, self.__win_count):
                        if type(self.__go_board[row + p][col]) == GoPiece and self.__go_board[row + p][col].get_color() == self.__current_player:
                            continue
                        else:
                            break
                    else:
                        return True
        #for loop to check diagonal left winners returns true if there is one
        for row in range(0, self.__board_size - self.__win_count + 1 ):
                for col in range(0, self.__board_size - self.__win_count + 1 ):
                    for p in range(0, self.__win_count):
                        if type(self.__go_board[row - p][col +p]) == GoPiece and self.__go_board[row - p][col + p].get_color() == self.__current_player:
                            continue
                        else:
                            break
                    else:
                        return True
        #for loop to check diagonal right winners returns true if there is one
        for row in range(0, self.__board_size - self.__win_count + 1 ):
                for col in range(0, self.__board_size - self.__win_count + 1 ):
                    for p in range(0, self.__win_count):
                        if type(self.__go_board[row + p][col +p]) == GoPiece and self.__go_board[row + p][col + p].get_color() == self.__current_player:
                            continue
                        else:
                            break
                    else:
                        return True
        return False #return false if theres no winners
def main():
    '''allows the player to the play the game gomoku and raises error when invalid moves happen'''
    board = Gomoku() #calls the gomoku class
    print(board) #print board
    play = input("Input a row then column separated by a comma (q to quit): ") #input a row and column
    while play.lower() != 'q': #continues as long as the player doesnt quit 
        play_list = play.strip().split(',') #split user input 
        try: 
            row = int(play_list[0]) #separates row from user input
            col = int(play_list[1]) ##separates column from user input
            player = board.get_current_player() #current player 
            piece = GoPiece(player) #current player's piece
            board.assign_piece(piece,row,col) #place piece on board
            if board.current_player_is_winner() is True: #checks if the current player has won
                player = board.get_current_player() #gets current player
                print(board) #prints final board
                print("{} Wins!".format(board.get_current_player())) #prints winning statement
                break #breaks while loop and ends game
            board.switch_current_player() #switch player 
            player = board.get_current_player() #new current player
            
            piece = GoPiece(player) #new current player's piece
            print(board) #prints board
            play = input("Input a row then column separated by a comma (q to quit): ") #user input
        except ValueError: #raises error if value is incorrect
            print('Incorrect input. Try again.')
            print(board)
            play = input("Input a row then column separated by a comma (q to quit): ")    
        except IndexError: #raises error if value is incorrect
            print('Incorrect input. Try again.')
            print(board)
            play = input("Input a row then column separated by a comma (q to quit): ")    
        
        except MyError as error_message: #calls error message from class
            print("{:s}\nTry again.".format(str(error_message)))
            print(board)
            play = input("Input a row then column separated by a comma (q to quit): ")

if __name__ == '__main__':
   main()
    





