import curses
import random

def start_screen(stdscr):
    # Clear the screen
    stdscr.clear()

    # Get the dimensions of the terminal window
    height, width = stdscr.getmaxyx()

    # Calculate the center of the screen
    center_y = height // 2
    center_x = (width - len("Welcome to the Terminal Tarot reader!")) // 2

    # Add text to the center of the screen
    stdscr.addstr(center_y, center_x, "Welcome to the Terminal Tarot reader!")

    # Add a new line and the prompt
    stdscr.addstr(center_y + 1, center_x, "Press any key to begin!")

    # Refresh the screen
    stdscr.refresh()

    # Wait for a key press
    stdscr.getkey()

# Use the wrapper function to properly initialize and finalize curses
if __name__ == "__main__":
    curses.wrapper(start_screen)
