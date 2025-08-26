### Python基础
#### 表达式
- 表达式描述一个计算并返回一个值。
- 表达式都可以用函数来表示。
- 表达式可以嵌套在其他表达式中。
- 表达式可以作为参数传递给函数。
- 表达式的构成：
    - 操作数，操作符（一般也是表达式）
#### 赋值
- 赋值运算符（=）用来将一个表达式的值赋给一个变量。
- 赋值运算符右边可以是一个表达式也可以是一个值，也可以是变量或函数的名称。
- 在帧中改变名称和值之间的绑定关系。
- 赋值语句的执行规则：
    - 如果右边是一个表达式，则先计算右边的表达式的值，再将其赋值给左边的变量。
- eg: 
```python
 x,y = 1,2
 f = max(x,y)
 ```
#### 创建函数
- 定义函数的语法：
```python
def 函数名(参数列表):
    函数体
```
#### 环境
- 环境框架（帧）是函数调用时创建的临时数据结构，用来存储函数的局部变量和参数。
- 环境有局部框架和全局框架，局部框架存储函数的局部变量，全局框架存储全局变量。
- 局部框架的作用域仅限于函数内部，当函数执行完毕后，局部框架就被销毁。
- 全局框架的作用域是全局的，所有的函数都可以访问全局变量。
---
- 一个名称在求值时，所处的环境帧决定了该名称的真正含义。
- 名称求解（Name Evaluation）：
    - 名称求解过程从当前环境开始，沿着环境链向上搜索，直到找到名称的定义。
    - 环境链的层次结构：当前环境 -> 父环境 -> 父环境的父环境 -> ... -> 全局环境
---
- 在不同的环境中，同一个名称可能有不同的含义。
- eg:
```python
def square(square):
    return square ** 2

print(square(3)) # 9
```
- 在上面的例子中，在square函数的环境帧中square作为参数存在，但在全局帧中，square作为一个函数存在。
- return将信息从本地帧带回首次调用该函数的环境帧。
- 不仅是变量，函数也是类似：
  - 每个用户定义的函数都有一个父框架，即包含函数定义的模块。
#### Print语句
- 打印语句用于输出表达式的值。
- 打印语句的语法：
```python
print(表达式1,表达式2,...)
```
- 打印语句的执行规则：
    - 首先计算所有表达式的值（包括函数调用）。
    - 然后将计算结果按照空格分隔的形式输出。
    - 打印语句的返回值是None。
- eg:
```python
print(print(1), print(2))

输出：
1 
2
None None
```
> **None**
None是Python中的一个特殊值，表示空值。
None可以作为任何数据类型的值，包括函数的返回值。
None可以用作条件表达式的结果。
- 打印语句是非纯函数。除了返回值外，调用一个非纯函数还会产生其他改变解释器和计算机的状态的副作用（side effect）。一个常见的副作用就是使用 print 函数产生（非返回值的）额外输出。
#### 控制语句
###### while循环
- while循环的语法：
```python
while 条件表达式:
    循环体
```
- while循环的执行规则：
    - 首先计算条件表达式的值。
    - 如果条件表达式的值为True，则执行循环体，并返回None。
    - 如果条件表达式的值为False，则退出循环。
###### for循环
- for循环的语法：
```python
for 变量 in 可迭代对象:
    循环体
```
- for循环的执行规则：
    - 首先将可迭代对象中的元素逐个赋值给变量。
    - 执行循环体，并返回None。
###### if语句
- if语句的语法：
```python
if 条件表达式1:
    语句1
elif 条件表达式2:
    语句2
else:
    语句3
```
- if语句的执行规则：
    - 首先计算条件表达式1的值。
    - 如果条件表达式1的值为True，则执行语句1，并返回None。
    - 如果条件表达式1的值为False，则计算条件表达式2的值。
    - 如果条件表达式2的值为True，则执行语句2，并返回None。
    - 如果条件表达式2的值为False，则执行语句3，并返回None。
###### 逻辑运算符
- and/or运算符：
    - 短路求值：
        - 如果and左边的表达式的值为False，则右边的表达式不会被求值。
        - 如果or左边的表达式的值为True，则右边的表达式不会被求值。
###### 断言语句assert
- assert语句的语法：
```python
assert 条件表达式, 错误消息
```
- 如果条件表达式的值为False，则抛出AssertionError异常，并附带错误消息。
- 断言语句用于在程序运行时检查一些条件是否满足，以便于调试。
#### 高阶函数
- 高阶函数是指接受函数作为参数或者返回函数的函数。
eg:
```python
def add(x, y, f):
    return f(x) + f(y)
```
- python中函数支持嵌套定义，可以将函数作为参数传递给另一个函数。
  eg:
```python
def make_adder(n):
    def adder(x):
        return x + n
    return adder

add_three = make_adder(3)
print(add_three(4)) # 7
```
  - make_adder函数接受一个参数n，返回一个函数adder，adder函数接受一个参数x，返回x+n。
  - add_three = make_adder(3)将make_adder(3)的返回值赋值给add_three。
#### lambda表达式
- lambda表达式是一种简化的函数定义方式。
- lambda表达式的语法：
```python
lambda 参数列表: 表达式
```
eg:
```python
add = lambda x, y: x + y
print(add(2, 3)) # 5
```
- lambda表达式只能用于一行函数，不能包含多条语句。
- lambda表达式不能包含赋值语句、条件语句、循环语句、打印语句等。
- def语句会赋予函数一个名称，lambda表达式不会。
#### 函数柯里化
- 函数柯里化（Currying）是将多参数函数转换为一系列单参数函数的过程。
- 一个函数柯里化的例子：
```python
def curry(f):
    def g(x):
        def h(y):
            return f(x, y)
        return h
    return g
```
- curry函数接受一个接受两个参数的函数f作为参数，返回一个函数g， g函数接受一个参数x，返回一个函数h，h函数接受一个参数y，返回f(x,y)。
#### 递归
###### 一个简单的例子

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

##### 递归函数
- 是一个主体直接或间接调用自身的函数。
eg:
```python
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
```
##### 相互递归
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
##### 树状递归
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
-Counting Partitions
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