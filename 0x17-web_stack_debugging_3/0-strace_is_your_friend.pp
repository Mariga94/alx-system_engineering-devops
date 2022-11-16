# Bug Fix

exec { 'bug-fix':
  command  => 'echo s/phpp/php/g > /var/www/html/wp-settings.php',
  path     => '/usr/local/bin/:/bin/'
