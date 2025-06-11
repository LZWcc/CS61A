; formals - 一个参数名的列表
; body 一个带引号的表达式
(define (curry-cook formals body) 
  (if (null? (cdr formals))
      (list 'lambda (list (car formals)) body)
      (list 'lambda (list (car formals)) (curry-cook (cdr formals) body))
  )
)

(define (curry-consume curry args)
  (if (null? args)
    curry
    (curry-consume (curry (car args)) (cdr args))
  )
)

; 把 switch 结构包装成一个带引号的列表，交给 switch-to-cond 处理。
(define-macro (switch expr options)
  (switch-to-cond (list 'switch expr options)))

(define (switch-to-cond switch-expr) ; 输入的列表为带引号的结构
  (cons 'cond
        (map (lambda (option)
               (cons (list 'equal? 
                           (car (cdr switch-expr)) ; 判断表达式
                           (car option))           ; 当前选项的匹配值
                     (cdr option)))                ; 当前选项的结果表达式
             (car (cdr (cdr switch-expr))))))      ; 所有选项的列表
; (car (cdr switch-expr)) 取出判断表达式
; (car option) 取出当前选项的匹配值
; (cdr option) 取出结果表达式
;switch-expr: '(switch (+ 1 1) ((1 'a) (2 'b) (3 'c)))
;options:      ((1 'a) (2 'b) (3 'c))
;option:       (1 'a)   (2 'b)   (3 'c)   (每次map处理一个)