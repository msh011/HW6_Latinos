###########################################

#
# 1. In this exercise we will make a "Patient" class
#
# The Patient class should store the state of
# a patient in our hospital system.
#
#
# 1.1)
# Create a class called "Patient".
# The constructor should have two parameters
# (in addition to self, of course):
#
# 1. name (str)
# 2. symptoms (list of str)
#
# the parameters should be stored as attributes
# called "name" and "symptoms" respectively

class Patient:
    
    def __init__(self, name, symptoms):
        self.name = name
        self.symptoms = symptoms
        self._test = None
        self._result = None

#
# 1.2)
# Create a method called "add_test"
# which takes two paramters:
# 1. the name of the test (str)
# 2. the results of the test (bool)
#
# This information should be stored somehow.

    def add_test(self,test,result):
        self._test=test
        self._result=result

#
# 1.3)
# Create a method called has_covid()
# which takes no parameters.
#
# "has_covid" returns a float, between 0.0
# and 1.0, which represents the probability
# of the patient to have Covid-19
#
# The probability should work as follows:
#
# 1. If the user has had the test "covid"
#    then it should return .99 if the test
#    is True and 0.01 if the test is False
# 2. Otherwise, probability starts at 0.05
#    and ncreases by 0.1 for each of the
#    following symptoms:
#    ['fever', 'cough', 'anosmia']

    def has_covid(self):
        if self._test=="covid" and self._result==True:
            return 0.99
        elif self._test=="covid" and self._result==False:
            return 0.01
        else:
            p=0.05
            for i in self.symptoms:
                if i in ['fever', 'cough', 'anosmia']:
                    p+=0.1
            return p

######################

# 2. In this exercise you will make an English Deck class made of Card classes
# 
# the Card class should represent each of the cards
#
# the Deck class should represent the collection of cards and actions on them

# 2.1) Create a Card class called "Card".
# The constructor (__init__ ) should have two parameters the "suit" and the "value" and the suit of the card.
# The class should store both as attributes.

class Card:
    
    def __init__(self,suit,value):
        self.suit=suit
        self.value=value
        


# 2.2) Create a Deck class called "Deck".
# The constructor will create an English Deck (suits: Hearts, Diamonds, Clubs, Spades and values: A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K). It will create a list of cards that contain each of the existing cards in an English Deck.
# Create a method called "shuffle" that shuffles the cards randomly. 
# Create a method called "draw" that will draw a single card and print the suit and value. When a card is drawn, the card should be removed from the deck.

class Deck():
    
    num_cards=0 #Thought the number of cards in the deck could be interesting and added this
    
    def __init__(self):
        self.cards=[]
        self._renew() #I ran into the issue that the deck has less and less cards and wanted to be able to renew the deck (e.g. by shuffeling). Therefore I built a separate renew method that can be used in init and in shuffeling.
        
        
    def _renew(self):   
        Deck.num_cards=0
        suits=["Heart","Diamond","Club","Spade"]
        values=["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        for i in suits:
            for j in values:
                self.cards.append(Card(i,j))
                Deck.num_cards+=1       
            
            
    def shuffle(self):
        import random
        self._renew()
        random.shuffle(self.cards)
        
    
    def draw(self):
        if self.cards!=[]:
            card_drawn=self.cards.pop()
            Deck.num_cards-=1
            print("Suite:",card_drawn.suit,", Value:",card_drawn.value)
        else:
            print("Deck is empty")
    
    
game=Deck()  
game.num_cards
game.shuffle()
game.draw()
game.num_cards   
    


###################

# 3. In this exercise you will create an interface that will serve as template 
# for different figures to compute their perimeter and surface. 

# 3.1Create an abstract class (interface) called "PlaneFigure" with two abstract methods:
# compute_perimeter() that will implement the formula to compute the perimiter of the plane figure.
# compute_surface() that will implement the formula to compute the surface of the plane figure.

# 3.2 Create a child class called "Triangle" that inherits from "PlaneFigure" and has as parameters in the constructor "base", "c1", "c2", "h". ("base" being the base, "c1" and "c2" the other two sides of the triangle and "h" the height). Implement the abstract methods with the formula of the triangle.

# 3.3 Create a child class called "Rectangle" that inherits from "PlaneFigure" and has as parameters in the constructor "a", "b" (sides of the rectangle). Implement the abstract methods with the formula of the rectangle.

# 3.3 Create a child class called "Circle" that inherits from "PlaneFigure" and has as parameters in the constructor "radius" (radius of the circle). Implement the abstract methods with the formula of the circle.

