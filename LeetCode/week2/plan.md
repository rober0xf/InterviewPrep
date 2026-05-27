# Week 2
This week It's about to use new techniques and do new problems.
The plan is to do one problem a day, and study each topic.

Week 2:
<br>
[x] Monday -> Valid Palindrome
<br>
[x] Tuesday -> Two Sum 2
<br>
[] Wednesday -> 3Sum
<br>
[] Thursday -> Best Time to Buy and Sell Stock
<br>
[] Friday -> Longest Substring Without Repeating Characters

### Valid Palindrome
First two pointers problem, pretty straightforward solution. As usual we need to create a left and right pointers and iterate while they meet.
<br>
We could optimize it to make it O(1) Space, but I like this more.

### Two Sum 2
An improved idea of two sum, in this case we need to return it in base 10 order. And they are in increasing order.
<br>
Given that is in increasing order, my first thought was to use binary search. But we need to keep in mind that we need to find two values not one, so we use the first value as a pivot and do the search using a left and right pointer based of the pivot value.
<br>
We will end up using a while loop inside the for loop (our pivot).
<br>
This solution is n*log n because the binary search.
<br>
There is a better and simpler approach using two pointers, but my first thought was to use binary search.
