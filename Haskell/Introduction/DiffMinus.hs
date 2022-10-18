{-
Implement the |-| operator, which returns the modulus of the
difference of the arguments passed to it.
-}
x |-| y = if x - y >= 0 then x - y else -(x - y)
