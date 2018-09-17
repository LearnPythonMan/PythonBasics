#My solution:
def valid_parentheses(string):
    p = 0
    for i in string:
       if i == '(':
           p+=1
       elif i == ')':
           p-=1
       if p<0:
           return False
    return p == 0


#Best:
# def valid_parentheses(string):
#     cnt = 0
#     for char in string:
#         if char == '(': cnt += 1
#         if char == ')': cnt -= 1
#         if cnt < 0: return False
#     return True if cnt == 0 else False

# Write a function called that takes a string of parentheses, and determines if the order of the parentheses is valid. The function should return true if the string is valid, and false if it's invalid.
#
# Examples
# "()"              =>  true
# ")(()))"          =>  false
# "("               =>  false
# "(())((()())())"  =>  truegi