(define (square n) (* n n))

(define (pow base exp)              ; 函数定义
  (cond                             ; 条件表达式开始
    ((= exp 0) 1)                   ; 情况1
    ((even? exp)                    ; 如果指数是偶数
     (square (pow base (/ exp 2)))) ; 使用 x^(2y) = (x^y)^2(将底数平方)
    (else                           ; 情况3
     (* base (pow base (- exp 1)))))); x^(2y+1) = x * x^(2y)

(define (repeatedly-cube n x)
  (if (zero? n)
      x
      (let ((y (repeatedly-cube (- n 1) x)))
        (* y y y))))

(define (cddr s) (cdr (cdr s)))

(define (cadr s) (car (cdr s)))

(define (caddr s) (car (cddr s)))

(cond ((> x 10) (print 'big))
      ((> x 5) (print 'medium))
      (else (print 'small)))
;两种实现的对应关系
;            递归版本	                   迭代版本	        数学含义
;(square (pow base (/ exp 2)))	a = a * a; b >>= 1	x^(2y) = (x^y)^2
;(* base (pow base (- exp 1)))	if (b & 1) ans *= a	x^(2y+1) = x * x^(2y)