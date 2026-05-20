# Week 1
This week It's about to get used to leetcode again.
I will start doing array and hashmap problems, easy ones.
The plan is to do one problem a day, and study each topic.

Week 1:
<br>
[x] Monday -> Two Sum
<br>
[x] Tuesday -> Contains Duplicate
<br>
[x] Wednesday -> Valid Anagram
<br>
[] Thursday -> Group Anagrams
<br>
[] Friday -> Top K Frequent Elements

### Two sum
Simple problem if you go for the brute force approach, we could just have two nested loops and check for the target.
<br>
For the optimal approach, we can use a hashmap to store the needed value for the current index, we do this every iteration.
<br>
We calculate the needed value as `needed = target - nums[i]`. If that value is in the map we just return its index and the current iteration index.
<br>
For the example input the map would look like: `{2: 0, 7: 1, 11: 2, 15: 3}`. value -> index.

### Contains Duplicate
In this case the easiest solution is the simpler one.
<br>
We create a hashset to store the check if the current number in the loop is already in the set, if it is then we just return True. If not we add it to the set.

### Valid Anagram
Another case where the easiest solution is the simpler one.
<br>
The thing that makes the solution easy its that a anagram just counts the counter, not that the order of the letters, for example abc and bac are anagram. It does not require to be cba.
<br>
We create two hashmap for each string, and store its count.
