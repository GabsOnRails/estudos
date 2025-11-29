//Preciso converter uma string em um número. Não faço ideia de como fazer isso.
// Deve ser utilizando uma lib. Há dois pacotes que fazem isso: Atoi e ParseInt.
// O Atoi é mais simples comparado ao ParseInt que deixa escolher a base do input entre
// binario, octal, hexadecimal etc.
// bem fácil na real, só usar o package para converter.

// ------------------------------------------------------------------------------------------------------------------
// Documentation:
// StringToNumber converts a string representation of a number into an integer.
//
// Parameters:
//
//	str - A string containing a numeric value (e.g., "42", "-10", "0")
//
// Returns:
//
//	int - The converted integer value
//
// Notes:
//   - Uses strconv.Atoi for simple string-to-integer conversion
//   - Returns 0 if the conversion fails (error case)
//   - For more complex conversions (different bases: binary, octal, hex),
//     consider using strconv.ParseInt instead
//
// Example:
//
//	StringToNumber("123")  // Returns: 123
//	StringToNumber("-45")  // Returns: -45
//	StringToNumber("abc")  // Returns: 0 (with error message printed)
package main

import (
	"fmt"
	"strconv"
)

func main() {

}

func StringToNumber(str string) (int, error) {
	num, err := strconv.Atoi(str)
	if err != nil {
		fmt.Println("Error converting string to integer:", err)

	}
	return num, err
}
