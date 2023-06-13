0. echo 'Hello, World' - This script prints "Hello, World" followed by a new line to the standard output.
1. echo "\"(Ôo)" - This script prints a confused smiley emoji.
2. cat /etc/passwd - This script displays the content of the '/etc/passwd' file.
3. cat /etc/passwd /etc/hosts - This script displays the content of two files at the same time.
4. tail -n 10 /etc/passwd - This script displays the last 10 lines of the '/etc/passwd' file. 
5. head -n 10 /etc/passwd - This script displays the first 10 lines of the '/etc/passwd' file.
6. head -n 3 iacta | tail -n 1 - This script displays the third line of the 'iacta' file.
7. echo 'Best School' > '\*\\'\''"Best School"\'\''\\*$\?\*\*\*\*\*:)' - This script creates a file with the given name with 'Best School' contained in the file. The single quotes '' at the beginning and end of the second part of the code protects the text so it has it serves its literal purpose.
8. ls -la > ls_cwd_content - This script writes the content of ls -la into ls_cwd_content.
9. tail -n 1 iacta >> iacta - This script duplicates the last line of the file 'iacta'.
10. find . -type f -name "*.js" -exec rm {} + - This script finds all regular files with ".js" as an extension within the current working dir and its subdir, then executes the delete command.
11. find . -mindepth 1 -type d | wc -l - This script counts the number of dir and subdir (+ hidden) in the current dir excluding current and parent dir.
12. ls -t | head -n 10 - This script displays the newest lines in the current dir sorted from newest to oldest.
13. sort | uniq -u - This script prints only words that appear once from a given list.
14. grep root /etc/passwd - This script displays lines containing the pattern 'root' from the file /etc/passwd.
15. grep -c bin /etc/passwd - This script displays the number of lines that contain the pattern bin from the /etc/passwd file.
16. grep root /etc.passwd --after-context=3 - This script displays lines containing the pattern 'root' and 3 lines after them in the /etc/passwd file.
17. grep -v bin /etc/passwd - This script displays all the lines in the file /etc/passwd that do not contain the pattern 'bin'.
18. grep '^[[:alpha:]]' /etc/ssh/sshd_config - This script displays all lines of the file /etc/ssh/sshd_config starting with a letter + capital letters.
19. tr A Z | tr c e - This script replaces A with Z and c with e.
20. tr -d c | tr -d C - This script removes all letters c and C from a file.
21. rev - This script reverses inputs.
22. cut -d : -f 1,6 /etc/passwd | sort - This script displays all users and their home dir, sorted by users based on the /etc/passwd file.
23. find . -empty -printf "%f\n" - This script or command finds all empty files and dir and subdir in the current dir.
24. find . -name "*.gif" -type f -printf "%f\n" | rev | cut -d. -f2- | rev | LC_ALL=C sort -f -
25. echo $(cut -c1 | tr -d " \n") - This script decodes acrostics that use the first letter of each line.
26. tail -n +2 | cut -f -1 | sort -k 1 | uniq -c | sort -mk 1 | head -n 11 | rev | cut -d' ' -f -1 | rev - This script parses web servers logs in TSV format as input and displays the 11 hosts or IP addresses which did the most requests.
