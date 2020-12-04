########### Current BEST!

from Player import Player
from Game import Action

global their_previous_actions

global angry

global my_prev_actions

global angry_list


my_prev_actions = []

their_previous_actions = []

angry = False

angry_list = []

cooperator = False

## Spiteful Water Tester

class MyPlayer(Player):
    # 1. Add your UINs seperated by a ':'
    #    DO NOT USE A COMMA ','
    #    We use CSV files and commas will cause trouble
    # 2. Write your strategy under the play function
    # 3. Add your team's name (this will be visible to your classmates on the leader board)

    UIN = "629001385"

    def play(self, opponent_prev_action):

        global angry
        global my_prev_actions
        global their_previous_actions
        global cooperator

        #if the uncertainty is too much I just confess because its too random
        if self.error_rate > 0.3:
            return Action.Confess

        if angry == True:
            return Action.Confess

        #this is code for the start of the match
        if opponent_prev_action != Action.Noop:
            their_previous_actions.append(opponent_prev_action)
        elif opponent_prev_action == Action.Noop:
            angry = False
            my_prev_actions = []
            their_previous_actions = []
        # I am testing the water here by remaining silent to see if I can pull out the tit for tat and the tough guy
        if len(my_prev_actions) < 3:
            my_prev_actions.append(Action.Silent)
            return Action.Silent

        if len(their_previous_actions) <= 11:
            return opponent_prev_action

        if self.error_rate <= 0.1:
            if len(their_previous_actions) > 11:
                counter1 = 0
                counter2 = 0
                for i in their_previous_actions[-11:]:
                    counter1 += 1
                    if i == Action.Confess:
                        counter2 += 1
                if counter2 / counter1 > 0.7:
                    angry = True
                    return Action.Confess
                else:
                    return Action.Silent
        # this is the exact same code as above except I am chance the threshold for getting angry as the uncertainty increases
        elif self.error_rate > 0.1:
            if len(their_previous_actions) > 11:
                counter1 = 0
                counter2 = 0
                for i in their_previous_actions[-11:]:
                    counter1 += 1
                    if i == Action.Confess:
                        counter2 += 1
                if counter2 / counter1 > 0.8:
                    angry = True
                    return Action.Confess
                else:
                    return Action.Silent


    def __str__(self):
        return "Shilleh"