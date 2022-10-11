# Nginx server configuration
exec {'Update the apt repository':
  command  => 'apt update',
  path     =>  '/usr/bin:/usr/sbin:/bin'
}

package {'The web server':
  ensure     	  => installed,
  name       	  => 'nginx',
  provider   	  => 'apt',
  install_options => ['-y']
}

file {'The home page':
   ensure  => file,
   path    => '/var/www/html/index.html',
   mode    => '0744',
   owner   => 'www-data',
   content => "Hello World!\n"
}

file {'The 404 page':
   ensure   => file,
   path     => '/var/www/error/404.html',
   mode     => '0744',
   owner    => 'www-data',
   content  => "Ceci n'est pas une page\n"
}
