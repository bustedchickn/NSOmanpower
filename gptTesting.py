import math
listm = []
# def baseconversion(k,b,l):
    
#     baseconversion(k//b,b,l)
#     if k<0:
#         return l.append(k%b)
    
# baseconversion(8,2,listm)
# print(listm)
k = 347
b = 6

# print([k//b**4%b,k//b**3%b,k//b**2%b,k//b%b,k%b])

def extended_euclidean(a, b):
    if b == 0:
        return a, 1, 0  # Base case: gcd(a, 0) = a, with x = 1, y = 0
    else:
        gcd, x1, y1 = extended_euclidean(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return gcd, x, y

# Example usage for GCD(255, 60)
a, b = 54, 61
gcd, x, y = extended_euclidean(a, b)

print(f"GCD({a}, {b}) = {gcd}")
print(f"Coefficients: x = {x}, y = {y}")
print(f"Verification: {a}({x}) + {b}({y}) = {gcd}")  # Should equal gcd


print("\n\n\n")

print(-23%54)

