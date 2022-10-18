{-
We will define points on the plane as pairs of type (Double, Double).
Implement a dist function that returns the distance between two points
passed as arguments to it.
-}

dist :: (Double, Double) -> (Double, Double) -> Double
dist p1 p2 = sqrt $ (fst p2 - fst p1) ^ 2 + (snd p2 - snd p1) ^ 2
