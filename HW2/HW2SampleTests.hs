{-Haskell HW2 HUnit test cases
 Please add at least 2 additional tests for problems 3(a)(b)(c) and 4(a)(b)(c) -}

module HW2SampleTests
    where

import Test.HUnit
import Data.Char
import Data.List (sort)
import HW2

{- Two useful functions in the HUnit package are assertEqual and assertBool.
The arguments to 'assertEqual' are:
      a descriptive string
      the expected value
      the value being tested
The arguments to 'assertBool' are:
      a descriptive string
      the boolean value being tested
-}

------ Test cases --
p1a_test1 = TestCase (assertEqual "merge2 [3,2,1,6,5,4] [1,2,3]" ([3,1,2,2,1,3,6,5,4])  (merge2 [3,2,1,6,5,4] [1,2,3]) ) 
p1a_test2 = TestCase (assertEqual "merge2 \"Ct 5\" \"pS35\"" ("CptS 355")  (merge2 "Ct 5" "pS35") ) 
p1a_test3 = TestCase (assertEqual "merge2 [1,2,3] []" ([1,2,3])  (merge2 [1,2,3] []) ) 

p1b_test1 = TestCase (assertEqual "merge2Tail [3,2,1,6,5,4] [1,2,3]" ([3,1,2,2,1,3,6,5,4])  (merge2Tail [3,2,1,6,5,4] [1,2,3]) ) 
p1b_test2 = TestCase (assertEqual "merge2Tail \"Ct 5\" \"pS35\"" ("CptS 355")  (merge2Tail "Ct 5" "pS35") ) 
p1b_test3 = TestCase (assertEqual "merge2Tail [1,2,3] []" ([1,2,3])  (merge2Tail [1,2,3] []) ) 

p1c_test1 = TestCase (assertEqual "mergeN [\"ABCDEF\",\"abcd\",\"123456789\",\"+=?$\"]" ("A+1=a?2$B3b4C5c6D7d8E9F")  (mergeN ["ABCDEF","abcd","123456789","+=?$"]) )
p1c_test2 = TestCase (assertEqual "mergeN [[3,4],[-3,-2,-1],[1,2,5,8,9],[10,20,30]]" [3,10,1,20,-3,30,2,4,5,-2,8,-1,9] (mergeN [[3,4],[-3,-2,-1],[1,2,5,8,9],[10,20,30]]) )
p1c_test3 = TestCase (assertEqual "mergeN [[],[],[1,2,3]]" [1,2,3]  (mergeN [[],[],[1,2,3]]) )

p2a_test1 = TestCase (assertEqual "removeDuplicates [5,4,3,2,1,1,2,3,4,5,6,7]" (sort [1,2,3,4,5,6,7])  (sort (removeDuplicates [5,4,3,2,1,1,2,3,4,5,6,7])) )
p2a_test2 = TestCase (assertEqual "removeDuplicates \"CptS322 - CptS322 -  CptS 321\""  (sort "-CptS 321") (sort (removeDuplicates "CptS322 - CptS322 -  CptS 321")) )
p2a_test3 = TestCase (assertEqual "removeDuplicates [[1,2],[1],[],[3],[1],[]]" (sort [[1,2],[3],[1],[]])  (sort (removeDuplicates [[1,2],[1],[],[3],[1],[]])) )

p2b_test1 = TestCase (assertEqual "count [] [[],[1],[1,2],[]]" 2 (count [] [[],[1],[1,2],[]]) ) 
p2b_test2 = TestCase (assertEqual "count (-5) [1,2,3,4,5,6,7]" 0 (count (-5) [1,2,3,4,5,6,7]) ) 
p2b_test3 = TestCase (assertEqual "count 'i' \"incomprehensibilities\"" 5 (count 'i' "incomprehensibilities") ) 

p2c_test1 = TestCase (assertEqual "histogram [[],[1],[1,2],[1],[],[]]" (sort [([1,2],1),([1],2),([],3)]) (sort (histogram [[],[1],[1,2],[1],[],[]])) )
p2c_test2 = TestCase (assertEqual "histogram \"macadamia\"" (sort [('c',1),('d',1),('m',2),('i',1),('a',4)]) (sort (histogram "macadamia")) )
p2c_test3 = TestCase (assertEqual "histogram (show 122333444455555)" (sort [('1',1),('2',2),('3',3),('4',4),('5',5)]) (sort (histogram (show 122333444455555))) )

