"""Code retrieved from Axelrod rand.py strategy"""

from axelrod.action import Action
from axelrod.player import Player

C, D = Action.C, Action.D


class Jonathan(Player):
    """A player who randomly chooses between cooperating and defecting.
    This strategy came 15th in Axelrod's original tournament.
    Names:
    - Random: [Axelrod1980]_
    - Lunatic: [Tzafestas2000]_
    """

    name = "Jonathan - Better than yours"
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
        self.calm_count = 0
        self.punish_count = 0

    def strategy(self, opponent: Player) -> Action:
        """Actual strategy definition that determines player's action."""

        if len(self.history) == 0:
            return C

        if self.punish_count > 0:
            self.punish_count -= 1
            return D

        if self.calm_count > 0:
            self.calm_count -= 1
            return C

        if opponent.history[-1] == D:
            self.punish_count = opponent.defections - 1
            self.calm_count = 2
            return D
        return C

    def strategy2(self, opponent: Player) -> Action:
        # First move
        if not self.history:
            return C

        # If the opponent defected on the previous round, Defect.
        if opponent.history[-1] == D:
            return D

        # If the opponent does not defect against defectBot, Defect.

        # If defecting on this round would lead to CheeseBot being punished for it
        # in future rounds, Cooperate. CheeseBot checks this by simulating future rounds
        # with a simulated history in which it defects on the current round.

        # If the opponent is a mirror-like bot, Cooperate. To test whether a bot is
        # mirror-like, CheeseBot simulates the opponent and checks if it defects against
        # DefectBot and cooperates with a bot that plays tit-for-tat but defects against
        # CooperateBot and DefectBot.

        # Defect
        return D

    def _post_init(self):
        super()._post_init()
        if self.p in [0, 1]:
            self.classifier["stochastic"] = False
        # Avoid calls to _random, if strategy is deterministic
        # by overwriting the strategy function.
        if self.p <= 0:
            self.strategy = self.defect
        if self.p >= 1:
            self.strategy = self.cooperate

    @classmethod
    def cooperate(cls, opponent: Player) -> Action:
        return C

    @classmethod
    def defect(cls, opponent: Player) -> Action:
        return D
