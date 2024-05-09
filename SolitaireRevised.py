import random
import math

class CardPile:
    ''' A definition of a class that creates an object called 'CardPile' which acts 
    as a pile of cards, the first index of the list represents the top of the card 
    pile while the last index represents the bottom'''
    
    def __init__(self):
        self.items = []
        
    def add_top(self, item):
        self.items = [item] + self.items
        
    def add_bottom(self, item):
        self.items.append(item)
        
    def remove_top(self):
        return self.items.pop(0)
        
    def remove_bottom(self): 
        return self.items.pop()
        
    def size(self):
        return (len(self.items))
    
    def peek_top(self):
        return self.items[0]
    
    def peek_bottom(self): 
        return self.items[self.size() - 1]
        
    def print_all(self, index): 
        ''' Prints the elements of a card pile out'''
        
        # Prints elements of a card pile out but with asterisks instead of values
        if index == 0:
            if len(self.items) != 0:
                print(str(self.items[0]) + ' ' + ('* ' * (len(self.items) - 1)))
            else:
                print('')
                
        # Prints elements of a card pile out
        elif index == 1:
            print(' '.join(map(str, self.items)))


class Solitaire:
    '''A class definition that creates an object for a game of solitaire'''

    def __init__(self, cards):
        # This list stores lists of CardPile objects used in one game
        self.piles = [] 
        self.num_cards = len(cards)
        self.num_piles = (self.num_cards // 8) + 3
        self.max_num_moves = math.ceil(self.num_cards * 1.9)
        self.balance = 0
        
        # Initialises empty CardPile objects in the 
        # 'piles' list based on the number of piles needed
        for i in range(self.num_piles): 
            self.piles.append(CardPile())
            
         # Adds the 'cards' list to the first CardPile object in the 'piles' list
        for i in range(self.num_cards):
            self.piles[0].add_bottom(cards[i])
            
            
    def get_pile(self, i):
        return self.piles[i] 
    
     
    def display(self): 
        '''Displays a visual representation of the game state in the console'''
        
        # Prints the first line of the game
        print('Pile 0: ', end='')
        self.piles[0].print_all(0) 
        
        # Prints the remaining lines of the game
        for pile in range(1, self.num_piles): 
            print('Pile ' + str(pile) + ': ', end='')
            self.piles[pile].print_all(1) 
            
                 
    def move(self, p1, p2):
        '''Moves cards between piles based off the paramters given:
            p1: pile the card is being moved from
            p2: pile the card is being moved to'''
        
        # Move top card of the first pile to the bottom of the pile if not empty
        if p1 == 0 and p2 == 0: 
            if self.piles[p1].size() != 0:
                self.piles[p2].add_bottom(self.piles[p1].remove_top())
                
        # Move the top card of the first pile to the bottom of another as long as the last 
        # number of the second pile is one more of the first number of the first pile
        elif p1 == 0 and p2 > 0 and self.piles[p1].size() != 0:
            if ((self.piles[p2].size() != 0 and self.piles[p2].peek_bottom() == 
                 self.piles[p1].peek_top() + 1) or self.piles[p2].size() == 0):
                self.piles[p2].add_bottom(self.piles[p1].remove_top())
                
        # Move cards from one pile to the bottom of another as long as the last 
        # number of the second pile is one more of the first number of the first pile
        elif (p1 > 0 and p2 > 0 and self.piles[p1].size() != 0
              and self.piles[p2].size() != 0):
            if self.piles[p1].peek_top() == self.piles[p2].peek_bottom() - 1:
                for i in range(self.piles[p1].size()):
                    self.piles[p2].add_bottom(self.piles[p1].remove_top()) 
                    
                     
    def is_complete(self):
        '''Checks to see if player can win the game, win condition:
            - No cards on the first pile
            - All the cards are on one pile
            - All the cards are in decreasing order'''
            
        pile_empty_count = 0
        for index in range(1, self.num_piles):
            if self.piles[index].size() != 0:
                pile_empty_count += 1
                
        # Checks to see if first pile has no cards and if only one pile is empty 
        if self.piles[0].size() == 0 and pile_empty_count == 1:
            return True
        return False    
    
                               
    def play(self, play_input, balance):
        '''Runs the Solitaire game with two parameters
            play_input: input that checks if player wants to start the game
            balance: the current balance of the player'''
        
        # Shows player balance and first pile if they press enter on the main menu
        if play_input == '':
            print("\n         BETTING")
            print("__________________________")
            print("Pile 1: ", end = '')
            self.piles[0].print_all(0)
            print(f'Balance: ${balance}\n')
            
            # Ask the player how much to bet, only accept input if player enters
            # a valid number, has enough money and puts in a minimum of $50
            while True:
                try:
                    bet_money = int(input("""How much would you like
        to bet?
         $"""))
                    if balance - bet_money < 0:
                        print('    NOT ENOUGH MONEY.\n')
                    elif bet_money < 50:
                        print('      MINIMUM $50.\n')
                    else:
                        break
                except ValueError:
                    print('PLEASE ENTER A VALID NUMBER.\n')
            balance -= bet_money
                
            # Start the game   
            print("__________________________")
            print("\n       Game Start!")
            print("__________________________\n")
            move_number = 1
            
            # Only loops the game when the max number of moves is not exceeded 
            # and the win condition is not satisfied
            while move_number <= self.max_num_moves and not self.is_complete():
                self.display()
                print("__________________________\n")
                print("Round", move_number, "out of", self.max_num_moves, end = ": ")
                pile1 = int(input("Move from pile no.: "))
                print("Round", move_number, "out of", self.max_num_moves, end = ": ")
                pile2 = int(input("Move to pile no.: "))
                print("__________________________\n")
                if (pile1 >= 0 and pile2 >= 0 and pile1 < self.num_piles
                    and pile2 < self.num_piles):
                    self.move(pile1, pile2)
                move_number += 1
                
            # Ends the game when the win condition is satisfied
            if self.is_complete():
                balance += bet_money*2
                print("You Won in", move_number - 1, "steps!\n")
            else:
                print("  You Lose!\n")
                
            # Gives the player an option to play again
            while True:
                print(f'  Balance: ${balance}')
                play_again = input('  Play Again? (Y/N): ')
                if (play_again == 'Y' or play_again == 'y' or 
                    play_again == 'N' or play_again == 'n'):
                    return play_again, balance
                print('Please enter Y or N.')       
                

def random_card_pile():
    '''Creates a random new card pile'''
    
    # Initialise a card pile with a random length
    card_pile = []
    pile_length = random.randint(7, 13)
    random_card = random.randint(1, 13 - pile_length + 1)
    first_card = random_card
    
    # Add a random card to the list in the range of the first random card and the
    # highest value card in the pile (first card + the length of the pile)
    for i in range(pile_length):
        while random_card in card_pile:
            random_card = random.randint(first_card, first_card + pile_length - 1)
        card_pile.append(random_card)
    
    # 66% chance to swap the first index of the card pile with a random index because
    # the first index is always the smallest number
    if random.randint(0,2) < 2:
        random_index = random.randint(1, pile_length - 1)
        card_pile[0], card_pile[random_index] = card_pile[random_index], card_pile[0]
    return card_pile

def main():
    '''Runs the game'''
    replay_input = 'Y'
    balance = 500
    enter_input = input("""__________________________
|************************|   
|*      WELCOME TO      *|  
|*      SOLITAIRE       *|  
|*                      *|  
|* PRESS ENTER TO BEGIN *|  
|________________________|""")
    
    # Starts the game only if the player has enough money and the right play input (Y or y)
    while True:
        cards = random_card_pile()
        if replay_input == 'Y' or replay_input == 'y':
            if balance > 0:
                game = Solitaire(cards)
                replay_input, balance = game.play(enter_input, balance)
            else:
                print("____________________________________________")
                print('\nSorry, you do not have enough money to play.')
                print('                 Goodbye\n')
                break
        elif replay_input == 'N' or replay_input == 'n': 
            print("__________________________")
            print("""\n    Have a good day!
                
                """)
            break
        
        
if __name__ == '__main__':
    main()
