# n! = 1 * 3 * 2 * 4..... * n
# n! = [1 * 3 * 2 * 4..... n-1] * n
# n! = n * (n-1)!


# product = 1
# for i in range(n):
#     product = product * (i + 1)
# print(product)

def factorial_iter(n):
    product = 1
    for i in range(n):
        product = product * (i + 1)
    return product

f = factorial_iter(5)
print(f)