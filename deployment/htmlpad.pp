$site = 'htmlpad.org'
$etherpad = 'etherpad.mozilla.org:9000'
$rootDir = '/var/htmlpad'
$apacheDir = '/etc/apache2'
$varDir = "$rootDir/$site"
$wsgiDir = "$varDir/wsgi-scripts"
$staticFilesDir = "$varDir/static-files"

package { 'libapache2-mod-wsgi':
  ensure => present,
  before => File["$apacheDir/sites-available/$site"],
}

service { 'apache2':
  ensure => running,
  enable => true,
  hasrestart => true,
  hasstatus => true,
  subscribe => File["$apacheDir/sites-available/$site"],
}

file { "$apacheDir/sites-available/$site":
  ensure => file,
  owner => 'root',
  group => 'root',
  content => template("$rootDir/deployment/apache-site.conf.erb"),
}

file { "$apacheDir/sites-enabled/001-$site":
  ensure => link,
  target => "$apacheDir/sites-available/$site"
}
