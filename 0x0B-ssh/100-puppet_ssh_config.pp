# configures the SSH client

$config = "IdentityFile ~/.ssh/school
PubKeyAuthentication yes
PasswordAuthentication no
"

file {'/etc/ssh/ssh_config':
    ensure  => present,
    content => $config
}
