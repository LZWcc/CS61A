`(+ ,(* 2 3) 1) ; (+ 6 1)
(define (square-expr term) `(* ,term ,term))
`(+ ,(square-expr `a) ,(square-expr `b)) ; (+ (* a a) (* b b))

(define-macro (twice expr)
    (list 'begin expr expr))
> (twice (print 2))
2
2

> (begin (print 2) (print 2))
2
2


(define (map fn vals) ;map为函数名, 接收两个参数fn(函数)和vals(列表)
    (if (null? vals) ;如果vals为空
        () 
        (cons
            (fn (car vals))
            (map fn (cdr vals))
        )
)
> (map (lambda (x) (* x x)) '(1 2 3 4))
(1 4 9 16)

(define-macro (for sym vals expr)
    (list 'map
          (list 'lambda (list sym) expr)
          vals)
)

def trace(fn):
    def traced(n):
        print(f"{fn.__name__} ({n})")
        return fn(n)
    return traced