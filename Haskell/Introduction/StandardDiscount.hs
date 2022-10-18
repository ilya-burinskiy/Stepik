{-
Recall the discount function, which returned the total amount of the
purchase with a possible discount. As parameters, the amount without the
discount sum, the percentage of the discount proc were passed to it, and
the discount was calculated if the transferred amount exceeded the
limit threshold. All of these parameters, as well as the return value, can be
stored in the Double type.
The type of a function can be specified in the source code file along with its definition:

discount :: Double -> Double -> Double -> Double
discount limit proc sum = if sum >= limit then sum * (100 - proc) / 100 else sum

Note that the type declaration is optional, although it is often recommended
as documentation. It is usually placed before a function definition, although
this top-level declaration can be placed anywhere in a source file.

Record the type of the standardDiscount function defined as a partial application of the discount function:

standardDiscount :: ???
standardDiscount = discount 1000 5
-}

discount :: Double -> Double -> Double -> Double
discount limit proc sum = if sum >= limit then sum * (100 - proc) / 100 else sum

standardDiscount :: Double -> Double
standardDiscount = discount 1000 5
