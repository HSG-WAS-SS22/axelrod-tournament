"""Code retrieved from Axelrod rand.py strategy"""

from axelrod.action import Action
from axelrod.player import Player

C, D = Action.C, Action.D


class Marcel(Player):
    """ 
    """

    name = "Marcel"
    classifier = {
        "memory_depth": 0,   # Memory-one Four-Vector = (p, p, p, p)
        "stochastic": True,
        "long_run_time": False,
        "inspects_source": False,
        "manipulates_source": False,
        "manipulates_state": False,
    }

    def __init__(self, p: float = 0.5) -> None:
        """
        Parameters
        ----------
        p, float
            The probability to cooperate
        Special Cases
        -------------
        Random(0) is equivalent to Defector
        Random(1) is equivalent to Cooperator
        """
        super().__init__()
        self.p = p

    def strategy(self, opponent: Player) -> Action:
        """Actual strategy definition that determines player's action."""
        # First move
        if not self.history or len(self.history) == 1:
            return D
        # React to the opponent's last two moves
        if opponent.history[-2] == C and opponent.history[-1] == C:
            return C
        return D

    # def _post_init(self):
    #     super()._post_init()
    #     if self.p in [0, 1]:
    #         self.classifier["stochastic"] = False
    #     # Avoid calls to _random, if strategy is deterministic
    #     # by overwriting the strategy function.
    #     if self.p <= 0:
    #         self.strategy = self.defect
    #     if self.p >= 1:
    #         self.strategy = self.cooperate

    @classmethod
    def cooperate(cls, opponent: Player) -> Action:
        return C

    @classmethod
    def defect(cls, opponent: Player) -> Action:
        return D