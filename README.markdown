# Requirements
* python2.7
* python-virtualenv
* postgresql

# Install
* create your virtualenv environment: `virtualenv --python=python2.7 --no-site-packages githost-python`
* load your virtualenv: `source githost-python/bin/activate`
* clone githost project: `git clone git://github.com/williammizuta/githost.git`
* download requirements: `cd githost && pip install -r requirements.txt`

# Run server
* load your virtualenv: `source githost-python/bin/activate`
* start server: `python manage.py runserver`
* access http://localhost:8000 in your browser

# Run tests
* load your virtualenv: `source githost-python/bin/activate`
* run tests: `python manage.py test`
