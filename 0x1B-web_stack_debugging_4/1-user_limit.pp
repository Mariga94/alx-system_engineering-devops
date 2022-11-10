#Change the OS configuration so that it is possible to login

exec {"increase limit for hard file":
  command => 'sed -i "/holberton hard/s/5/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}

exec {"increase limit for soft file":
  command => 'sed -i "/holberton soft/s/6/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}
