#### 函数式编程
- 所有函数都是纯函数，它们只接受输入并返回输出，不产生副作用。
- 无重新赋值的函数和变量。
- 无可变数据类型。
- 创建的名称-值绑定是不可变的。
- 优势：
   - 表达式的值与子表达式的值的计算顺序无关，因此可以并行计算。
   - 引用透明性：函数的输出只取决于输入，因此可以将函数的结果传递给其他函数。
#### 尾递归
- 尾递归是指函数的最后一个操作是递归调用，即尾调用。
- 尾调用即尾位置（即函数的最后一步操作）的调用表达式，例如在scheme语言中:
   - lamba表达式最后一个主表达式
   - 在尾位置的if表达式中的结果和替代项表达式
   - 在尾位置cond表达式中的每个条件表达式
   - 在尾位置and/or表达式的最后一个子表达式
   - 在尾位置begin表达式的最后一个子表达式
> 注：如果在尾位置的表达式中的调用表达式仍需要做进一步计算，则其不是尾调用。
> 注：线性递归过程也可以转换为尾递归过程。
```scheme
; 线性递归
(define (factorial n)
  (if (= n 0)
      1
      (* n (factorial (- n 1)))))

; 尾递归
(define (factorial n k)
  (if (= n 0)
      k
      (factorial (- n 1) (* n k))))
```
- scheme 语言的尾调用优化可以提高效率，因为它可以避免创建新的栈帧，节省内存。
#### 宏
- 宏执行代码转换，类似于编译器的预处理，是在程序源代码被编译前进行的操作。
- 定义宏：`define-macro (name formals) body`它接受一个形式参数列表和一个表达式，并返回一个宏。
- 宏接受一个表达式作为参数，并返回一个表达式。
- 在使用宏时，首先调用宏过程，而不是先评估接受到的参数，然后将宏的结果作为表达式求值。
```scheme
> (define-macro (twice expr)(list 'begin expr expr))
twice
> (twice (print "hello"))
"hello"
"hello"
; 在普通的define中，print语句会提前评估。
> (define (twice expr) (list 'begin expr expr))
twice
> (twice (print "hello"))
"hello"
(begin None None)
; 一个解决方法是使用延迟求值，即利用引用
> (eval (twice '(print "hello")))
"hello"
"hello"

```
- 实例：追踪函数调用
```scheme
(define-macro (trace expr)
   (define operator (car expr))
`(begin
   (define original ,operator)
   (define ,operator (lambda (n)
                        (print (list ,operater n))
                        (original n)))
   (define result ,expr)
   (define ,operator original)
   result))
```