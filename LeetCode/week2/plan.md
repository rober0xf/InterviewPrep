# Week 2
This week It's about to use new techniques and do new problems.
The plan is to do one problem a day, and study each topic.

Week 2:
<br>
[x] Monday -> Valid Palindrome
<br>
[x] Tuesday -> Two Sum 2
<br>
[x] Wednesday -> 3Sum
<br>
[x] Thursday -> Best Time to Buy and Sell Stock
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

### 3Sum
Not a medium problem at all. It was very difficult to come up with a solution.
<br>
My first thought was to use a 3 nested loop solution, but it throws a time limit exceeded.
<br>
After that and some thinking, I came up with a solution that uses two pointers and sorting. It sorts an inner nums vector and checks if the sum of the current pivot and left and right pointers gives 0. If it does, then we store it in a vector and sort it to prevent duplicates. But this solution also throws up a time limit.
<br>
So after looking for solutions, the closest solution that I found was to use a set instead of a vector and sort each time.

### Best Time to Buy and Sell Stock
A pretty problem where we need to keep track of a condition where p1 > p2 always.
<br>
My first thought was to use two pointers in the normal way where l = 0, r = len(nums)-1. But after debugging, I realize that a better approach is to use two pointers but p1 = 0, p2 = p1+1.
<br>
And then check for profits and update the pointers correctly. It's important that if nums[p1] > nums[p2] we do p1 = p2, p2 += 1. We dont want do to p1 += 1. 
