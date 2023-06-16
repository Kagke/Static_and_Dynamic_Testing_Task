### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:

#there is not a function that  gives the __init__ self.
  def check_for_ace(self, card):
    if card.value = 1:
      # card.value == 1
      return True
    else
#the else doesnt have collums ( : ) in the end
      return False
   

  dif highest_card(self, card1 card2):
  # in this line def is mispronounced  with dif and inside the parenthesis between card1 and card2 it needs one coma
  if card1.value > card2.value:
  # the if statement and everything under it is outside of the def statement
    return card
  # there is no variable called card so this will break , it is missing the number in the end (card1)
  else:
    return card2
  


def cards_total(self, cards):
#this def is outside of the class so it wont be called anywhere
  total
# in this line total is not a variable it is missing the value 
  for card in cards:
    total += card.value
# this line will break because total is not menctioned as a variable just like line 40
    return "You have a total of" + total
  # this line wont work because total is nothing but a error here plus it sould be outside the for loop and should be a str(total)
  
```
