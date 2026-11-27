def fizzbuzz(n):
    result = []
    for x in range(1, n+1):
        if x%15==0:
            result.append("FizzBuzz")
        elif x%3==0:
            result.append("Fizz")
        elif x%5==0:
            result.append("Buzz")
        else:
            result.append(x)
    return result

print(fizzbuzz(15))
