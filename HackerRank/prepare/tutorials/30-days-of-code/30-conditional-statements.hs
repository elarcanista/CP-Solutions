-- https://www.hackerrank.com/challenges/30-conditional-statements/
import Control.Applicative
import Control.Monad
import System.IO

main = do
	temp <- getLine
	let n = read temp :: Int
	if mod n 2 /= 0
		then putStrLn "Weird"
		else if n >= 2 && n <= 5
			then putStrLn "Not Weird"
			else if n >= 6 && n <= 20
				then putStrLn "Weird"
				else putStrLn "Not Weird"
