'''
# Rock Paper Scissors

Let's play! You have to return which player won! In case of a draw return `Draw!`.

**Examples(Input1, Input2 --> Output):**

```
"scissors", "paper" --> "Player 1 won!"
"scissors", "rock" --> "Player 2 won!"
"paper", "paper" --> "Draw!"
```

![rockpaperscissors](http://i.imgur.com/aimOQVX.png)
'''

def rps(p1, p2):
    dict = {"scissors": "paper", "rock": "scissors", "paper": "rock"}
    
    if dict[p1] == p2:
        return "Player 1 won!"
    if p1 == p2:
        return "Draw!"
    
    return "Player 2 won!"