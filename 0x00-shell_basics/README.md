0. pwd This script prints the absolute path name of the current working dir.
1. ls This script displays the content of the current working dir.
2. cd This script changes the working dir to the user’s home dir.
3. ls -l This script displays current dir contents in a long format.
4. ls -a This script displays current dir contents, including hidden files.
5. ls -lna This script displays current dir contents, in long format including numerics.
6. mkdir /tmp/my_first_directory This is a script that creates a dir in a dir from the working dir.
7. mv /tmp/betty /tmp/my_first_directory This is a script that moves a file from parent dir to subdir.
8. rm /tmp/my_first_directory/betty This is a script that deletes a file from a subdir of a parent dir without navigating to the actual file.
9. rmdir /tmp/my_first_directory This is a script that deletes a subdir from a parent dir. Subdir must be empty.
10. cd - This is s script that changes the working dir to a previous one.
11. ls -al . .. /boot This is a script that lists all files in the current dir and the parent of the working dir and the /boot dir, in long format.
12. file /tmp/iamafile This is a script that prints the file named iamafile in the tmp dir.
13. ln -s /bin/ls __ls__ This is a script that creates a symbolic link to /bin/ls, named __ls__
14. cp -un *.html ../ This is a script that copies all the HTML files from the current working dir to the parent of the working dir, but only copies files that did not exist in the parent of the working dir.
15. mv [[:upper:]]* /tmp/u This is a script that moves all files beginning with an uppercase letter to the dir /tmp/u
16. rm *~ This is a script that deletes all files in the current working dir that end with the character ~.
17. mkdir -p welcome/to/school This is a script that creates the dir -> welcome/, welcome/to/ and welcome/to/school in the current dir.
18. ls -mavp This is a script that lists all the files and directories of the current directory, separated by commas (,), has dir names ending with slash (/), files and dir starting with . are listed and where digits and letters are used to sort, with digits appearing first.