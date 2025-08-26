### 迭代器与生成器
#### 迭代器
- 迭代器（Iterator）可以隐式地表示顺序数据。
- 在python中，它们用作访问不同容器中的元素的一种方式。
- `iter()` 函数可以将容器转换为迭代器, 而 `next()` 函数可以获取迭代器的下一个元素。
  - eg. 
  ```python
    my_list = [1, 2, 3]
    my_iter = iter(my_list)
    print(next(my_iter))  # 1
    print(next(my_iter))  # 2
    ```
- 迭代器只能用于一次性访问容器中的元素，不能对其进行修改。
- list()可以列出迭代器的剩余内容，并将其转换为list,但list()只能调用一次，之后迭代器失效。
##### 字典遍历  
```python
my_dict = {'a': 1, 'b': 2, 'c': 3}
k = iter(my_dict.keys())#或iter(my_dict),可以获取键的迭代
v = iter(my_dict.values())#可以获取值的迭代
i = iter(my_dict.items())#可以获取键值对的迭代
print(next(k))#a
print(next(v))#1
print(next(i))#('a', 1)
```
- 迭代器失效：如果改变了字典的大小，所有创建的迭代器失效。
##### for循环与迭代器
- for 循环可以遍历迭代器，并自动调用 `next()` 函数获取下一个元素,但只能有效遍历一次。
```python
my_list = [1, 2, 3]
my_iter = iter(my_list)
for i in my_iter:
    print(i)
# 1
# 2
# 3
for i in my_iter:
    print(i)
#
# 迭代器已经失效，不能再使用了。
```
##### 返回迭代器的函数
- 一些函数返回迭代器，可以用for循环来遍历它们,也可以通过list()、tuple()、sorted()等函数将其转换为列表或元组。
eg:
- `map(func, iterable)`应用函数func到序列iterable的每个元素。
- `filter(func, iterable)`过滤序列iterable中满足func的元素。
- `zip(iterable1, iterable2, ...)`将多个序列组合成一个序列，返回一个迭代器。
- `reversed(iterable)`返回一个迭代器，其元素顺序与iterable相反。
- 以map()为例，由于迭代器的惰性求值特性，只有在请求下一个元素时，才会调用函数func。
###### zip()函数
- zip()函数可以将多个序列组合成一个序列，并将相应位置的元素组合成元组。
- 如果序列长度不同，则返回长度最短的序列。
eg:
```python
a = [1, 2, 3]
b = [4, 5, 6, 7]
c = [8, 9]
zipped = zip(a, b, c)
print(list(zipped))
# [(1, 4, 8), (2, 5, 9)]
```
#### 生成器
- 生成器（Generator）是一种特殊的迭代器，它可以生成一系列值，但不必一次性生成所有值。
- 生成器函数使用yield语句来返回值，而不是直接用return返回值。
eg:
```python
def even_numbers(start, end):
    even = start + (start % 2)
    while even <= end:
        yield even
        even += 2
t = even_numbers(1, 10)
print(next(t))  # 2
print(next(t))  # 4
list(t)  # [6, 8, 10]
```
- 生成器函数在每次调用next()时，都会返回yield语句后面的值，直到函数结束。
- yield from 可以将生成器函数的输出直接传递给另一个生成器函数。
eg:
```python
def count_down(n):
    if n>0:
        yield n
        yield from count_down(n-1)
t = count_down(5)
print(list(t))  # [5, 4, 3, 2, 1]
```
- 善用yield可以让函数的逻辑更加清晰，更容易理解。
  - eg: partition(n,m)的实现，将n划分成多份，每份的大小不大于m，列出所有可能的划分方法。 
```python
def partition(n, m):
    if n<0 or m==0:
        return []
    else:
        exact_match=[]
        if n==m:
            exact_match=[str(m)]
        with_m = [p + '+' + str(m) for p in partition(n-m, m)]
        without_m=partition(n, m-1)
        return exact_match + with_m + without_m
for p in partition(6, 4):
    print(p)
    # 2+4
    # 1+1+4
    # 3+3
    # 1+2+3
    # 1+1+1+3
    # 2+2+2
    # 1+1+2+2
    # 1+1+1+1+2
    # 1+1+1+1+1+1
```
- 用生成器函数实现较为简化,且它可以避免创建大量的中间数据，例如partition(60,50)会生成9663870种情况，而生成器只生成需要的情况。
```python
def partition(n, m):
    if n>0 and m>0:
        if n==m:
            yield str(m)
        for p in partition(n-m, m):
            yield str(m) + '+' + p
        yield from partition(n, m-1)
for p in partition(6, 4):
    print(p)
```