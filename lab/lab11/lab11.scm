(define (if-program condition if-true if-false)
  (list 'if condition if-true if-false)
)

(define (square n) (* n n))

(define (pow-expr base exp) 
  (cond
    ((= exp 0) 1)
    ((even? exp) (list 'square (pow-expr base (/ exp 2))))
    ((odd? exp) (list '* base (pow-expr base (- exp 1))))
  )
)

(define-macro (repeat n expr)
  `(repeated-call ,n (lambda () ,expr)))
;                     这是一个没有参数的过程。
;                     只能用 (f) 这样调用它

; Call zero-argument procedure f n times and return the final result.
(define (repeated-call n f)
  (if (= n 1)
      (f);(f) 的意思是调用这个过程，得到它的返回值。
         ;f 只是过程本身，不会执行。
      (begin (f) (repeated-call (- n 1) f))))
