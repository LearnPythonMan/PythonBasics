#So there is a lot of math here
# Sources:
#  https://mitpress.mit.edu/sites/default/files/sicp/full-text/book/book-Z-H-11.html#%_sec_1.2.4
# https://en.wikipedia.org/wiki/Canonical_coordinates

def fib(n):
    a = q = 1
    b = p = 0
    n -= 1
    while (n != 0):
        if n%2  == 0:
            p, q = p*p+q*q, (2*p+q)*q
            n /= 2
        else:
            a, b = b*q+a*q+a*p, b*p+a*q
            n -= 1
    return a

# def fib(n):
#   return fibiter(1,0,0,1,n)
#
# def fibiter(a,b,p,q,count):
#     if count == 0:
#         return b
#     elif count%2 == 0:
#         return fibiter(a,
#                 b,
#                 p * p + q * q,
#                 (2 * p + q) * q,
#                 count/2
#                 )
#     else:
#         return fibiter(
#             b*q+a*q+a*p,
#             b*p+a*q,
#             p,
#             q,
#             count-1
#         )

print(fib(2000000))