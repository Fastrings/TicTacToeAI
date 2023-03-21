Tic-Tac-Toe in Python
Arthur Launoy <arthur.launoy88@gmail.com>

SUMMARY

Simple TicTacToe command-line game with added AIs playing the game. The basic parts
of this appliation were implemented following Robert Heaton's post, available on his website:
https://robertheaton.com/2018/10/09/programming-projects-for-advanced-beginners-3-a/.

USAGE

python main.py
&emsp;Play against the computer. More instructions will be prompted
python main.py battles [num] [ai1] [ai2]
&emsp;Launch any *num* number of games pitching *ai1* and *ai2* against each other.
&emsp;The AI *ai1* will always play first. Adding save at the end of this line saves
&emsp;the result of the battles to the database.


After running the *battles* option a good number of times, we can obtain statistics on 
our game of TicTacToe. Here are mine, visualized using Microsoft's tool, Power BI.

[! Alt text](Statistics.png?raw=true "Statistics")