0. alias ls="rm *" - This script creates an alias with ls as name and rm * as value.
1. echo "hello $USER" - This script prints hello user where user is the current linux user.
2. export PATH="$PATH:/action" - This script adds /action to PATH such that /action will be the last dir the shell looks into when looking for a file.
3. find $PATH type -d | wc -1 - This script counts the number of dir in the PATH.
4. 