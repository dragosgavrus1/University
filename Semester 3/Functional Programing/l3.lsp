; 11. Write a function to determine the depth of a list.

(defun searching (l level)
    (cond
        ((atom l) level)
        ((listp l) (apply #'max (mapcar #'(lambda(s) (searching s (+ level 1))) l)))
    )
)

         
(print (searching '(1 (2 (3)) (4) (5 (6 (7)))) -1))