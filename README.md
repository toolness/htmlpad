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

### Installation ###

Just run `python manage.py runserver` and open your browser to [http://localhost:8000](http://localhost:8000). As you save changes to HTMLpad's source code, the server will automatically apply them, allowing you to iterate quickly.

### Troubleshooting ###

While HTMLpad is a Django application, you don't need to have Django installed system-wide. That's because running `manage.py` automatically creates a virtual environment, downloads and installs the appropriate version of Django and any other dependencies, and activates the virtual environment for the duration of the script.

However, this can sometimes result in a broken virtual environment, particularly if `manage.py` is aborted while it's still setting things up. If anything goes amiss, try wiping the `.virtualenv` directory and starting over.

### Deployment ###

You can run `python setup.py install` to install the `htmlpad` Django application package into any environment, including virtual ones.

This Django application assumes the following custom settings variables:

* `HTMLPAD_ROOT` is the string prefix, including any trailing slash but no leading slash, of the HTMLpad instance on the Web server. It can be an empty string. For example, if a user browses to http://foo.com/mypad/ to access your HTMLpad's root, then the setting's value is `'mypad/'`.

* `ETHERPAD_HOST` is the Etherpad instance that your HTMLpad delegates to, formatted as a hostname:port string.

See the [hackasaurus-puppet-data][] repository for Puppet deployment files.

### Security Considerations ###

Because the HTMLpad simply delivers universally-writeable Etherpad content as raw HTML, an HTMLpad instance should probably be served on its own dedicated domain.

  [hackasaurus-puppet-data]: https://github.com/toolness/hackasaurus-puppet-data
  [Atul Varma]: http://toolness.com
