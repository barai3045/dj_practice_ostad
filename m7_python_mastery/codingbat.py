"""Logic-2 > make_bricks
prev  |  next  |  chance
We want to make a row of bricks that is goal inches long. We have a number of small bricks (1 inch each) and big bricks (5 inches each). Return True if it is possible to make the goal by choosing from the given bricks. This is a little harder than it looks and can be done without any loops. See also: Introduction to MakeBricks


make_bricks(3, 1, 8) → True
make_bricks(3, 1, 9) → False
make_bricks(3, 2, 10) → True"""


def make_bricks(small, big, goal):
    while goal >= 5 and big > 0:
        goal = goal - 5
        big = big - 1
        
    while goal >= 1 and small > 0:
        goal = goal - 1 
        small = small - 1
    
    if goal == 0:
      return True
    else: 
      return False
  
  
"""Logic-2 > lone_sum
prev  |  next  |  chance
Given 3 int values, a b c, return their sum. However, if one of the values is the same as another of the values, it does not count towards the sum.


lone_sum(1, 2, 3) → 6
lone_sum(3, 2, 3) → 2
lone_sum(3, 3, 3) → 0"""

def lone_sum(a, b, c):
    if a == b == c:
        return 0
    elif a == b:
        return c
    elif b==c:
        return a
    elif a==c:
        return b
    else:
        return a+b+c
    
    
"""Logic-2 > lucky_sum
prev  |  next  |  chance
Given 3 int values, a b c, return their sum. However, if one of the values is 13 then it does not count towards the sum and values to its right do not count. So for example, if b is 13, then both b and c do not count.


lucky_sum(1, 2, 3) → 6
lucky_sum(1, 2, 13) → 3
lucky_sum(1, 13, 3) → 1"""

def lucky_sum(a, b, c):
    if a == 13:
        return 0
    elif b ==13:
        return a
    elif c==13:
        return a+b
    else:
        return a+b+c
    
    

"""Given 3 int values, a b c, return their sum. However, if any of the values is a teen -- in the range 13..19 inclusive -- then that value counts as 0, except 15 and 16 do not count as a teens. Write a separate helper "def fix_teen(n):"that takes in an int value and returns that value fixed for the teen rule. In this way, you avoid repeating the teen code 3 times (i.e. "decomposition"). Define the helper below and at the same indent level as the main no_teen_sum().


no_teen_sum(1, 2, 3) → 6
no_teen_sum(2, 13, 1) → 3
no_teen_sum(2, 1, 14) → 3"""


def no_teen_sum(a, b, c):
    s = fix_teen(a) + fix_teen(b)+ fix_teen(c)

    return s
  
  
  

def fix_teen(n):
    if n in range(13,20,1) :
        if n == 15 or n == 16:
            return n
        else:
            return 0
    else:
        return n
    

"""Logic-2 > round_sum
prev  |  next  |  chance
For this problem, we'll round an int value up to the next multiple of 10 if its rightmost digit is 5 or more, so 15 rounds up to 20. Alternately, round down to the previous multiple of 10 if its rightmost digit is less than 5, so 12 rounds down to 10. Given 3 ints, a b c, return the sum of their rounded values. To avoid code repetition, write a separate helper "def round10(num):" and call it 3 times. Write the helper entirely below and at the same indent level as round_sum().


round_sum(16, 17, 18) → 60
round_sum(12, 13, 14) → 30
round_sum(6, 4, 4) → 10"""


def round_sum(a, b, c):
    return round10(a)+ round10(b) +round10(c)

def round10(n):
    div = n//10
    mod = n%10
    if mod >= 5:
        return div*10 + 10
    else:
        return div*10
    
    
"""Logic-2 > close_far
prev  |  next  |  chance
Given three ints, a b c, return True if one of b or c is "close" (differing from a by at most 1), while the other is "far", differing from both other values by 2 or more. Note: abs(num) computes the absolute value of a number.


close_far(1, 2, 10) → True
close_far(1, 2, 3) → False
close_far(4, 1, 3) → True"""