
import random


class Deck:
    
    # class attribute
    cards = [str(i) for i in range(2,11)] + ["J", "Q", "K", "A"]
    suits = ["D", "H", "C", "S"]
    
    def __init__(self):
        # initializing empty list we can keep track of the cards
        self.card_lst = []
        # calling the function distribute to get the cards from the list
        self.distribute_deck()
        
        
    def distribute_deck(self):
        # we basically combining the suit and card values and generating new list with existing values
        new_deck = []
        for suit in Deck.suits:
            for card in Deck.cards:
                combine_card = suit + card
                new_deck.append(combine_card)
                
        return new_deck
    
    def shuffle(self):
        # it shuffles the list that was inititally made by combining cards 
        return random.shuffle(self.card_lst)
    
    def deal(self,n):
        # first of all we have to check if the cards are available to distribute based on given number
        deal_cards = []
        
        for i in range(n):
            if len(self.cards) == 0:
                break
            
            removed_card = self.card_lst.pop()
            deal_cards.append(removed_card)
            
        return deal_cards
    
    
    def sort_by_suit(self):
        
        cards_arrangement = { "H": [], "D" : [], "C": [], "S": []}
        
        for card in self.cards:
            # example JC = give out C which represents club
            suit = card[-1]
            cards_arrangement[suit].append(card)
            
            
        self.cards = (
            cards_arrangement["H"] +
            cards_arrangement["D"] +
            cards_arrangement["C"] +
            cards_arrangement["S"]
        )
    def contains(self,card):
        return card in self.card_lst
        
    def copy(self):
        new_obj = Deck()
        new_obj.card_lst = self.card_lst
        return new_obj
    
    def get_cards(self):
        pass
        
             
    