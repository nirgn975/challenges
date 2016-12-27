"""
Create the hero move method

Create a move method for your hero to move through the level.
Adjust the hero's position by changing the position attribute. The level is a grid with the following values.

00	01	02	03	04
10	11	12	13	14
20	21	22	23	24
30	31	32	33	34
40	41	42	43	44

The dir argument will be a string
```
up
down
left
right
```

If the position is not inside the level grid the method should throw an error and not move the hero
"""

class Hero:
    def __init__(self):
        self.position = '00'
        self.downLimit = 4
        self.upLimit = 0
        self.rightLimit = 4
        self.leftLimit = 0


    def move(self, dir):
        self.position = int(self.position)
        firstNumber = self.position / 10
        secondNumber = self.position / 10

        if dir == 'down' and firstNumber < self.downLimit:
            self.position += 10
        elif dir == 'up' and firstNumber > self.upLimit:
            self.position -= 10
        elif dir == 'left' and secondNumber > self.leftLimit:
            self.position -= 1
        elif dir == 'right' and secondNumber < self.rightLimit:
            self.position += 1
        else:
            self.position = str(self.position)
            raise Exception('new position is out of bounds')

        if self.position < 10:
            self.position = '0{}'.format(str(self.position))
        else:
            self.position = str(self.position)
