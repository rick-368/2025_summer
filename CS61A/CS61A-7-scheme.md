### Scheme 基础
- Scheme程序由表达式构成，表达式可以是基本表达式，也可以是组合表达式。
- 基本表达式包括：数字、字符串、布尔值、变量、过程调用。
- 组合表达式包括：函数定义、条件表达式、赋值语句、序列表达式。
- 调用表达式的语法形式为：(proc arg1 arg2...)，其中proc是过程名，arg1, arg2...是过程参数，调用表达式可以跨越多行。
``` scheme
> (quotient 10 3)
3

> (quotient(+ 8 7) 5)
3

> (+ (* 3
        (+ (* 2 4)
           (+ 3 5)))
     (+ (- 10 7)
        6))
57

> (number? 123)
#t

> (zero? 1)
#f

>(integer? 3.14)
#f
```
- 常用表达式
  - `if`：条件表达式，语法为`(if test consequent alternative)`，当test为真时，返回consequent，否则返回alternative,仅用于两个分支的条件判断，多个分支的情况可以使用`cond`。
  - `and`：逻辑与，语法为`(and exp1 exp2...)`，当所有exp都为真时返回#t，否则返回#f。
  - `or`：逻辑或，语法为`(or exp1 exp2...)`，当任意exp为真时返回#t，否则返回#f。
  - `define`：定义变量，语法为`(define var exp)`，将exp的值赋给var,也可以用于函数定义，语法为`(define (proc arg1 arg2...) body)`，将body作为proc的定义体，可以有多个表达式，返回最后一个表达式的值，参数为arg1, arg2...。

   ``` scheme
   > (define (square x) (* x x))
   > (square 5)
   25

   ```
   - 在scheme中也支持函数的嵌套和递归定义
   ``` scheme
   >(define(sqrt x)
     (define(update guess)
       (if (= (square guess) x)
           guess
           (update (average guess (/ x guess))))))
   > (sqrt 25)
   5
   ```
  - `lambda`：定义匿名函数，语法为`(lambda (var1 var2...) body)`，返回一个函数，参数为var1, var2...，函数体为body。
  ``` scheme
  >(define (square x) lambda (x) (* x x))
  > (square 5)
  25
  ```
  - `cond`：条件语句，语法为`(cond (test1 exp1) (test2 exp2) ... (else expn))`，当test1为真时，执行exp1，否则判断test2，直到找到真值，执行对应的exp。如果没有真值，则执行else。
  - `begin`：多表达式语句，语法为`(begin exp1 exp2...)`，将多个表达式组成一个表达式，返回最后一个表达式的值。
  ``` scheme
  > (begin (print "Hello") (print "World"))
  Hello
  World
  ```
  - `let`：局部变量绑定，语法为`(let ((var1 exp1) (var2 exp2) ...) body)`，将var1, var2...绑定到exp1, exp2...的值，在body中使用var1, var2...。
  ``` scheme
  > (define c (let((a 3)
              (b 4)
              (+ a b))))
  > c 
  7
  ```
  > 在本例中，a和b是局部变量，在let表达式中绑定到3和4，在body中使用+运算符将a和b相加，得到7，赋值给c。
  - `repeat`：重复执行表达式，语法为`(repeat n exp)`，重复执行n次exp。
