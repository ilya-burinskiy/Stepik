{-
Define a function that calculates the double factorial, that is, the product of
natural numbers that do not exceed a given number and have the same parity
-}

doubleFact :: Integer -> Integer

doubleFact 0 = 1
doubleFact 1 = 1
doubleFact n = n * doubleFact (n - 2)
