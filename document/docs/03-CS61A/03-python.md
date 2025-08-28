# 序列
## python列表
- 列表是python中最常用的数据结构，它可以存储多个元素，每个元素可以是任意类型,包括列表。
- 列表的创建：
```python
my_list = [1,'string', True, [1, 2, 3]]
```
- 列表的索引从0开始
- len()函数可以获取列表的长度
- python中列表之间可以进行运算，比如可以进行拼接、重复、切片等操作
eg:
```python
my_list = [1, 2, 3]
my_list2 = [4, 5, 6]

# 列表拼接
my_list3 = my_list + my_list2
print(my_list3)  # [1, 2, 3, 4, 5, 6]

# 列表重复
my_list4 = my_list * 3
print(my_list4)  # [1, 2, 3, 1, 2, 3, 1, 2, 3]

# 列表切片
my_list5 = my_list[1:3]
print(my_list5)  # [2, 3]
# 切片可以省略起始值，表示从头开始；可以省略终止值，表示到末尾结束。
my_list6 = my_list[1:]
print(my_list6)  # [2, 3]
my_list7 = my_list[:2]
print(my_list7)  # [1, 2]
```

- in和not in可以用来判断元素是否在列表中
eg:
```python
my_list = [1, 2, 3]
print(2 in my_list)  # True
print(4 not in my_list)  # True
```
- pair
  - 列表可以表示一对数据`pair = [1,2]`
  - 可以对列表进行解包，得到两个元素`a, b = pair``a = 1` `b = 2`
  - eg.有理数的构建  
```python
      def build_rational(numerator, denominator):
          return [numerator, denominator]
      # 改进（将分数表示为其最简形式）
      def build_rational(numerator, denominator):
          divisor = gcd(numerator, denominator)
          return [numerator // divisor, denominator // divisor]
```
### 列表推导式
- 列表推导式可以根据条件创建列表。
- 语法：
```python
new_list = [expression for item in list if condition]
```
- 表达式：可以是任意表达式，可以是变量、函数调用等。
- 条件：可以是任意表达式，返回True或False。
- 示例：找出给定n的因数
```python
def divisors(n):
    return[1]+[i for i in range(2, n) if n % i == 0]
    print(divisors(10))  # [1, 2, 5, 10]
```
### 列表操作函数
- sum()函数可以求和，元素类型可以是数字、字符串、列表等。
  - 形式：sum(iterable, start=0)初始值可以省略，默认为0。
eg:
```python
print(sum([[1,2],[3,4],[5,6]], []))  # [1, 2, 3, 4, 5, 6]
print(sum([1, 2, 3, 4, 5]))  # 15
```
- max()函数可以求最大值，支持传入一个key函数，max会返回key函数返回最大值的元素。
eg:
```python
my_list = [1, 3, 2, 5, 4]
print(max(my_list, key=lambda x: 7-x))  # 1
``` 
- all()函数可以判断列表中的所有元素是否都为True，如果有一个元素为False，则返回False。
- sort()函数可以对列表进行排序，默认升序，可以传入一个key函数，排序时会使用key函数返回的值进行比较。
### 列表类方法
- append()方法可以向列表中添加一个元素。
- extend()方法可以将一个列表中的元素添加到另一个列表中。
- pop()方法可以删除并返回列表中的最后一个元素，默认删除最后一个元素。
- remove()方法可以删除列表中第一个匹配的元素。

---
## for循环
- 基本语法：
```python
for item in list:
    # do something with item
```
- 可以在for循环语句中直接进行序列解包，这只对固定长度序列的序列有效。
  eg:
```python
for a, b in [(1, 2), (3, 4), (5, 6)]:
    print(a, b)
```
## range序列
- range()函数可以生成一个整数序列，可以指定起始值、终止值、步长。
- range包含起始值，不包含终止值。
- 转换为列表：list()函数
  eg:
```python
my_range = range(1, 10, 2)
my_list = list(my_range)
print(my_list)  # [1, 3, 5, 7, 9]
```
- 步长可以为负数，表示逆序
- 步长可以省略，默认为1；起始值也可以省略，默认为0。
---
## 字符串
- 字符串是由零个或多个字符组成的序列，通常用单引号或双引号括起来（三引号的字符串可以跨越多行，换行也可以用\n表示）。字符串可以包含任意的 ASCII 字符，包括空格、数字、字母、符号等。
- 字符串可以看作是一种特殊的列表，每个元素都是字符。字符串的索引从 0 开始，可以用方括号 `[]` 来访问其中的元素。
- 在字符串中，in可以用来寻找连续的字母
  eg: 
  ```python
  s = "hello world"
  if "ll" in s:
      print("found it!") # output: found it!
  ```
---
## 字典
- 字典是一种无序的键值对集合，其中每个键值对由一个键和一个值组成。键必须是唯一的，不能为列表或字典，值可以是任意的 Python 对象。
- 形式: `dict = {key1: value1, key2: value2,...}`
- 字典查找：`value = dict[key]`
- 字典也是一个特殊的列表，其中每个元素都是键。
  ```python
  numerals = {'one': 1, 'two': 2, 'three': 3}
  print(list(numerals)) # output: ['one', 'two', 'three']
  ```
