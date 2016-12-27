/**
Regular Ball Super Ball

Create a class Ball.

Ball objects should accept one argument for "ball type" when instantiated.

If no arguments are given, ball objects should instantiate with a "ball type" of "regular."

```
ball1 = Ball()
ball2 = Ball("super")
ball1.ball_type  #=> "regular"
ball2.ball_type  #=> "super"
```
**/

var Ball = function(ballType) {
  if (!ballType) {
    this.ballType = 'regular';
  } else {
    this.ballType = ballType;
  }
};
