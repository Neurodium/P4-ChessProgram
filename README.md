# Project Name

Chess Tournament

## Project description

Program in console to manage chess tournaments

## Project features

With this console-program, you can manage chess tournaments by:
- creating multiple tournaments
- adding players into a tournament 
- generating rounds of matchs using the swiss rules
- displaying reports on screen

With this program you can record your players matchs through the different tournaments and manage their ranking
The reports will help you to track your players data and tournament as well
At any point in time, you can save or load your data into a small database using TinyDB

## Project structure

The program is built under the MVC (Model View Controller) architecture.
Model folder regroups the object classes
View folder regroups the reports and menu displays
Controller regroups the  actions between views and objects

## Project installation

### 1. Install Python
\
Install python 3.4 or above : https://www.python.org/downloads/

	  (https://www.python.org/downloads/)

### 2. Virtual environment
\
Execute command:

	  python -m venv env

Activate venv:

	  source env/bin/activate
	
Windows:

	  {path to venv}\\Scripts\\activate.bat

### 3. Package install
\
Install requirements

	  pip install -r requirements.txt
  
### 4. Generate flake8-html report
\
Execute the following commant in the terminal:
 
    flake8 --format=html --htmldir=flake8_rapport
    
### 5. Parameters that can be changed
\
The program runs with default settings set as:
* 8 players per tournament
* 4 rounds per tournament
 
These parameters can be changed if a tournament needs to be changed

## How to use the program

After executing main.py:
1. Create a tournament
2. Add the players to it until you reach the max number of players
3. When all players have been added, first round is automatically generated with the pair of matches
4. Enter the score for each match
5. When all score have been entered, round is closed and a new one is opened till the max number of rounds is hit
6. When tournament is over, you can close it to create a new one
7. At any point in time you can save your data or load the last state saved, print reports
