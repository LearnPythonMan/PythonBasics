test = [1,100,50,-51,1,1]

def find_even_index(arr):
    for p,x in enumerate(arr):
        if (p<=len(arr)):
            if sum(arr[:p]) == sum(arr[p+1:]):
                return p
    return -1

print(find_even_index(test))

# You are going to be given an array of integers. Your job is to take that array and find an index N where the sum of
# the integers to the left of N is equal to the sum of the integers to the right of N. If there is no index that
# would make this happen, return -1.

# Test.assert_equals(find_even_index([20,10,-80,10,10,15,35]),0)
# Test.assert_equals(find_even_index([10,-80,10,10,15,35,20]),6)
# Test.assert_equals(find_even_index(range(1,100)),-1)
# Test.assert_equals(find_even_index([0,0,0,0,0]),0,"Should pick the first index if more cases are valid")
