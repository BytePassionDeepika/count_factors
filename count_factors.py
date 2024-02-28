def count_factors(num):
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1
    return count

user_input = int(input("Enter an integer: "))

result = count_factors(user_input)
print(f"The number of factors for {user_input} is: {result}")
