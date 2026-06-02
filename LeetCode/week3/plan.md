# Week 3
This week It's about learning and solving stack problems.
The plan is to do one problem a day.

Week 3:
<br>
[x] Monday -> Valid Parentheses
<br>
[] Tuesday -> Min Stack
<br>
[] Wednesday -> Evaluate Reverse Polish Notation
<br>
[] Thursday -> Daily Temperatures
<br>
[] Friday -> Car Fleet

### Valid Parentheses
First stack problem, the hard part is to come with the idea of a map to check if the closing is the iteration char. If it is, then we check that the opening is the same kind with stack[-1] == map[c] and then pop. If not then its a different kind and we can return False immediately.
