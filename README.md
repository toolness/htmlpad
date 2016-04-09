## HTMLpad

By [Atul Varma][]

This is a simple Web application that, for any URL path, serves the
contents of an [Etherpad][] with the same path with the MIME type
`text/html`.

For example, if the application is served from htmlpad.org and the
Etherpad backend it's configured to use is at
etherpad.mozilla.org:9000, then visiting http://htmlpad.org/foo
will deliver the contents of https://public.etherpad-mozilla.org/p/foo as
HTML.

This effectively allows people to easily collaborate on writing HTML,
and it provides a very fast feedback loop between trying something
out, seeing how it looks in the browser, and sharing it with others.

## Requirements

* Python 2.7
* [pip and virtualenv](http://stackoverflow.com/q/4324558)

## Quick Start

```
virtualenv venv

# On Windows, replace the following line with 'venv\Scripts\activate'.
source venv/bin/activate

pip install -r requirements.txt
python manage.py runserver
```

Then open your browser to http://localhost:8000. As you save changes to
HTMLpad's source code, the server will automatically apply them, allowing
you to iterate quickly.

## Environment Variables

Unlike traditional Django settings, we use environment variables
for configuration to be compliant with [twelve-factor][] apps.

**Note:** When an environment variable is described as representing a
boolean value, if the variable exists with *any* value (even the empty
string), the boolean is true; otherwise, it's false.

**Note:** When running `manage.py`, `DEBUG` is enabled.

* `DEBUG` is a boolean value that indicates whether debugging is enabled
  (this should always be false in production).
* `AUTO_COLLECTSTATIC` is a boolean that determines whether to
  automatically run `manage.py collectstatic` when the WSGI app is
  instantiated. Useful for certain production deployments, such as Heroku.
* `HTMLPAD_ROOT` is the string prefix, including any trailing slash but no
  leading slash, of the HTMLpad instance on the Web server. For example,
  if a user browses to http://foo.com/mypad/ to access your HTMLpad's root,
  then the setting's value is `'mypad/'`. Defaults to an empty string.
* `ETHERPAD_PROTOCOL` is the protocol of the Etherpad instance that
  your HTMLpad delegates to. Defaults to 'https'.
* `ETHERPAD_HOST` is the Etherpad instance that your HTMLpad delegates to,
  formatted as a hostname:port string. Defaults to 'public.etherpad-mozilla.org'.

### Security Considerations ###

Because the HTMLpad simply delivers universally-writeable Etherpad content
as raw HTML, an HTMLpad instance should probably be served on its own
dedicated domain.

<!-- Links -->

  [Etherpad]: https://github.com/ether/etherpad-lite
  [twelve-factor]: http://12factor.net/
  [Atul Varma]: http://toolness.com
