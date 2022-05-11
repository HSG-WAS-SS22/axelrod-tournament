from axelrod.action import Action
from axelrod.player import Player
from random import choices

C, D = Action.C, Action.D


class Ruben(Player):

    # These are various properties for the strategy
    name = 'Ruben'
    classifier = {
        'memory_depth': 1, 
        'stochastic': False,
        'inspects_source': False,
        'manipulates_source': False,
        'manipulates_state': False
    }

    def __init__(self) -> None:
        super().__init__()

    def strategy(self, opponent):
        """This is the actual strategy"""
        # First move
        if len(self.history) == 0:
            return choices([C, D], [0.8, 0.2], k=1)[0]
        # React to the opponent's last move
        if opponent.history[-1] == D:
            return choices([C, D], [0.2, 0.8], k=1)[0]
        return choices([C, D], [0.8, 0.2], k=1)[0]
    