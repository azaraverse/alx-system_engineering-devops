1. echo 'Hello, World' - This script prints "Hello, World" followed by a new line to the standard output.
2. echo "\"(Ôo)" - This script prints a confused smiley emoji.
3. cat /etc/passwd - This script displays the content of the '/etc/passwd' file.
4. cat /etc/passwd /etc/hosts - This script displays the content of two files at the same time.
5. tail -n 10 /etc/passwd - This script displays the last 10 lines of the '/etc/passwd' file. 
6. head -n 10 /etc/passwd - This script displays the first 10 lines of the '/etc/passwd' file.
7. head -n 3 iacta | tail -n 1 - This script displays the third line of the 'iacta' file.
8. echo 'Best School' > '\*\\'\''"Best School"\'\''\\*$\?\*\*\*\*\*:)' - This script creates a file with the given name with 'Best School' contained in the file. The single quotes '' at the beginning and end of the second part of the code protects the text so it has it serves its literal purpose.
9. ls -la > ls_cwd_content - This script writes the content of ls -la into ls_cwd_content.
10. tail -n 1 iacta >> iacta - This script duplicates the last line of the file 'iacta'.
11. find . -type f -name "*.js" -exec rm {} + - This script finds all regular files with ".js" as an extension within the current working dir and its subdir, then executes the delete command.
12. find . -mindepth 1 -type d | wc -l - This script counts the number of dir and subdir (+ hidden) in the current dir excluding current and parent dir.
13. 