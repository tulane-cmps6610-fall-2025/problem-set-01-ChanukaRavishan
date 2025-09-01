"""
CMPS 6610  Assignment 1.

Chanuka Ravishan Algama

"""
# no imports needed.

def foo(a, b):

    if a ==0:
        return b
    elif b ==0:
        return a
    else:
        x, y = (min(a,b), max(a,b))
        return foo( y , y %x)


def longest_run(mylist, key):
    """
    mylist = list of integers
    key = integer to find longest run of
    return = the length of the longest run of key in mylist
    """
    no = 0
    max_no = 0

    for i in mylist:
        if i == key:
            no += 1
            if no > max_no:
                max_no = no
        else:
            no = 0

    return max_no


class Result:
    """ done """
    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size              # the length of the longest run on left side of input
                                                # eg, with a key of 12, [12 12 3] has left_size of 2 
        self.right_size = right_size            # length of longest run on right side of input
                                                # eg, key 12, [3 12 12] has right_size of 2
        self.longest_size = longest_size        # length of longest run in input
                                                # eg, [12 12 4 12 12 12]: longest_size is 3
        self.is_entire_range = is_entire_range  # True if the entire input matches the key
        
    def __repr__(self):
        return('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
              (self.longest_size, self.left_size, self.right_size, self.is_entire_range))
    
    
def longest_run_recursive(mylist, key):  
    """divide and conquer implementation"""

    """
    mylist = list of integers
    key = integer to find longest run of
    return = the length of the longest run of key in mylist
    """

    if len(mylist) == 0:
        return Result(0, 0, 0, False)
    if len(mylist) == 1:
        if mylist[0] == key:
            return Result(1, 1, 1, True)
        else:
            return Result(0, 0, 0, False)
    

    mid = len(mylist) // 2
    left = mylist[:mid]
    right = mylist[mid:]

     #Recursive part

    left_result = longest_run_recursive(left, key)
    right_result = longest_run_recursive(right, key)

    # for left 
    left_size_combined = left_result.left_size
    if left_result.is_entire_range and len(left) > 0:
        left_size_combined += right_result.left_size
    
    # for right
    right_size_combined = right_result.right_size
    if right_result.is_entire_range and len(right) > 0:
        right_size_combined += left_result.right_size
    
    midpoint = left_result.right_size + right_result.left_size

    longest_size = max(left_result.longest_size, right_result.longest_size, midpoint)
    is_entire_range_combined = left_result.is_entire_range and right_result.is_entire_range

    return Result(left_size_combined, right_size_combined, longest_size, is_entire_range_combined)


## Feel free to add your own tests here.
def test_longest_run():
    assert longest_run([2,12,12,8,12,12,12,0,12,1], 12) == 3


