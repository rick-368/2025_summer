# 类
## 自建类
- 在Python中，我们可以定义自己的类，来表示我们需要的数据结构。
- 一个类语句以`class`关键字开始，后面跟着类的名称，然后是类的属性和方法。
- `__init__`方法是类的构造函数，它会在类的实例化时自动调用。
- self参数是类的实例变量，它代表类的当前实例。

eg:
```python
class Account:
    interest_rate = 0.02
    def __init__(self, account_holder):
        self.account_holder = account_holder
        self.balance = 0
    def deposit(self, amount):
        self.balance += amount
        return self.balance
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return self.balance
        else:
            return "Insufficient balance"
```
- 类属性在类中定义，可以被所有实例共享。
```python
a = Account("Alice")
b = Account("Bob")
print(a.interest_rate) # 0.02
print(b.interest_rate) # 0.02
```
- 实例的属性和类的属性不一定必须要在构建类时声明，可以随时引入或改变。若实例属性与类属性同名，则实例属性会覆盖类属性。
```python
a = Account("Alice")
b = Account("Bob")
a.backup = b
print(a.backup.account_holder) # Bob
a.interest_rate = 0.03
print(a.interest_rate) # 0.03
print(b.interest_rate) # 0.02
Account.interest_rate = 0.04
print(a.interest_rate) # 0.03
print(b.interest_rate) # 0.04

```
- is/is not运算符用来比较两个表达式是否是同一个对象。
```python
a = Account("Alice")
b = Account("Bob")
c = a
print(a is b) # False
print(a is c) # True
```
## 继承
- `class SubClass(ParentClass):`通过此类语句创建的子类可以继承父类的属性和方法，也可以添加自己的属性和方法，或者覆盖父类的方法。
```python
class CheckingAccount(Account):
    interest_rate = 0.01
    withdraw_fee = 1
    def with_draw(self, amount):
        return Account.withdraw(self, amount + self.withdraw_fee)
```
- 多重继承：`class SubClass(Parent1, Parent2, Parent3):`，当父类有同名属性或方法时，子类会继承第一个父类中的属性或方法。
## 链表类
- 在python中，链表是通过创建类来实现的
```python
class Link:
    empty=()
    def __init__(self, data, next=empty):
        assert next is Link.empty or isinstance(next, Link)
        self.data = data
        self.next = next
>>> l1 = Link(1, Link(2, Link(3)))
>>> l1.data
1
>>> l1.next.data
2
>>> l1.next.next.data
3
```
- Link类有两个属性，data和next。data表示数据，next表示下一个节点的地址。
- 其他的操作，比如插入、删除、查找等，都可以通过修改next指针来实现。
- 链表的插入操作：
```python
# 按升序插入链表
def add(s,v):
    assert s is not Link.empty
    if s.data>=v:
        s.data,s.rest=v,Link(s.data,s.rest)
    elif s.data<v and empty(s.rest):
        s.rest=Link(v)
    elif s.data<v:
        add(s.rest,v)
```
## 树类
- 树也可以用类来实现。
```python
class Tree:
    def __init__(self,label,branches=[]):
        self.label=label
        for branch in branches:
            assert isinstance(branch,Tree)
        self.branches=list(branches)
```
- 在类中可以定义树的属性，比如打印的方法等等。
---

## 字符串转换
- Python 规定所有的对象都应该生成两个不同的字符串表示：一种是人类可读的文本，另一种是 Python 可解释的表示式。字符串的构造函数，即 str，返回一个人类可读的字符串,即调用print函数时看到的字符串。如果可能，repr 函数返回一个 Python 可解释的表达式，该表达式的求值结果与原对象相同。
- 对于表达式的值调用 repr 的结果就是 Python 在交互式会话中所打印的内容。
```python
>>> x = 12e6
>>> str(x)
'1.2e+7'
>>> repr(x)
'12000000.0'

>>> from fractions import Fraction
>>> half = Fraction(1, 2)
>>> str(half)
'1/2'
>>> repr(half)
'Fraction(1, 2)'

>>>s='hello world'
>>> str(s)
'hello world'
>>> repr(s)
"'hello world'"
>>> print(s)
hello world
>>> print(repr(s))
'hello world'
```
- 在一些情况下，不存在对原始值的字符串表示时，Python 通常生成一个被尖括号包围的描述。
```python
>>> repr(min)
'<built-in function min>'
```
- eval()函数是一个评估函数，它接受一个字符串作为输入，并返回一个 Python 对象。
```python
>>> eval('12e6')
12000000.0
>>> eval('Fraction(1, 2)')
Fraction(1, 2)
>>> eval("'hello world'")
'hello world'
```
- repr()与str()函数的本质：它们分别调用了零参数方法`__repr__()`和`__str__()`，如果在相应的类中没有`__str__()`方法，则返回调用`__repr__()`方法的结果。
底层逻辑：
```python
def repr(obj):
    return type(obj).__repr__(obj) 
    # 忽略obj的实例属性，调用类上的__repr__方法
```
```python
>>> half.__repr__()
'Fraction(1, 2)'
>>> half.__str__()
'1/2'
```
## 字符串插值
- f-string 是Python的一种字符串插值方式。它允许在字符串中嵌入变量，并在运行时计算它们的值。
- 语法：`f"string {expression} string"`
---
## 类的特殊方法
- 以双下划线开头和结尾的方法，它们是Python的内置函数，与内置的对象系统进行交互。
    - `__init__()`方法，它在对象被创建时被调用。
    - `__repr__()`方法，它返回一个字符串，该字符串可以被用作该对象的表示式,在交互式环境显示其值的时候自动调用。
    - `__str__()`方法，它返回一个字符串，该字符串可以被用作该对象的文本表示,在打印时自动调用。
    - `__add__()`方法，它定义了两个对象之间的加法运算，obj1 + obj2调用该方法。
    - `__bool__()`方法，它定义了对象在布尔上下文中的行为，bool(obj)调用该方法。
    - `__float__()`方法，它尝试将对象转换为浮点数。
    - `__radd__()`方法，它定义了两个对象之间的反向加法运算。
-  以分数类为例：
```python
class Ratio:
    def __init__(self, n, d):
        self.num = n
        self.den = d

    def __repr__(self):
        return 'Ratio({0}, {1})'.format(self.num, self.den)
    def __str__(self):
        return '{0}/{1}'.format(self.num, self.den)

    def __add__(self, other):
        # 类型分派：根据参数类型调用不同的方法
        if isinstance(other,int):
            n = self.num + self.den * other
            d = self.den
        elif isinstance(other,Ratio):
            n = self.num * other.den + self.den * other.num
            d = self.den * other.den
            g = gcd(n, d)
        elif isinstance(other,float):
            return float(self) + other
        return Ratio(n // g, d // g)
    __radd__ = __add__
    def gcd(n,d):
        while n !=d:
            n,d=min(n,d),abs(n-d)
        return n
    def __float__(self):#类型强制转换
        return self.num/self.den

>>> Ratio(1,2)+Ratio(3,4)
Ratio(7, 4)
>>> Ratio(1,2)+3
Ratio(5, 2)
>>> 1+Ratio(1,2)
Ratio(3, 2)
>>> 0.5+Ratio(1,2)
1.5
```
- 在上例中，展现了不同类进行交互的两种策略：类型分派和类型强制转换。