"""This code simulate Two player Rock-paper-cissor game 
Here i have assignes numeric values to each possible outcome
Rock = 1 ,paper = 2  and scissor = 3"""

    

import random 
import time
import sys
class rpcGame:
    def game(self):
        flag = 'y';

        rules = """Gmae Rules:
        1.Rock beats scissors
        2.Scissors beats paper
        3.Paper beats rock"""
        print"\n Welcome to Rock-Paper-Scissor Game: "
        print "\n",rules;
        choice = input("Enter '0' to play...! ");
        if choice != 0:
            return
        else:
            while flag == 'y':
                player1 = input("\n Player 1's turn, 1 to play ");
                if player1 == 1:
                    p1 = random.randint(1,3);
                else:
                    print"\n Wrong input..!";
                    break;
                player2 = input("\n Player 2's turn, press 2 to play ");
                if player2 == 2:
                    p2 = random.randint(1,3);
                else:
                    print"\nWrong input..!";
                    break;
                animation = ["Rock ",".",".","."," Paper ",".",".","."," Scissor ",".","." ,"."];
                for i in range(len(animation)):
                    print animation[i],;
                    sys.stdout.flush(); #To buffer the output, because we are giving delay
                    time.sleep(0.5);
                
                  
                if p1 == 1 and p2 == 2: #rule3 , p2 wins
                    print"\n player 2 Wins..!! Rule3: Paper beats rock ";
                elif p1 == 1 and p2 == 3: #rule1, p1 wins 
                    print "\n Player 1 wins..!! Rule1: Rock beats scissors " 
                elif p1 == 2 and p2 == 1: #rule3, p1 wins 
                    print "\n Player 1 wins..!! Rule3: Paper beats rock "
                elif p1 == 2 and p2 == 3: #rule2, p2 wins 
                    print "\n Player 2 wins..!! rule2: Scissors beats paper "
                elif p1 == 3 and p2 == 1: #rule1, p2 wins 
                    print "\n player 2 wins..!! Rule1: Rock beats Scissor " 
                elif p1 == 3 and p2 == 2: #rule2, p1 wins 
                    print "\n player 1 wins..!! Rule2: Scissors beats paper "
                elif p1 == p1: #11,22,33 no rules defined
                    print"\n No one wins or lose, Same out come .....try again";
                flag = raw_input("\nPress y to play again or any any key to abort..!");
            
                
if __name__ == "__main__":
    gameObject = rpcGame();
    gameObject.game();

    
    