#### Scheme 列表
- 在Scheme中，每个列表都有一个链表的形式，每个元素都是一个值，每个元素都有指针指向下一个元素。
- 形式：`cons(car, cdr)`，其中car是列表的第一个元素，cdr是列表的剩余元素。
- `car`：返回列表的第一个元素。
- `cdr`：返回列表的剩余元素。
- `nil`：空列表，表示列表的结束。
- `list?`：判断是否为列表.
- `null?`：判断是否为空列表。
``` scheme
> (cons 1 (cons 2 (cons 3 nil)))
(1 2 3)
> (define x (cons 1 (cons 2 (cons 3 nil))))
> (car x)
1
> (cdr x)
(2 3)
```
- 可以直接使用`list`构造列表，语法为`(list elem1 elem2...)`，返回一个包含elem1, elem2...的列表。
``` scheme
> (list 1 2 3)
(1 2 3)
```
- `append`：将两个列表连接成一个列表，语法为`(append list1 list2)`，返回一个包含list1和list2所有元素的列表。
- `map`：对列表中的每个元素进行操作，语法为`(map proc list)`，返回一个包含proc对list中每个元素的结果的列表。
- `filter`：对列表中的每个元素进行判断，返回满足判断条件的元素组成的列表，语法为`(filter proc list)`。
- `apply`：将proc应用于参数list，语法为`(apply proc list)`，返回proc(list)。
``` scheme
> (define x (list 1 2))
> (append x x)
(1 2 1 2)
> (map even? s)
(#f #t)
> (filter odd? s)
(1)
> (apply + (list 1 2 3))
6
```
#### 引用
- Scheme中可以用quote来引用特殊的表达式，语法为`(quote exp)`，返回exp的形式，不求值。
``` scheme
> (list 1 (quote a))
(1 a)
```
- 也可以用前缀'来引用表达式，语法为`'exp`，返回exp的形式。
``` scheme
> (list 1 'a)
(1 a)
> '(1,a)
(1,a)
```
- eval函数可以求值表达式，语法为`(eval exp env)`, env为环境，返回exp的求值结果。
``` scheme
> (list '+ 1 2)
(+ 1 2)

> (eval (list'+ 1 2) '())
3
```
- 通过eval和quote，我们可以让函数返回表达式。
``` scheme
> (define (fact n)(if (zero? n) 1 (* n (fact (- n 1)))))
> (fact 5)
120
> (define(fact_expr n)
 (if (zero? n) 1 (list '* n (fact_expr (- n 1)))))
> (fact_expr 5)
(* 5 (* 4 (* 3 (* 2 1))))
> (eval (fact_expr 5) '())
120
```
#### 作用域
- 作用域分为两种：静态作用域和动态作用域。
- 静态作用域：在编译时确定，与函数定义、变量定义的环境相关。
- 动态作用域：在运行时确定，与函数调用，变量引用的环境相关。
- 大多数语言（如Java、C++）都采用静态作用域，而Scheme采用动态作用域。

``` scheme
> (define f (lambda (x)(+ x y)))
> (define g (lambda (x y) (f (+ x x))))
> (g 1 2)
4
```
``` python
def f(x):
    return x + y

def g(x, y):
    return f(x + x)

>>> g(1, 2)

······ #省略报错
NameError: name 'y' is not defined
```
#### 准引用
- 取消引用的语法为`(unquote exp)`，返回exp的求值结果，或使用,来指示取消引用。
- 准引用用`前缀表示，它与quote类似，但在取消引用时，会将表达式求值，并将求值结果作为引用的表达式，而quote将取消引用的表达式也一并引用。
``` scheme
> (define x 1)
>'(1 ,(+ x 2))
(1 unquote (+ x 2))
>`(1 ,(+ x 2))
(1 3)
```
- 准引用对生成scheme函数很有用，可以使函数返回表达式，包括新的函数。
``` scheme
> (define (make n) (lambda (d) (+ d n)))
> (make 3)
(lambda (d) (+ d n))
; 由于Scheme的动态作用域，函数make的n并没有在make函数定义时绑定。
> (define (make n) `(lambda (d) (+ d ,n)))
> (make 3)
(lambda (d) (+ d 3))
; 准引用可以解决这个问题。
```
``` scheme
;此例实现了一个while循环的求和函数，使用了准引用。
> (define (sum_while init-x cond add update-x)
  `(begin
    (define (f x total)
      (if ,cond
        (f ,update-x (+ total ,add))
        total))
        (f ,init-x 0)))
> (define result (sum_while 1 '(< (* x x) 50) 'x '(+ x 1)))
> result
(begin
  (define (f x total)
    (if (< (* x x) 50)
      (f (+ x 1) (+ total x))
      total))
  (f 1 0))
> (eval result '())
28 ; 1+2+3+4+5+6+7
```