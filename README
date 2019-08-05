# RCC book

This uses [Sphinx with
Markdown](https://docs.readthedocs.io/en/stable/intro/getting-started-with-sphinx.html),
and the dependencies are listed in `requirements.txt` and set up using `virtualenv` via:

```
source venv/bin/activate
pip install -r requirements.txt
```

To regenerate the static HTML from the Markdown chapter sources, first
run:

```
make html
```

To launch the web server, it'd be a better idea to run Nginx+Gunicorn
or some comparable WSGI-ish framework, but this trivial example simply
runs the Flask app on port `8080` via:

```
nohup ./app.py 8080
```

So far, this has only been run on Ubuntu 18.04 LTS and Mac OSX 10.13.6
but it's relatively generic HTML + JavaScript from Sphinx and nothing
especially tricky in Flask.
