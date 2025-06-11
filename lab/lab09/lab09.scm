(define (over-or-under num1 num2) 
  (cond 
    ((< num1 num2) -1)
    ((= num1 num2) 0)
    (else
      1))
)

(define (make-adder num) 
  (lambda (inc) (+ inc num))
)

(define (composed f g) 
  (lambda (x) (f (g x))) ;f(g(x))
)

(define (repeat f n) 
  (if (= n 0)
    (lambda (x) x) ; 条件为真时执行的单个表达式
    (composed f (repeat f (- n 1))) ; 条件为假时执行的单个表达式
  ); 如果需要在条件分支中执行多条操作，使用 begin 表达式
)

(define (max a b)
  (if (> a b)
      a
      b))

(define (min a b)
  (if (> a b)
      b
      a))

(define (gcd a b) 
  (if (= b 0)
    a
    (gcd b (modulo a b))
  )
)


;return b == 0 ? a : gcd(b,a%b);
; cons 创建链表的双参数程序
; car 返回列表第一个元素
; adr 返回链表其余部分
; nil 计算结果为空链表

; > (cons 1 (cons 2 nil))
;;;(define a 1)
;;;(define x (cons 1 (cons 2 nil)))
x       ; (1, 2)
;;;(car x) ; 1
;;;(cdr x) ; (2)
;;;(define y '(1, 2)) ;引号 ' 告诉 Scheme 这是数据，不是函数调用
; (cons 'a nil) == (cons (quote a) nil)
;;;(define s (cons 1 (cons 2 nil)))
;s -> (1, 2)
;;;(append s s) ; (1, 2, 1, 2)
;;;(list s s) ; ((1 2) (1 2))

;;;(map even? s) ; (#f #t)
;;;(map (lambda (x) (*2 x)) s) ; (2 4)

;;;(filter even? s) ; (2)
;;;(filter even '(5 6 7 8 9)) ; (6 8)
;;;(filter list? '(5 (6 7) 8 (9))) ; ((6 7) 9)
;;;(map (lambda (s) (cons 5 s)) (filter list? '(5 (6 7) 8 (9)))) ; ((5 6 7) (5 9))

;;;(apply quotient '(10 5)) ; 2
;;;(apply + '(1 2 3 4))
(define (f x total)
  (if (< x 10)
    (f (+ x 2) (+ total (* x x)))
    total
  )
)
(f 2 0)
