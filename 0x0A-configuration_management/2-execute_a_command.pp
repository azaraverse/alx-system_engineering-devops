# a puppet manifest that kills a process
exec { 'killme_process':
    command => 'pkill -f killmenow',
    path    => '/usr/bin'
}
