;; (defun fct(f l)
;;    ((lambda(x)
;;     (cond
;;         ((null l) nil)
;;         (x (cons x (fct f (cdr l))))
;;         (t nil)
;;     ) 
;;    ) (funcall f (car l))
;;    )
;; )

;; (defun g(l) (list (car l) (car l)))
;;---------------------------------------------------
;; (defun f(l e lvl)
;;     (cond
;;         ((and (atom l) (= 0 (mod lvl 2))) l)
;;         ((atom l) e)
;;         (t (mapcar #'(lambda(x) (f x e (+ lvl 1))) l))
;;     )
;; )

;; (defun ff(l e)
;;     (f l e -1)
;; )
;;---------------------------------------------------

;; (defun f(x &rest y)
;;     (cond
;;         ((null y) x)
;;         (t (append x (mapcar #'car y)))
;;     )
;; )
;; (defun g(x &optional (y 6))
;;     (cond
;;         (t y)
;;     )
;; )

;; (defun lvl(l n)
;;     (cond
;;         ((and (atom l) (= n 0)) 0)
;;         ((atom l) l)
;;         (t (mapcar #'(lambda(x) (lvl x (- n 1))) l))
        
    
;;     )
;; )

;-----------------------------------------------------------

;; (defun g(f l)
;;     (funcall f l)
;; )


(defun f(l)
    (cond
        ((and (numberp l) (= 0 (mod l 2))) (+ l 1))
        ((atom l) l)
        (t (mapcar #'f l))
        
    )
)

(defun g(x &rest y)
    (cond
        ((null y) x)
        (t (append x (mapcar #'car y)))
    )
)

(print(append(g `(1 2))(g `(3 4) `(5 6) `(7 8))))