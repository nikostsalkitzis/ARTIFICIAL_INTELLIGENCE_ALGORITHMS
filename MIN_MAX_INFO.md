The MinMax algorithm is used in game theory and it used to determine the best move for 
a player in a competitive game. By the term competitive we mean that
it is a game with two players which are orthological(declaring that they both wan to win the game).
It is important that both of the players have the same amount of information, the play consecutively and they have the same rules.
The definition of the world of the game includes the rules, the possible moves and the operands for the moves 
which are the first. The algorithm has a very interesting name, since its player has
to make a move which will help him THE MOST in his way to win and affects THE WORST the opponent's plan to win.
So, based on a criterion called utitlity function which determines how good is the next move we are going to define two players
called MAX and MIN and by default we are the Max one. The most common thought in games like that is that based on my opponent's move the best I can do is this and it goes like that.
This concept creates a tree of decision where its level of the tree "acommodates" MAX and MIN one after the other.
The algorithm distinguish two cases:

A) The parent node is MIN: We choose the child node with the minimum value

B)The parent node is MAX: We choose the child node with the maximum value

In order this algorithm to be effective the process shouldn't be exhaustive
since the algorithm will be dramatically slow. In reality we apply the Minmax algorithm
for a given depth(it reminds us the way that chess players think in front of 5 moves).
The time complexity of the above implementation is: O(b^d) where d is the depth of the tree and b is the mean branching factor
(the average children each node has) and the space complexity is O(b*d).