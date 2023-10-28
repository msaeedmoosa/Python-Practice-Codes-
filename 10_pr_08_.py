def multiplication_table(number, limit):
    for i in range(1, limit + 1):
        print(f"{number} X {i} = {number * i}")


num = int(input("Enter the number: "))
limit = int(input("Enter the limit: "))
multiplication_table(num, limit)

