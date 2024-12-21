-- https://www.hackerrank.com/challenges/30-loops/
import Control.Applicative
import Control.Monad
import System.IO


main :: IO ()
main = do
    n_temp <- getLine
    let n = read n_temp :: Int
    multi 10 n

multi :: Int -> Int -> IO()

multi 0 b = return ()
multi a b = do
	multi (a-1) b
	putStrLn(show b ++ " x " ++ show a ++ " = " ++ show (b*a))

