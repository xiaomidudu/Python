def total(initial=5, *numbers, **keywords):  #定义一个带*的参数，像 *numbers 时,从那一点后所有的参数被收集为一 个叫做 ’numbers’ 的列表
    count = initial
    for number in numbers:
        count += number
    for key in keywords:  #当我们定义一个带两个星的参数,像 **keywords 时,从那一点开始的 所有的关键字参数会被收集为一个叫做 ’keywords’ 的字典
        count += keywords[key]
    return count
print(total(10, 1, 2, 3, vegetables=50, fruits=100))