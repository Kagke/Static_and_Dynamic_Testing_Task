import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.card1 = Card("Hearts", 1)
        self.card2 = Card("Spades", 5)
        self.card3 = Card("Diamonds", 10)
        self.card_game = CardGame()

    def test_check_card_value(self):
        self.assertEqual( 1 , self.card1.value  )

    def test_check_card_suit(self):
        self.assertEqual("Hearts" , self.card1.suit)
    
    def test_check_for_ace_false(self):
        result = self.card_game.check_for_ace(self.card2)
        self.assertEqual(False, result)

    def test_check_for_ace_true(self):
        result = self.card_game.check_for_ace(self.card1)
        self.assertEqual(True, result)

    def test_higher_card_on_deck(self):
        result = self.card_game.highest_card(self.card1, self.card2)
        self.assertEqual(self.card2, result)

    def test_for_total_value_of_cards(self):
        cards= [self.card1,self.card2,self.card3]
        result = self.card_game.cards_total(cards)
        self.assertEqual("You have a total of 16", result)