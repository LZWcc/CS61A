(define (ascending? s) 
    (cond
        ((null? s) #t)
        ((null? (cdr s)) #t)
        ((> (car s) (car (cdr s))) #f)
        (else (ascending? (cdr s)))
    )
)

(define (my-filter pred s)
    (cond
    ((null? s) '())
    ((pred (car s)) (cons (car s) (my-filter pred (cdr s))))
    ;   判断条件       (cons 将‘该元素’添加到列表前面  原列表)
    (else (my-filter pred (cdr s)))
    )
)

; Scheme - 自动返回最后一个表达式的值
(define (interleave lst1 lst2) 
    (cond
        ((null? lst1) lst2)
        ((null? lst2) lst1)
        (else
            (cons (car lst1) (interleave lst2  (cdr lst1)))
        )
    )
)

(define (no-repeats s)
    (if (null? s)
        '()
        ;                          (filter predicate(函数) list(过滤列表))
        (cons (car s) (no-repeats (filter (lambda(x) (not (= x (car s)))) (cdr s))))   
        ;                                 返回 x 是否不等于当前列表的第一个元素 (car s)
    )
)

