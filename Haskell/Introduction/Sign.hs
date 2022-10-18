
{-
Write an implementation of the sign function that returns 1
if it's a positive number, (-1) if it's negative, and 0 if it's 0.
-}
sign x = if x > 0 then 1
         else
            if x < 0 then (-1)
            else 0
