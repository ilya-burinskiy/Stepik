{-
Implement a seqA function that finds the elements of the next recurrent sequence
    S_0 = 1
    S_1 = 2
    S_(n + 3) = S_(n + 2) + S_(n + 1) - 2S_n
-}
seqA :: Integer -> Integer

seqA n = let
    helper a b c n
        | n == 0 = a
        | n == 1 = b
        | n == 2 = c
        | otherwise = helper b c (b + c - 2 * a) (n - 1)
    in helper 1 2 3 n
