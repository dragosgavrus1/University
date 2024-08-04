(defun par (L)
    (cond 
        ((null L) nil)
        ((and (numberp L) (= (mod L 2 ) 0)) (+ L 1))
        ((atom L) L)
        (t (mapcar `par L))
    )
)


(print(par `(1 s 4 (2 f (7)))))