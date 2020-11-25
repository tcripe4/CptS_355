-- CptS 355 - Fall 2020  : 09/06/2020

module HW1
     where


-- 1.a. biggerDate and maxDate
biggerDate::(Ord a1,Ord a2,Ord a3)=>(a3,a2,a1)->(a3,a2,a1)->(a3,a2,a1)
biggerDate (x, x1, x2) _ = (x, x1, x2)
biggerDate (x, x1, x2) (y, y1, y2) = if x2 > y2 then (x, x1, x2) else if x1 > y1 then (x, x1, x2) else (y, y1, y2)


-- 1.b. maxDate
maxDate :: (Ord a1, Ord a2, Ord a3) => [(a3, a2, a1)] -> (a3, a2, a1)
maxDate (x:xs) = foldr1 biggerDate xs

-- 2. ascending
ascending :: Ord t => [t] -> Bool
ascending [] = True
ascending (x:xs) = (tracker xs x)

tracker :: Ord t => [t] -> t -> Bool
tracker [] y = True
tracker (x:xs) y = y <= x && tracker xs x
-- 3.a. insert 
insert :: (Eq t1, Num t1) => t1 -> t2 -> [t2] -> [t2]
insert 0 y x = y:(insert 100 y x)
insert a y [] = []
insert a y (x:xs) = x:(insert (a-1) y xs)

-- 3.b. insertEvery
insertEvery :: (Eq t, Num t) => t -> a -> [a] -> [a]
insertEvery a y [] = []
insertEvery a y x = count a x where
  count 0 x = y:count a x
  count _ [] = []
  count m (x:xs) = x:count (m - 1) xs


-- 4.a. getHours
storelog = [("Mon",50),("Fri",20), ("Tue",20),("Fri",10),("Wed",25),("Fri",30)]
sales = [("Amazon",[("Mon",30),("Wed",100),("Sat",200)]), ("Etsy",[("Mon",50),("Tue",20),("Wed",25),("Fri",30)]), ("Ebay",[("Tue",60),("Wed",100),("Thu",30)]), ("Etsy",[("Tue",100),("Thu",50),("Sat",20),("Tue",10)])]

getSales :: (Num p, Eq t) => t -> [(t, p)] -> p
getSales day [] = 0
getSales day ((x,y):xs) | (day == x) = y + (getSales day xs) | otherwise = getSales day xs
                          
-- 4.b. sumSales
sumSales:: (Num p)=> String -> String -> [(String,[(String,p)])] -> p
sumSales a b ((x,(y)):xs) = if (x == a) then getSales b y else sumSales a b xs


-- 5.a. split
split :: Eq a => a -> [a] -> [[a]]
split _ [] = []
split x y = w : split x (drop 1 a) where (w,a) = span (/=x) y


-- 5.b. nSplit
--nSplit :: (Ord a1, Num a1, Eq a2) => a2 -> a1 -> [a2] -> [[a2]]
--nSplit x n [] = []
--nSplit x n y = (take n y):(nSplit x n (drop n y))

-- I really strtuggled with this one and could not get it to work
