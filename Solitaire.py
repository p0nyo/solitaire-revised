class CardPile:
    ''' A definition of a class that creates an object called 'CardPile' which acts as a pile of cards, 
    the first index of the list represents the top of the card pile while the last index represents the bottom '''
    
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
    '''A class definition that creates an object for a game of solitaire
        cards: a list of starting cards for the first pile'''
        
    def __init__(self, cards):
        # This list stores lists of CardPile objects used in one game
        self.piles = [] 
        self.num_cards = len(cards)
        self.num_piles = (self.num_cards // 8) + 3
        self.max_num_moves = self.num_cards * 2
        
        # Initialises empty CardPile objects in the 'piles' list based on the number of piles needed
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
        print('0: ', end='')
        self.piles[0].print_all(0) 
        
        # Prints the remaining lines of the game
        for pile in range(1, self.num_piles): 
            print(str(pile) + ': ', end='')
            self.piles[pile].print_all(1)
            
            
    def move(self, p1, p2):
        '''Moves cards between piles based off the paramters given:
            p1: pile the card is being moved from
            p2: pile the card is being moved to'''
            
        # Move top card of the first pile to the bottom of the same pile if not empty
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
                  
                    
    def play(self):
        '''Runs the Solitaire game, no parameters are needed'''
        
        print("********************** NEW GAME *****************************")
        move_number = 1
        
        # Only loops the game when the max number of moves is not exceeded 
        # and the win condition is not satisfied
        while move_number <= self.max_num_moves and not self.is_complete():
            self.display()
            print("Round", move_number, "out of", self.max_num_moves, end = ": ")
            pile1 = int(input("Move from pile no.: "))
            print("Round", move_number, "out of", self.max_num_moves, end = ": ")
            pile2 = int(input("Move to pile no.: "))
            if (pile1 >= 0 and pile2 >= 0 and pile1 < self.num_piles
                and pile2 < self.num_piles):
                self.move(pile1, pile2)
            move_number += 1
            
        # Ends the game when the win condition is satisfied
        if self.is_complete():
            print("You Win in", move_number - 1, "steps!\n")
        else:
            print("You Lose!\n")
    
    
# Code to run the game
cards = [3, 6, 2, 5, 4, 1]
game = Solitaire(cards)
game.play()