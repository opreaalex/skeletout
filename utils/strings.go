package utils

import (
	"strings"
)

// A capitalization utility function that works like
// python's str.capitalize
// For a given string, the function will capitalize the first
// character while lowering the case of the remaining string.
func Capitalize(s string) string {
	first := ""
	remains := ""

	if len(s) > 0 {
		first = strings.ToUpper(string(s[0]))
	}

	if len(s) > 1 {
		remains = strings.ToLower(string(s[1:]))
	}

	return first + remains
}
