import Control.Monad
import Control.Monad.State
import Data.List

data Node = Node { metadata :: [Int], children :: [Node] }
    deriving Show

type Parser = State [Int]

getNext :: Parser Int
getNext = state (\(x:xs) -> (x, xs))

parseTree :: Parser Node
parseTree = do
    numChildren <- getNext
    numMetadata <- getNext
    children <- replicateM numChildren parseTree
    metadata <- replicateM numMetadata getNext
    return (Node metadata children)

toTree :: [Int] -> Node
toTree = evalState parseTree

value1 :: Node -> Int
value1 (Node m c) = sum m + sum (map value1 c)

value2 :: Node -> Int
value2 (Node m []) = sum m
value2 (Node m c)  = sum [value2 (c !! i) | i <- m_, i < (length c)]
    where m_ = map (subtract 1) m

easyInput = [2, 3, 0, 3, 10, 11, 12, 1, 1, 0, 1, 99, 2, 1, 1, 2]

main = do
    let tree = toTree easyInput
    putStrLn $ "Part 1: " ++ (show (value1 tree))
    putStrLn $ "Part 2: " ++ (show (value2 tree))
