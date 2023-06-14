0. alias ls="rm *" - This script creates an alias with ls as name and rm * as value.
1. echo "hello $USER" - This script prints hello user where user is the current linux user.
2. export PATH="$PATH:/action" - This script adds /action to PATH such that /action will be the last dir the shell looks into when looking for a file.
3. echo $PATH | tr -s ":" "\n" | wc -l - This script counts the number of dir in the PATH.
4. printenv - This script lists environment variables.
5. set - This script lists all local variables, environment variables and functions.
6. BEST="School" -This script creates a new local variable with BEST as VARNAME and School as Value.
7. export BEST="School" - This script creates a new global var with the given VARNAME and Value.
8. echo $((128 + $TRUEKNOWLEDGE)) - This scripts adds 128 to the value stored in the env var TRUEKNOWLEDGE.
9. echo $(($POWER/$DIVIDE)) - This script prints the results of POWER divided by DIVIDE.
10. echo $(($BREATH**$LOVE)) - This script prints the results of BREATH exponent LOVE.
11. echo $((2#$BINARY)) - This script converts a number from base 2 to base 10 from the BINARY var.
12. printf "%s\n" {a..z}{a..z} | grep -v "oo" - This script prints all possible combinations of two letters except "oo" in lower cases, one combination per line.
13. printf "%.2f\n" $NUM - This script prints a number with two decimal places. The number is stored in the env var NUM.
14. printf "%x\n" $DECIMAL - This script converts a number from base 10 to base 16 from the DECIMAL env var.
15. tr 'A-Za-z' 'N-ZA-Mn-za-m' - This script encodes and decodes text using the rot13 encryption.
16. 