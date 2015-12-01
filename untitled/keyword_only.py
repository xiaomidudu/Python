def total(initial=5, *numbers, vegetables):  #指定特定的关键参数为 keyword-only 而不是位置参数,可以在带星的参数后申明
    count = initial
    for number in numbers:
        count += number
    count += vegetables
    return count

print(total(10, 1, 2, 3, vegetables=50))
print(total(10, 1, 2, 3,))