package diffsquares

// SquareOfSums perform square of sums of first number integers
func SquareOfSums(number int) int {
	num := float64(number)
	sum := num * (num + 1.0) * (0.5)
	return int(sum * sum)

}

// SumOfSquares perform sum of squares of first number integers
func SumOfSquares(number int) int {
	num := float64(number)
	sum := num * 1.0 / 3.0 * (num + 1.0) * (num + 0.5)
	return int(sum)

}

// Difference perform difference of SquareOfSums and SumOfSquares
func Difference(num int) int {
	return SquareOfSums(num) - SumOfSquares(num)
}