- .values() 方法可以用来获取字典中的所有值。
  ```python
  numerals = {'one': 1, 'two': 2, 'three': 3}
  print(numerals.values()) 
  # output: dict_values([1, 2, 3])
  ```
   - dict_values([1, 2, 3])不是列表，是特殊的序列类型，但sum，min，max等函数可以用，也可以用list()转换为列表。
  ```python
  print(list(numerals.values())) # output: [1, 2, 3]
  ```
### 字典推导式
- 形式：`{key_expression: value_expression for item in iterable if condition}`
- 示例：
  ```python
  numbers = [1, 2, 3, 4, 5]
  squares = {num: num**2 for num in numbers if num % 2 == 0}
  print(squares) # output: {2: 4, 4: 16}
  ```
---
## Python中树的构建
- 在python中，我们可以用列表来构建树。函数接受一个标签和一个分支列表作为参数，并返回一个树的根节点，树的每个节点是一个列表，第一个元素是标签，后面是分支列表。
```python
  def build_tree(label, branches=[]):
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [label]+branches

    def is_tree(tree):
        if type(tree)!= list or len(tree) < 1:
            return False
        for branch in branches(tree):
            if not is_tree(branch):
                return False
        return True

  def label(tree):
    return tree[0]

  def branches(tree):
    return tree[1:] 
  
```
- eg:斐波那契树的构建
```python
  def fib_tree(n):
    if n <= 1:
      return tree(n)
    else:
      left = fib_tree(n-1)
      right = fib_tree(n-2)
      return tree(label(left) + label(right), [left, right])
```
- 一些树递归函数
```python
  def is_leaf(tree):
    return not branches(tree)

  def print_tree(t):
    print(label(t))
    for b in branches(t):
      print_tree(b)
    # 当树为空时，branches(t)返回空列表，因此不会有循环
```
- 典型问题：
  - Count paths that have a total label sum 
``` python
  def count_paths(t, total):
    if label(t)==total:
      found = 1 #根节点自身作为路径
    else:
      found = 0
    return found + sum(count_paths(b, total-label(t)) for b in branches(t))
```
---
## 对象和类
- 对象代表信息，它包含数据和行为。具有特殊的属性和方法，可以通过点表达式访问。
- 类是对象的一种类型，它定义了对象的属性和方法。类可以实例化为对象，对象可以调用类的方法。
- eg: 字符串
  ```python
  s = "hello world"
  s.upper() # "HELLO WORLD"
  s.lower() # "hello world"
  ```
### 对象的变化
- **以字符串为例**
  - 可以直接通过索引修改元素，例如 `s[0] = 'H'`。
  - .pop() 删除并返回字符串中的最后一个字符。
  - .remove() 删除字符串中第一个出现的指定字符。
  - .append() 在字符串末尾添加字符。
  - .extend() 在字符串末尾添加多个字符,参数可以是字符串或列表。
- 字典也有类似性质
  - 可以直接通过键修改值，例如 `d['key'] = 'value'`。
  - 也可以通过键添加键值对，例如 `d['new_key'] = 'new_value'`。
  - .pop() 删除并返回字典中的键值对,如果没有指定键则删除最后一个键值对。
- 如果我将两个不同的名称绑定到同一个对象，那么修改其中一个，另一个也会受到影响。
  eg:
  ```python
  list1 = [1, 2, 3]
  list2 = list1
  list2.append(4)
  print(list1) # output: [1, 2, 3, 4]
  ```
- 只有可变对象才可以被修改，例如列表、字典、集合。不可变对象（如数字、字符串）一旦创建就不能被修改。
  
---
## 元组
- 元组是不可变的列表，可以用圆括号括起来，甚至可以不用括号，元素用逗号隔开。
- tuple()可以用来创建元组，可以接受列表、字符串、元组作为参数。
- 如果要创建只有一个元素的元组，必须在元素后面加一个逗号。
- 元组在某些性质上类似列表，例如可以用索引访问元素，可以用运算符+和*连接元组，可以用min、max、sum、in等函数。
- 不含列表的元组可以作为字典的键。
- 元组的内容并不是绝对不变的，比如可以更改元组内列表的元素。
---
## 可变对象和不可变对象
- 对于可变对象，如果修改了对象，则会影响到其他变量，例如：
  ```python
  a = [1, 2, 3]
  b = a
  b.append(4)
  print(a) # output: [1, 2, 3, 4]
  ```
- 对于不可变对象，如果修改了对象，则会创建新的对象，例如：
  ```python
  a = (1, 2, 3)
  b = a
  b = (1, 2, 3, 4)
  print(a) # output: (1, 2, 3)
  ```
- 身份运算符（is）可以用来判断两个变量是否指向同一个对象。
  ```python
  a = [1]
  b = [1]
  c = a
  print(a is b) # output: False
  print(a is c) # output: True
  ```
- 函数的默认参数占用同一块内存，因此如果在函数中修改了默认参数，则会影响到所有调用该函数的地方。
eg:
```python
def f(s=[]):
    s.append(3)
    return len(s)
  print(f()) # output: 1
  print(f()) # output: 2
  print(f()) # output: 3
```
---
## 可变函数
- 对于可变对象，函数的默认参数是引用传递，因此函数可以修改对象的值。
eg:
```python
 def make_withdraw(balance):
  b = [balance]
    def withdraw(amount):
      if amount > b[0]:
        return "Insufficient funds"
      b[0] -= amount
      return b[0]
    return withdraw

wd = make_withdraw(100)
print(wd(50)) # output: 50
print(wd(75)) # output: Insufficient funds
```