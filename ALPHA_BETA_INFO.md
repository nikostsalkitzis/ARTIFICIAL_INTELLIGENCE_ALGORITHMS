This algorithm is a variation of the MinMax algorithm in which we try to 
cut the branches of the decision tree if they serve a given condition.
To do so we initialize two variables a,b which are the "code synonyms" of max and min analogically.
The initialization of these is set to the smallest and greatest value for a and b proportionally.
In C we could have set them to MAX_INT and MIN_INT(including the limits library) but in Python we use just a huge and a tiny number.
Then, we traverse the tree of decisions for the game with the inorder technique and we transfer the values of a,b in each node.
If the current level of the tree is max then only a changes and if it is min only b changes.
A subtree is pruned when the condition a>=b is set.