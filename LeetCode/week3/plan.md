# Week 3
This week It's about learning and solving stack problems.
The plan is to do one problem a day.

Week 3:
<br>
[x] Monday -> Valid Parentheses
<br>
[x] Tuesday -> Min Stack
<br>
[] Wednesday -> Evaluate Reverse Polish Notation
<br>
[] Thursday -> Daily Temperatures
<br>
[] Friday -> Car Fleet

### Valid Parentheses
First stack problem, the hard part is to come with the idea of a map to check if the closing is the iteration char. If it is, then we check that the opening is the same kind with stack[-1] == map[c] and then pop. If not then its a different kind and we can return False immediately.

### Min Stack
A different kind of problem where we need to design a special type of stack. The important part is that we need to return the min value in O(1). It would be easy returning it in O(n) time just looping.
<br>
Archieving in constant time we need to associate each value with the min value at that point, for example:
<br>
[4, 3, 5, 1, 6] -> [(4,4), (3,3), (5,3), (1,1), (6,1)] 

### Evaluate Reverse Polish Notation
Similar problem that valid parentheses. 
<br>
We loop the input array until the value is an operand, if not we append it to a stack.
<br>
If its an operand then we pop the last 2 elements of the stack and do the operation, then append that result to the same stack.
