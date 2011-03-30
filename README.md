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

See the [hackasaurus-puppet-data][] repository for Puppet deployment files.

  [hackasaurus-puppet-data]: https://github.com/toolness/hackasaurus-puppet-data
  [Atul Varma]: http://toolness.com
