# a manifest that installs and configures an Nginx server using puppet.
# - listens on port 80
# - return a page with Hello World! when requesting a page using curl
# - redirection must be "301 Moved Permanently"
# - 404 page that displays "Ceci n'est pas une page"

$nginx_package = 'nginx'
$nginx_service = 'nginx'
$index_file = '/var/www/html/index.html'
$file_404 = '/usr/share/nginx/html/404.html'
$config_file = '/etc/nginx/sites-available/default'

# install Nginx package
exec { 'apt-get update':
    command => '/usr/bin/apt-get update',
    path    => ['/usr/bin', '/usr/sbin']
}

package { $nginx_package:
    ensure  => installed,
    require => Exec['apt-get update']
}

# define html file
file { $index_file:
    ensure  => present,
    content => "Hello World!\n",
    require => Package[$nginx_package]
}

# define 404 file
file { $file_404:
    ensure  => file,
    content => "Ceci n'est pas une page\n",
    require => Package[$nginx_package]
}

# define temp config
file { $config_file:
    ensure  => file,
    content => "
server {
    root /var/www/html;
    index index.html index.htm;

    server_name _;

    location /redirect_me {
        return 301 https://www.facebook.com/yushahuazara?mibextid=ZbWKwL;
    }

    error_page 404 /404.html;

    location = /404.html {
        root /usr/share/nginx/html;
        internal;
    }
}",
    require => Package[$nginx_package],
    notify  => Service[$nginx_service]
}

# define nginx service
service { $nginx_service:
    ensure  => running,
    enable  => true,
    require => Package[$nginx_service]
}
