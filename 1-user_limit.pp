# Change OS configuration to login with the holberton user
# + and open file without any error message
exec {'increase file limit':
  command => 'sysctl -w fs.file-max=500000'
}
