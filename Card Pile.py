class CardPile:
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
        if index == 0:
            print(str(self.items[0]) + ' ' + ('* ' * (len(self.items) - 1)))
        elif index == 1:
            print(' '.join(map(str, self.items)))
            

# cards = [1, 3, 6, 2, 4, 5]
# pile1 = CardPile()
# pile2 = CardPile()
# pile3 = CardPile()
# remov1 = pile1.remove_top()
# print(remov1)
# pile2.add_bottom(0)
# pile1.add_bottom(1)
# pile3.add_bottom(3)
# pile3.add_bottom(pile1.remove_top())
# pile1.print_all(1)
# pile2.print_all(1)
# pile3.print_all(1)