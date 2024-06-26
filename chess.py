import pygame
from board import ChessBoard
from userInterface import UserInterface


if __name__ == "__main__":
    pygame.init()  # initialize pygame
    # set window size for create pygame window for chess program
    surface = pygame.display.set_mode([600, 600], 0, 0)  # (Re adjust the coordinate if you want to change size of game's window

    # sets the title of the window
    pygame.display.set_caption('CHESS-DEMYSTIFYING AI')

    # Initialize chessBoard class. Used for our interface
    Board = ChessBoard()

    # create and initialize User interface object to run pygame chess program
    UI = UserInterface(surface, Board)

    UI.playGame()  # call play game function to start the game

    pygame.quit()  # Close program
