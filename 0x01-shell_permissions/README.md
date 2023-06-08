0. su betty - This script switches the current user to betty.
1. whoami - This script prints the effective username of the current user.
2. groups - This script prints the groups current user belongs to.
3. chown betty hello - This script changes the ownership of 'hello' to betty.
4. touch hello - This script creates an empty file named 'hello'.
5. chmod u+x hello - This script adds execution permission to the file 'hello'.
6. chmod ug+x, o+r hello - This script adds execution permit to owner and group owners and read only permit to other users for the file 'hello'.
7. chmod ugo+x hello - This script adds execution permission to the owner, the group and others for the file 'hello'.
8. chmod 007 hello - This script removes all permissions from user and group and adds all pwermissions to other users for the file 'hello'.
9. chmod 753 hello - This script gives read, write and execute permission to user, read and execute permission to group and write and execute permission to other users for the file 'hello'.
10. chmod --reference=olleh hello - This script sets the mode of the file 'hello' the same as 'olleh's' mode.
11. chmod -R +x - This script adds an execute permission to all subdir of the current dir for owner, group owner and other users without affecting regular files.
12. mkdir -m 751 my_dir - This script creates a dir named my_dir with 751 as permissions.
13. chgrp school hello - This script chnages the owner of the file 'hello' to school.
14. chown vincent:staff - This script changes the owner of all files and dir to vincent and group owner to staff.
15. chown -h vincent:staff _hello - This script changes the owner and group owner to vincent and staff respectively of the file 'hello'.
16. chown --from=guillaume betty hello - This script changes the owner of the file hello to betty only if the file is owned by guillaume.
17. telnet towel.blinkenlights.nl - This script will play starwars episode IV in your termnial.
