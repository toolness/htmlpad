## HTMLpad ##

By [Atul Varma][]

This is a trivial wsgi application that, for any URL path, serves the
contents of an Etherpad with the same path with the MIME type
`text/html`.

For example, if the application is served from `htmlpad.org` and the
Etherpad backend it's configured to use is at
`etherpad.mozilla.org:9000`, then visiting `http://htmlpad.org/foo`
will deliver the contents of `http://etherpad.mozilla.org:9000/foo` as
HTML.

This effectively allows people to easily collaborate on writing HTML,
and it provides a very fast feedback loop between trying something
out, seeing how it looks in the browser, and sharing it with others.

### Installation ###

This project has no dependencies aside from Python 2.5. Just run `server.py` and open your browser to [http://localhost:8000](http://localhost:8000).

### Deployment ###

The [Puppet](http://docs.puppetlabs.com/learning/) configuration files used for deployment on [htmlpad.org](http://htmlpad.org) are in the `deployment` directory. They assume a bare Ubuntu maverick server (10.10) that has Puppet 2.6.1 or later installed. The steps to deploy are:

1. Check out the HTMLpad repository to `/var/htmlpad`.

2. Run `sudo puppet /var/htmlpad/deployment/htmlpad.pp`.

You may want to also add an entry to your computer's `/etc/hosts` file to point htmlpad.org to the server that you're deploying to, since the apache configuration in the deployment sets up a virtual host for that domain.

  [Atul Varma]: http://toolness.com
