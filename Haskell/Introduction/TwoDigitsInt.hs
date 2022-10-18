{-
Implement a twoDigits2Int function that takes two characters and returns a
number made up of those characters if both characters are numeric and
100 otherwise. (The first character is treated as a number of tens,
the second character is treated as units.)
-}

import Data.Char

twoDigits2Int :: Char -> Char -> Int
twoDigits2Int x y = if isNumber(x) && isNumber(y)
                    then digitToInt(x) * 10 + digitToInt(y)
                    else 100