p3a_test1 = TestCase (assertEqual "test 3a-1" "enrolled in CptS-355 and CptS-322" (concatAll [["enrolled"," ","in"," "],["CptS","-","355"],[" ","and"," "],["CptS","-","322"]]) )
p3a_test2 = TestCase (assertEqual "concatAll [[],[]]" "" (concatAll [[],[]]))
p3a_test3 = TestCase (assertEqual "test 3a-3" "this homework sucked" (concatAll [["this"," ","homework"," "],["sucked"]]) )
p3a_test4 = TestCase (assertEqual "concatAll [[]]" "" (concatAll [[]]))

p3b_test1 = TestCase (assertEqual "test 3b-1" (AString "enrolled in CptS-355 and CptS-322") (concat2Either [[AString "enrolled", AString " ", AString "in", AString " "],[AString "CptS", AString "-", AnInt 355], [AString " ", AString "and", AString " "], [AString "CptS", AString "-", AnInt 322]]) )
p3b_test2 = TestCase (assertEqual "test 3b-2" (AString "0") (concat2Either [[AString "", AnInt 0],[]]) )
p3b_test3 = TestCase (assertEqual "test 3b-3" (AString "" ) (concat2Either []) )
p3b_test4 = TestCase (assertEqual "test 3b-4" (AString "this homework sucked") (concat2Either [[AString "this", AString " ", AString "homework", AString " "],[AString "sucked"]]) )
p3b_test5 = TestCase (assertEqual "test 3b-5" (AString "yeetyeet") (concat2Either [[AString "yeet", AString "yeet"]]) )

p3c_test1 = TestCase (assertEqual "test 3c-1" ("enrolled in CptS-355 and CptS-322") (concat2Str [[AString "enrolled", AString " ", AString "in", AString " "],[AString "CptS", AString "-", AnInt 355], [AString " ", AString "and", AString " "], [AString "CptS", AString "-", AnInt 322]]) )
p3c_test2 = TestCase (assertEqual "test 3c-2" ("0") (concat2Str [[AString "", AnInt 0],[]]) )
p3c_test3 = TestCase (assertEqual "test 3c-3" ("") (concat2Str []) )
p3c_test4 = TestCase (assertEqual "test 3c-4" ("i4") (concat2Str [[AString "i", AnInt 4],[]]) )
p3c_test5 = TestCase (assertEqual "test 3c-5" ("") (concat2Str [[AString ""],[]]) )

-- Sample Tree Integer examples given in the assignment prompt; make sure to provide your own tree examples for both tree data types
-- Your trees should have minimum 4 levels. 
-- include your tree samples in HW2.hs
exprtree1 =  (ENODE Mul (ENODE Sub (ENODE Add (ELEAF 4) (ELEAF 5)) (ELEAF 6)) (ENODE Sub (ELEAF 10) (ELEAF 8)))
exprtree2 = (ENODE Add (ELEAF 10) (ENODE Sub (ELEAF 50) (ENODE Mul (ELEAF 3) (ELEAF 10))))

p4a_test1 = TestCase (assertEqual "evaluateTree exprtree1" 6 (evaluateTree exprtree1) )
p4a_test2 = TestCase (assertEqual "evaluateTree exprtree2" 30 (evaluateTree exprtree2) )
p4a_test3 = TestCase (assertEqual "evaluateTree (ELEAF 4)" 4 (evaluateTree (ELEAF 4)) )
p4a_test4 = TestCase (assertEqual "evaluateTree tree1" 49 (evaluateTree tree1) )
p4a_test5 = TestCase (assertEqual "evaluateTree tree1" 6 (evaluateTree tree2) )

