# 递归
## 一个简单的例子

```python
def print_sums(x):
    print(x)
    def next_sum(y):
        return print_sums(x + y)
    return next_sum

print_sums(1)(3)(5)
```

输出：

```
1
4
9
```

## 递归函数
- 是一个主体直接或间接调用自身的函数。
eg:
```python
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
```
## 相互递归
- 一个函数调用另一个函数，而该函数又调用了它自己。
eg:
```python
def split(n):
    return n//10, n%10

def sum_digits(n):
    if n < 10:
        return n
    else:
        all_but_last, last = split(n)
        return sum_digits(all_but_last) + last
def luhn_sum(n):
    if n < 10:
        return n
    else:
        all_but_last, last = split(n)
        return luhn_sum_double(all_but_last) + last
def luhn_sum_double(n):
    all_but_last, last = split(n)
    luhn_digit = sum_digits(2*last)
    if n <10:
        return luhn_digit
    else:
        return luhn_sum(all_but_last) + luhn_digit
```
## 树状递归
- 一个函数调用自身多次，每次递归深度增加一层。
- 如斐波那契数列，阶乘，汉诺塔等。
eg：
- 斐波那契数列
```python
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
```
- Counting Partitions
```python
def count_partitions(n, k):
    if n == 0:
        return 1
    elif n < 0 or k < 0:
        return 0
    elif k == 0:
        return 0
    else:
        return count_partitions(n, k-1) + count_partitions(n-k, k)
```