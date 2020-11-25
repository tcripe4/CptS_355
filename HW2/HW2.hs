-- CptS 355 Assignment 2
-- Travis Cripe
-- 11519554
module HW2
     where

-- 1
{- (a) merge2 5%-}
{-The function merge2 takes two lists, l1 and l2, and
returns a merged list where the elements from l1 and l2 appear interchangeably.
The resulting list should include the leftovers from the longer list and it may include duplicates.-}
merge2::[a]->[a]->[a]
merge2 [] [] = []
merge2 x [] = x
merge2 [] y = y
merge2 (x:xt) (y:yt) = x:y:(merge2 xt yt)
{- (b) merge2Tail 10% -}
merge2Tail::[a]->[a]->[a]
merge2Tail x y = mergehelp x y where
                 mergehelp [] [] = []
                 mergehelp x [] = x
                 mergehelp [] y = y
                 mergehelp (x:xt) (y:yt) = x:y:(mergehelp xt yt)
{- (c) mergeN 5%-}
mergeN:: [[a]] -> [a]
mergeN (x:xt) = foldl merge2 x xt
-- 2
{- (a) removDuplicates 10% -}
removeDuplicates:: Eq a => [a] -> [a]
removeDuplicates [] = []
removeDuplicates (x:xs) = x : removeDuplicates (filter (/= x) xs)
{- (b) count 5% -}
count :: Eq a => a -> [a] -> Int
count n [] = 0
count n x = length xs where
            xs = [xs | xs <- x, xs == n]
{- (c) histogram 10% -}
--histogram :: Eq a => [a] -> [(a, Int)]
--histogram list = (+) map (\l -> (length l, head l)) (group (sort list))


-- 3
data AnEither  = AString String | AnInt Int
                deriving (Show, Read, Eq)
{- (a) concatAll 4% -}
concatAll :: [[String]] -> String
concatAll [[]] = ""
concatAll x = foldr (++) "" (map concat x)
{- (b) concat2Either 9% -}
concat2Either:: [[AnEither]] -> AnEither
concat2Either x = foldr concatHelper (AString "") (map (foldr concatHelper (AString "")) x) where
concatHelper :: AnEither -> AnEither -> AnEither
concatHelper (AString x) (AnInt y) = AString(x ++ (show y))
concatHelper (AString x) (AString y) = AString(x ++ y)
concatHelper (AnInt x) (AString y) = AString((show x) ++ y)
{- (c) concat2Str 6% -}


concat2Str:: [[AnEither]] -> String
concat2Str x = foldr concatHelp "" (foldr (++) [] x) where
concatHelp :: AnEither -> String -> String
concatHelp (AString x) y = (x ++ y)
concatHelp (AnInt x) y = (show(x) ++ y)

-- 4 

data Op = Add | Sub | Mul | Pow
          deriving (Show, Read, Eq)

evaluate:: Op -> Int -> Int -> Int
evaluate Add x y =  x+y
evaluate Sub x y =  x-y
evaluate Mul x y =  x*y
evaluate Pow x y = x^y

data ExprTree a = ELEAF a | ENODE Op (ExprTree a) (ExprTree a)
                  deriving (Show, Read, Eq)

{- (a) evaluateTree - 10% -}
evaluateTree :: ExprTree Int -> Int
evaluateTree (ELEAF a) = a
evaluateTree (ENODE o l r) = evaluate o (evaluateTree l) (evaluateTree r)

{- (b) printInfix - 10% -}
printInfix:: Show a => ExprTree a -> String
printInfix (ELEAF a) = show(a)
printInfix (ENODE o l r) = "(" ++ printInfix l ++ " " ++ show(o) ++ " " ++ printInfix r ++ ")"


{- (c) createRTree 12% -}
data ResultTree a  = RLEAF a | RNODE a (ResultTree a) (ResultTree a)
                     deriving (Show, Read, Eq)
createRTree :: ExprTree Int -> ResultTree Int
createRTree (ELEAF a) = RLEAF(a)
createRTree (ENODE o l r) = RNODE(evaluateTree (ENODE o l r)) (createRTree l) (createRTree r)
-- 5
{-Sample trees 4% -}

tree1 = (ENODE Add (ENODE Mul (ENODE Add (ELEAF 2) (ELEAF 8)) (ELEAF 5)) (ENODE Sub (ELEAF 1) (ELEAF 2)))
tree2 = (ENODE Add (ELEAF 10) (ENODE Sub (ELEAF 50) (ENODE Mul (ELEAF 3) (ELEAF 10) (ENODE Pow (ELEAF 2)))))
-- did tree 2 just to show a printInfix error



