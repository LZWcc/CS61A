scm> (define-macro (twice expr) (list 'begin expr expr))
twice
scm> (twice (+ 2 2))  ; evaluates (begin (+ 2 2) (+ 2 2))
4
scm> (twice (print (+ 2 2)))  ; evaluates (begin (print (+ 2 2)) (print (+ 2 2)))
4
4

; Q1: Mystery Macro
(define-macro (mystery-macro expr old new)
    (mystery-helper expr old new))

(define (mystery-helper e o n)
  (if (pair? e)
      (cons (mystery-helper (car e) o n) (mystery-helper (cdr e) o n))
      (if (eq? e o) n e)))

; 如果e不是一个pair(即它是一个原子, 检查这个原子e和旧原子o是否完全相同), 相同返回新原子n, 不同返回旧原子o
; 如果e是一个有序对, 处理列表的头部和尾部, 并用cons构造一个新的有序对

; Q2: Multiple Assignment
(define-macro (assign sym1 sym2 expr1 expr2)
  `(begin
     (define ,sym1 ,expr1)
     (define ,sym2 ',(eval expr2)))) ; 在宏展开阶段，就把 expr2 的值算出来

(assign x y (+ 1 1) 3)
(assign x y y x)
(expect x 3)
(expect y 2)

; Q3: Switch
(define-macro (switch expr cases)
    `(let ((val ,expr)) ; 先计算 expr，把结果绑定到 val
	  ,(cons
	    'cond
	    (map (lambda (case) (cons   ; map 生成每个分支, 对 cases 里的每个 case（如 (1 (print 'a))），都生成一条 cond 分支。
	           '(equal? val ,(car case)) ; 生成 ((equal? val 1) (print 'a)) 这样的 cond 分支。
		       (cdr case)))
		     cases))))