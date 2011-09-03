## HTMLpad ##

By [Atul Varma][]

This is a simple Web application that, for any URL path, serves the
contents of an Etherpad with the same path with the MIME type
`text/html`.

For example, if the application is served from htmlpad.org and the
Etherpad backend it's configured to use is at
etherpad.mozilla.org:9000, then visiting http://htmlpad.org/foo
will deliver the contents of http://etherpad.mozilla.org:9000/foo as
HTML.

This effectively allows people to easily collaborate on writing HTML,
and it provides a very fast feedback loop between trying something
out, seeing how it looks in the browser, and sharing it with others.

### Quick Start ###

To get started, run this at your shell prompt:

    git clone --recursive git://github.com/hackasaurus/htmlpad.git
    cd htmlpad/htmlpad_dot_org
    python manage.py runserver

Then open your browser to [http://localhost:8000](http://localhost:8000). As you save changes to HTMLpad's source code, the server will automatically apply them, allowing you to iterate quickly.

### Deployment ###

This Django application assumes the following custom settings variables:

* `HTMLPAD_ROOT` is the string prefix, including any trailing slash but no leading slash, of the HTMLpad instance on the Web server. It can be an empty string. For example, if a user browses to http://foo.com/mypad/ to access your HTMLpad's root, then the setting's value is `'mypad/'`.

* `ETHERPAD_HOST` is the Etherpad instance that your HTMLpad delegates to, formatted as a hostname:port string.

See the [hackasaurus-puppet-data][] repository for Puppet deployment files.

### Security Considerations ###

Because the HTMLpad simply delivers universally-writeable Etherpad content as raw HTML, an HTMLpad instance should probably be served on its own dedicated domain.

  [hackasaurus-puppet-data]: https://github.com/toolness/hackasaurus-puppet-data
  [Atul Varma]: http://toolness.com
