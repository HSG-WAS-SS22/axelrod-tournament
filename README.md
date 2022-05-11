# WAS Axelrod Tournament

Main repository for the Axelrod Tournament of the Web-based Autonomous Systems course that uses the [Axelrod 4.12.0 Python library](https://pypi.org/project/Axelrod/).

## How to install Axelrod
The library requires Python 3.6 or greater. Install with `pip`:
```
pip install axelrod
```

## WAS Axelrod Tournament Rules
Each player submits its strategy for the Prisoner's Dilemma. The tournament is a round robin run (one iteration) so that each player is paired with each other player. 
Each player is also paired with its own twin and with RANDOM, a strategy player that cooperates and defects with equal probability. 
Each match between two players consists of 10 rounds.
The player whose strategy accumulated the greatest score wins.

Scores are attributed based on the Prisoner's Dilemma where each player has two possible actions, Cooperate (C), and Defect(D). The following negative payoffs indicate how many years each player will spend in prison (in absolute value):
|               | Cooperate (C) | Defect (D) |
|:-------------:|:-------------:|:----------:|
| Cooperate (C) |    (-1,-1)    |   (-5,0)   |
|   Defect (D)  |    (0,-5)     |   (-3,-3)  |


## How to prepare for the WAS Axelrod Tournament
### Run a simple tournament 
Run `python3 was-tournament/was_tournament.py` ([was_tournament.py](/was-tournament/was_tournament.py)) to run a simple tournament of 10 rounds (1 round robin) between a `TitForTat`, a `Grudger` (i.e. a Trigger), a `Defector`, a `Cooperator`, and a `Random`.

The tournament produces three files analysing the results:
- was_tournament_analysis.csv: summarises tournament results
- was_results.png: visualizes tournament normalized scores
- was_win_distributions.png: visualizes tournament win distributions

Additionally, the program prints the [morality metrics](https://axelrod.readthedocs.io/en/stable/how-to/calculate_morality_metrics.html) calculated for each player of the tournament.

### Play as a human to explore different strategies
Before implementing your strategy, you can run `python3 was-human-inclusive-match/was-human-inclusive-match.py` ([was-human-inclusive-match.py](/was-human-inclusive-match/was_human_inclusive_match.py)), and try out different startegies by 
[playing as a human against a TitForTat player](https://axelrod.readthedocs.io/en/stable/tutorials/new_to_game_theory_and_or_python/human_interaction.html). 

### Implement and submit your own strategy
Create a new branch, and [implement your strategy](https://axelrod.readthedocs.io/en/fix-documentation/tutorials/contributing/strategy/writing_the_new_strategy.html) in the `was-tournament.wasstrategies` package. (Also, see an [additional strategy example](https://github.com/Axelrod-Python/Axelrod/blob/75ef1f24187350292c43d244370c100c644748bc/docs/how-to/contributing/strategy/writing_the_new_strategy.rst) that considers the history of interactions.)

Your module name should have the format  `{your_name}_strategy.py` and your new strategy class name should have the format `{Name}` (e.g., `Danai()`). See [danai_strategy.py](/was-tournament/wasstrategies/danai_strategy.py) as an example. 

You can always modify the [provided simple tournament](/was-tournament/was_tournament.py) to try out your strategy against basic Axelrod strategies.
