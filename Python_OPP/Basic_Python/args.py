def all_sum(*numbers):
    print(numbers)
    sum  = 0
    for num in numbers:
        print(num)
        sum = sum + num
    return sum 

total = all_sum(45, 46, 89, 11, 81, 5, 2, 7)
print('All Sum', total)