__author__ = 'kguryanov'

import random
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
    """
    Converts an RPSLS throw to an integer
    Prints an error message to console in case an invalid parameter is provided
    :param name: String value
    :return: an integer corresponding to a throw name; None if throw name is invalid
    """
    if name == 'rock':
        return 0
    elif name == 'Spock':
        return 1
    elif name == 'paper':
        return 2
    elif name == 'lizard':
        return 3
    elif name == 'scissors':
        return 4
    else:
        print '[ERROR] Invalid throw "%s". Make sure you throw one of the following: ' \
              'rock, paper, scissors, lizard or Spock.' % name


def number_to_name(number):
    """
    Converts an number to a valid RPSLS throw
    Prints an error message to console in case an invalid parameter is provided
    :param number: Integer value in range [0..4] (inclusive)
    :return: String representation of a throw (rock, paper, scissors, lizard or Spock);
    None if number provided is outside the valid range [0..4]
    """
    if number == 0:
        return 'rock'
    elif number == 1:
        return 'Spock'
    elif number == 2:
        return 'paper'
    elif number == 3:
        return 'lizard'
    elif number == 4:
        return 'scissors'
    else:
        print '[ERROR] Invalid throw: "%d". Valid values are: [0..4].' % number


def rpsls(player_choice):
    """
    Plays RPSLS against player's choice.
    Randomly chooses the throw to play against player
    Prints the throw result to console
    :param player_choice: Player's choice
    :return: None
    """
    print
    print 'Player chooses %s' % player_choice

    player_choice_number = name_to_number(player_choice)

    computer_choice_number = random.randrange(0, 5)
    computer_choice = number_to_name(computer_choice_number)

    print 'Computer chooses %s' % computer_choice

    result = (computer_choice_number - player_choice_number) % 5

    if result == 0:
        print "Player and computer tie!"
    elif result <= 2:
        print "Computer wins!"
    else:
        print "Player wins!"


# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric
#
# print name_to_number("rock")
# print name_to_number("Spock")
# print name_to_number("paper")
# print name_to_number("lizard")
# print name_to_number("scissors")
# print name_to_number("scissors1")
#
# print "==========="
#
# print number_to_name(0)
# print number_to_name(1)
# print number_to_name(2)
# print number_to_name(3)
# print number_to_name(4)
# print number_to_name(5)
# print number_to_name(-1)
