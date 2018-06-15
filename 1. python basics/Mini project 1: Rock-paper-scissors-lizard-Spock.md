# Mini project 1: Rock-paper-scissors-lizard-Spock

In our first mini-project, we will build a Python function 𝚛𝚙𝚜𝚕𝚜(𝚗𝚊𝚖𝚎) that takes as input the string 𝚗𝚊𝚖𝚎, which is one of "𝚛𝚘𝚌𝚔", "𝚙𝚊𝚙𝚎𝚛", "𝚜𝚌𝚒𝚜𝚜𝚘𝚛𝚜", "𝚕𝚒𝚣𝚊𝚛𝚍", or "𝚂𝚙𝚘𝚌𝚔". The function then simulates playing a round of Rock-paper-scissors-lizard-Spock by generating its own random choice from these alternatives and then determining the winner using a simple rule that we will next describe.

While Rock-paper-scissor-lizard-Spock has a set of ten rules that logically determine who wins a round of RPSLS, coding up these rules would require a large number (5x5=25) of 𝚒𝚏/𝚎𝚕𝚒𝚏/𝚎𝚕𝚜𝚎 clauses in your mini-project code. A simpler method for determining the winner is to assign each of the five choices a number:

- 0 — rock
- 1 — Spock
- 2 — paper
- 3 — lizard
- 4 — scissors

In this expanded list, each choice wins against the preceding two choices and loses against the following two choices (if rock and scissors are thought of as being adjacent using modular arithmetic).









**Template**

```python
# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

def name_to_number(name):
    # delete the following pass statement and fill in your code below
    pass

    # convert name to number using if/elif/else
    # don't forget to return the result!


def number_to_name(number):
    # delete the following pass statement and fill in your code below
    pass
    
    # convert number to a name using if/elif/else
    # don't forget to return the result!
    

def rpsls(player_choice): 
    # delete the following pass statement and fill in your code below
    pass
    
    # print a blank line to separate consecutive games

    # print out the message for the player's choice

    # convert the player's choice to player_number using the function name_to_number()

    # compute random guess for comp_number using random.randrange()

    # convert comp_number to comp_choice using the function number_to_name()
    
    # print out the message for computer's choice

    # compute difference of comp_number and player_number modulo five

    # use if/elif/else to determine winner, print winner message

    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric
```

