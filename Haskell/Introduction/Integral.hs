{-
Implement a function that finds the value of the definite integral of the given function f
on the given interval [a,b] using the trapezoidal method.
(Use a uniform grid; 1000 elementary segments are sufficient.)
-}

integration :: (Double -> Double) -> Double -> Double -> Double

integration f a b =
    let n = 1e4
        h = (b - a) / n
        sum i
            | i == n = 0 
            | otherwise = f (a + h * i) + sum (i + 1)
    in h * ((f a + f b) / 2 + sum 1)