p4b_test1 = TestCase (assertEqual "printInfix exprtree1" "(((4 `Add` 5) `Sub` 6) `Mul` (10 `Sub` 8))" (printInfix  exprtree1) )
p4b_test2 = TestCase (assertEqual "printInfix exprtree2" "(10 `Add` (50 `Sub` (3 `Mul` 10)))" (printInfix  exprtree2) )
p4b_test3 = TestCase (assertEqual "printInfix (ELEAF 4)" "4" (printInfix  (ELEAF 4)) )
p4b_test4 = TestCase (assertEqual "printInfix tree1" "(((4 `Add` 5) `Sub` 6) `Mul` (10 `Sub` 8))" (printInfix  tree1) )
p4b_test5 = TestCase (assertEqual "printInfix tree2" "(((2 Add 8) Mul 5) Add (1 Sub 2))" (printInfix  tree2) )

-- The createRTree should return the following "ResultTree" values for the above "ExprTree"s
resulttree1 = RNODE 6 (RNODE 3 (RNODE 9 (RLEAF 4) (RLEAF 5)) (RLEAF 6)) (RNODE 2 (RLEAF 10) (RLEAF 8))
resulttree2 = RNODE 30 (RLEAF 10) (RNODE 20 (RLEAF 50) (RNODE 30 (RLEAF 3) (RLEAF 10)))


p4c_test1 = TestCase (assertEqual "createRTree exprtree1" (resulttree1) (createRTree exprtree1) )
p4c_test2 = TestCase (assertEqual "createRTree exprtree2" (resulttree2) (createRTree exprtree2) )
p4c_test3 = TestCase (assertEqual "createRTree (ELEAF 4)" (RLEAF 4) (createRTree (ELEAF 4)) )

-- include your tree samples in HW2.hs

tests = TestList [ TestLabel "Problem 1a - test1 " p1a_test1,
                   TestLabel "Problem 1a - test2 " p1a_test2,
                   TestLabel "Problem 1a - test3 " p1a_test3,                   
                   TestLabel "Problem 1b - test1 " p1b_test1,
                   TestLabel "Problem 1b - test2 " p1b_test2,                   
                   TestLabel "Problem 1b - test3 " p1b_test3,                                      
                   TestLabel "Problem 1c - test1 " p1c_test1,
                   TestLabel "Problem 1c - test2 " p1c_test2,
                   TestLabel "Problem 1c - test3 " p1c_test3,                                      
                   TestLabel "Problem 2a - test1 " p2a_test1,
                   TestLabel "Problem 2a - test2 " p2a_test2,  
                   TestLabel "Problem 2a - test3 " p2a_test3,
                   TestLabel "Problem 2b - test1 " p2b_test1,
                   TestLabel "Problem 2b - test2 " p2b_test2,  
                   TestLabel "Problem 2b - test3 " p2b_test3,
                   TestLabel "Problem 2c - test1 " p2c_test1,
                   TestLabel "Problem 2c - test2 " p2c_test2,  
                   TestLabel "Problem 2c - test3 " p2c_test3,
                   TestLabel "Problem 3a - test1 " p3a_test1,
                   TestLabel "Problem 3a - test2 " p3a_test2,  
                   TestLabel "Problem 3b - test1 " p3b_test1,
                   TestLabel "Problem 3b - test2 " p3b_test2,
                   TestLabel "Problem 3b - test3 " p3b_test3,
                   TestLabel "Problem 3c - test1 " p3c_test1,
                   TestLabel "Problem 3c - test2 " p3c_test2,
                   TestLabel "Problem 3c - test3 " p3c_test3,
                   TestLabel "Problem 4a - test1 " p4a_test1,
                   TestLabel "Problem 4a - test2 " p4a_test2,
                   TestLabel "Problem 4a - test3 " p4a_test3,
                   TestLabel "Problem 4b - test1 " p4b_test1,
                   TestLabel "Problem 4b - test2 " p4b_test2,
                   TestLabel "Problem 4b - test3 " p4b_test3,
                   TestLabel "Problem 4c - test1 " p4c_test1,
                   TestLabel "Problem 4c - test2 " p4c_test2,
                   TestLabel "Problem 4c - test3 " p4c_test3
                 ] 
                  

-- shortcut to run the tests
run = runTestTT  tests