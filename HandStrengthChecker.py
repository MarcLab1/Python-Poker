class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
    
    def __str__(self):
        return f"{self.getValueString()} {self.suit}"

    def getValueString(self):
        if(self.value==1):
            return "A"
        elif (self.value == 11):
            return "J"
        elif (self.value == 12):
            return "Q"
        elif (self.value == 13):
            return "K"
        else:
            return self.value    

    #override this method to make our Card class sortable with list.sort()
    def __lt__(self, other):
        return (self.value, self.suit) < (other.value, other.suit)

class HandStrength(object):
    
    def __init__(self, hand):
        self.hand = hand
        self.isFlushVar = False
        self.isStraightVar = False
        self.isAceHighStraightVar = False

    def __str__(self):
       return self.getHandStrength()

    def getHandStrength(self):
        self.hand.sort()
        self.isFlush()
        self.isStraight()

        if(self.isFlushVar and self.isStraightVar):
            if(self.isAceHighStraightVar):
                return "Royal Flush"
            else:
                return "Straight Flush"
        elif(self.isFlushVar):
            return "Flush"
        elif(self.isAceHighStraightVar or self.isStraightVar):
            return "Straight"
        else:
            return self.isPairsEtc()

    def isFlush(self):
        if(self.hand[0].suit == self.hand[1].suit and self.hand[1].suit == self.hand[2].suit and self.hand[2].suit == self.hand[3].suit and self.hand[3].suit == self.hand[4].suit ):
            self.isFlushVar = True

    def isStraight(self):
        if(self.hand[0].value == 1 and self.hand[1].value == 10 and self.hand[2].value == 11 and self.hand[3].value == 12 and self.hand[4].value == 13):
            self.isAceHighStraightVar = True
        elif(self.hand[0].value +1 == self.hand[1].value and self.hand[1].value +1 == self.hand[2].value and self.hand[2].value +1 == self.hand[3].value and self.hand[3].value +1 == self.hand[4].value):
            self.isStraightVar = True
        
    def isPairsEtc(self):
        if((self.hand[0].value == self.hand[1].value and self.hand[1].value == self.hand[2].value and self.hand[2].value == self.hand[3].value) or 
        (self.hand[1].value == self.hand[2].value and self.hand[2].value == self.hand[3].value and self.hand[3].value == self.hand[4].value) ):
            return "4 of a Kind"
        elif((self.hand[0].value == self.hand[1].value and self.hand[1].value == self.hand[2].value and self.hand[3].value == self.hand[4].value) or
        (self.hand[0].value == self.hand[1].value ) and (self.hand[2].value == self.hand[3].value and (self.hand[3].value == self.hand[4].value))):
            return "Full House"
        elif((self.hand[0].value == self.hand[1].value and self.hand[1].value == self.hand[2].value) or 
        (self.hand[1].value == self.hand[2].value and self.hand[2].value == self.hand[3].value) or
        (self.hand[2].value == self.hand[3].value and self.hand[3].value == self.hand[4].value)):
            return "Trips"
        elif((self.hand[0].value == self.hand[1].value and self.hand[2].value == self.hand[3].value) or 
        (self.hand[0].value == self.hand[1].value and self.hand[3].value == self.hand[4].value) or
        (self.hand[1].value == self.hand[2].value and self.hand[3].value == self.hand[4].value)):
            return "Two Pairs"
        elif((self.hand[0].value == self.hand[1].value) or (self.hand[1].value == self.hand[2].value) or 
        (self.hand[2].value == self.hand[3].value) or (self.hand[3].value == self.hand[4].value)):
            return "One Pair"
        else:
            return "High Card"
        

handStr = HandStrength([
Card(1, "Diamond"), 
Card(13, "Diamond"),
Card(12, "Clubs"),
Card(12, "Diamond"),
Card(5, "Diamond"),
])

print(handStr.getHandStrength())
