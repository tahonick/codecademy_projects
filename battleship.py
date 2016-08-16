Skip to content
 
 
Search…
All gists
GitHub
New gist @tahonick
  Star 1
  Fork 0
  @pdpinchpdpinch/battleship.py
Created 4 years ago
Embed  
<script src="https://gist.github.com/pdpinch/3977680.js"></script>
  Download ZIP
 Code  Revisions 2  Stars 1
Codecademy Battleship game
Raw  battleship.py

import random

board = []

for x in range(0,5):
  board.append(["O"] * 5)

def print_board(board):
  for row in board:
    print " ".join(row)

print "Let's play Battleship!"
print_board(board)

def random_row(board):
  return random.randint(0,len(board)-1)

def random_col(board):
  return random.randint(0,len(board[0])-1)

ship_row = random_row(board)
ship_col = random_col(board)
# print ship_row
# print ship_col

#Everything from here on should go in your for loop!
#Be sure to indent!
max_guesses = 5
for turn in range(max_guesses):
	guess_row = input("Guess Row:")
	guess_col = input("Guess Col:")

	if guess_row == ship_row and guess_col == ship_col:
	  print "Congratulations! You sunk my battleship!"
	  break
	else:
	  if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
	    print "Oops, that's not even in the ocean."
	  elif(board[guess_row][guess_col] == "X"):
	    print "You guessed that one already."
	  else:
	  	print "You missed my battleship!"
	  	board[guess_row][guess_col] = "X"
	  	if turn == (max_guesses-1):
	  		print "Game over"
	  # Print (turn + 1) here!
	  print "You have used", (turn), "guesses out of 5."
	  print_board(board)
 @tahonick
  
         
Write  Preview

Leave a comment
Attach files by dragging & dropping,  Choose Files selecting them, or pasting from the clipboard.
 Styling with Markdown is supported
Comment
Contact GitHub API Training Shop Blog About
© 2016 GitHub, Inc. Terms Privacy Security Status Help
