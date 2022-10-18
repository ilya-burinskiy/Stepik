{-
Implement a three-argument function lenVec3 that calculates the length of a
three-dimensional vector.  The function arguments specify the
Cartesian coordinates of the end of the vector, its beginning is assumed to be
at the origin. To take the square root, use the sqrt function defined in the
standard library.
-}

lenVec3 x y z = sqrt (x ^ 2 + y ^ 2 + z ^ 2)
