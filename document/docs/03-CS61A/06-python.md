# 效率提升与异常处理
## 效率
- 记忆化搜索：如果一个问题的解已经被计算过，则直接返回该解，避免重复计算。
```python
def memo(f):
    cache = {}
    def memoized(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]
    return memoized
def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
fib = memo(fib)
>>>fib(30)
832040
>>>fib(50)
12586269025
```
- 对问题的求解方式不同，有不同的算法效率。
```python
def exp(base, exp):# O(N)
    if exp == 0:
        return 1
    else:
        return base * exp(base, exp-1)
def exp_fast(base, exp):# O(logN)
    if exp == 0:
        return 1
    elif exp % 2 == 0:
        temp = exp_fast(base, exp//2)
        return temp * temp
    else:
        return base * exp_fast(base, exp-1)
```
## 模块化
- 代码模块化：将代码分成多个文件，每个文件只做一件事情，并提供一个接口。
- 接口：函数、类、模块等，只提供必要的功能，隐藏实现细节。
## 异常
- 异常处理：在程序运行过程中，如果出现异常，可以捕获异常并进行处理。
- 有很多内置异常类。
  - 常见异常类：
  - `TypeError`：传入参数类型错误。
  - `ValueError`：传入参数值错误。
  - `IndexError`：访问列表索引越界。
  - `KeyError`：访问字典键值不存在。
  - `NameError`：访问变量不存在。
- 可以用`raise`语句主动引出异常。
```python
def divide(a, b):
    if b == 0:
        raise ValueError("division by zero")
    return a / b

>>> divide(10, 0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 3, in divide
ValueError: division by zero
```
- 可以用`try...except`语句捕获异常,except后面可以加多个异常类型，捕获指定的异常,并执行相应的处理代码。
```python
>>> try:
        a = 1 / 0
    except ZeroDivisionError   as e:
        print("Error:", e)
        a = 0

Error: division by zero
>>> a
0
```