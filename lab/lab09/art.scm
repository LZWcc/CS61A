;;; Scheme Recursive Art Contest Entry
;;;
;;; Pl       ; Simplified nested expressions by extracting variables
       (let ((z0 (list (/ x scale-factor) (/ y scale-factor))))
         (let ((z-bail (mandel c-param z0 max-iterations)))
           (let ((iterations (im (cdr z-bail))))
             (if (< iterations max-iterations)
                 ; Mandelbrot set escape case - use color
                 (let ((color (col iterations)))
                   (pixel x y color)
                   (pixel (* x -1) (* y -1) color))
                 ; Inside Mandelbrot set - use black
                 (begin
                   (pixel x y "black")
                   (pixel (* x -1) (* y -1) "black")))
             (loop (+ x 1) y))))))))clude your name or personal info in this file.
;;;
;;; Title: Deep Blue
;;;
;;; Description:
;;;   Dreaming spirals blue
;;;   Midnight fractal swirls awake
;;;   Silence of deep math

; need to define complex numbers. Complex numbers are lists here.
(define c-param '(0.39 -0.31))

; Constants for better readability
(define max-iterations 50)
(define escape-radius-squared 4)
(define scale-factor 66.67)

(define (square-rl a) (* a a))
(define (im z) (car (cdr z)))
(define (mag-square z) (+ (square-rl (car z)) (square-rl (im z))))
(define (mandel c z0 iters)
  (let ((x0 (car c)) (y0 (im c)) (x (car z0)) (y (im z0)) (x2 (square-rl (car z0))) (y2 (square-rl (im z0))))
  (define (mandel-iter x y x2 y2 n)
    (if (or (= n max-iterations) (> (+ x2 y2) escape-radius-squared))
      (list x y n)
      (let ((new-y (+ (* 2 x y) y0))
            (new-x (+ (- x2 y2) x0)))
        (let ((new-x2 (* new-x new-x))
              (new-y2 (* new-y new-y)))
          (mandel-iter new-x new-y new-x2 new-y2 (+ n 1))))))
  (mandel-iter x y x2 y2 0)))

(define (col i)
  (let ((t (/ i max-iterations)))     
    (rgb 0                          
         (* (- 1 t) 0.6)             
         (- 1 (* 0.7 t)))))          

(define (fill-points l w)
  (define (loop x y)
    (cond
      ((> y w)  ; Fixed: changed from (> y 0) to proper exit condition
       'done)   ; Added return value
      ((>= x l)
       (goto (* l -1) (+ y 1))
       (loop (* l -1) (+ y 1)))
      (else
       ; Simplified nested expressions by extracting variables
       (let ((z0 (list (/ x 66.67) (/ y 66.67))))
         (let ((z-bail (mandel c-param z0 50)))
           (let ((iterations (im (cdr z-bail))))
             (if (< iterations 50)
                 ; Mandelbrot set escape case - use color
                 (let ((color (col iterations)))
                   (pixel x y color)
                   (pixel (* x -1) (* y -1) color))
                 ; Inside Mandelbrot set - use black
                 (begin
                   (pixel x y "black")
                   (pixel (* x -1) (* y -1) "black")))
             (loop (+ x 1) y)))))))
  (loop (* l -1) (* w -1)))

(define (draw)
  (ht)
  (speed 0)
  (begin_fill)
  (goto 1000 0)
  (circle 900)
  (end_fill) (pu)
  (pixelsize 5)
  (fill-points 100 100)
  (exitonclick))
; command to run: python3 scheme contest_copy2.scm --turtle-save-path output
; Please leave this last line alone. You may add additional procedures above
; this line.
(draw)