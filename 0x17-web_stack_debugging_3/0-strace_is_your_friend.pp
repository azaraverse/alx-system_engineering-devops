# puppet file to debug apache

$file='/var/www/html/wp-settings.php'
file { $file:
    ensure  => file,
}
exec {'correct typo':
    command => "sed -i s/class-wp-locale.phpp/class-wp-locale.php/g ${file}",
    path    => ['/bin/', '/usr/bin/', '/usr/sbin/'],
}
