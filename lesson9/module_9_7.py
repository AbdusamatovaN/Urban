def is_prime(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        for i in range(2, res):
            if res % i == 0:
                print('Составное')
                return res
        print('Простое')
        return res
    return wrapper

@is_prime
def sum_three(a, b, c):
    return a + b + c

result = sum_three(2, 3, 6)
print(result)
result = sum_three(3, 4, 5)
print(result)