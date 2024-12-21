-- https://www.hackerrank.com/challenges/30-operators/
main = do
	bases <- getLine
	tips <- getLine
	texs <- getLine
	let base = read bases:: Float
	let tip = read tips:: Float
	let tex = read texs:: Float
	let tipt = base*tip/100
	let text = base*tex/100 
	let ans = (tipt + text + base)
	putStrLn("The total meal cost is " ++ show (round(ans)) ++ " dollars.")
