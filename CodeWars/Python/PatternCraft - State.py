"""
The State Design Pattern can be used, for example, to manage the state of a tank in the StarCraft game.

The pattern consists in isolating the state logic in different classes rather than having multiple `if`s to determine what should happen.

Your Task

Complete the code so that when a `Tank` goes into `SiegeMode` it cannot move and its damage goes to `20`. When it goes to `TankMode` it should be able to move and the damage should be set to `5`.

You have 3 classes:

* `Tank`: has a `state`, `canMove` and `damage` properties
* `SiegeState` and `TankState`: has `canMove` and `damage` properties
Note: The tank initial state should be `TankState`.
"""


class SiegeState:
    def __init__(self, m=False, d=20):
        self.m = m
        self.d = d


class TankState:
    def __init__(self, m=True, d=5):
        self.m = m
        self.d = d

class Tank:
    def __init__(self, state = None):
        self.state = TankState()

    def can_move(self):
        return self.state.m

    def damage(self):
        return self.state.d
