[![circleci](https://img.shields.io/circleci/build/gh/ncar-xdev/xdevbot?label=circleci)](https://circleci.com/gh/ncar-xdev/xdevbot)
[![codecov](https://img.shields.io/codecov/c/gh/ncar-xdev/xdevbot?label=codecov)](https://codecov.io/gh/ncar-xdev/xdevbot)
[![license](https://img.shields.io/github/license/ncar-xdev/xdevbot)](http://www.apache.org/licenses/LICENSE-2.0)
[![release](https://img.shields.io/github/v/release/ncar-xdev/xdevbot)](https://github.com/ncar-xdev/xdevbot/releases/latest)
XdevBot
=======

This is the NCAR Xdev Bot (v2).  The Bot exists to help organize Xdev activities and
work, making it easier to track issues/PRs by project.

aiohttp
-------

This Bot application is build using `aiohttp`, an asynchronous web server/client
framework for Python 3.5+.  If you are unfamiliar with asynchronous programming in
Python (namely, Python 3.5+'s `asyncio`), then you should read up on it here:

- https://docs.python.org/3/library/asyncio.html
- https://realpython.com/async-io-python/

The `aiohttp` package provides a web server and client that uses this fundamental
`asyncio` functionality.  To learn more about `aiohttp`, you can read up on it here:

- https://docs.aiohttp.org/en/v3.0.1/tutorial.html#aiohttp-tutorial

motor
-----

This Bot is designed to work with MongoDB for persistent data storage.  MLab
provides a cloud-based MongoDB DBaaS which has a free "sandbox" level (512 MB).
The Bot does not need much storage, so we use this service for free, but we may
need to upgrade to a paid service in the future, or switch to a different DB
solution.

The recommended `asyncio`-compatible driver for MongoDB is `motor`.  The tutorial
for `motor` with `asyncio` can be found here:

- https://motor.readthedocs.io/en/stable/tutorial-asyncio.html

Heroku
------

This Bot is also designed to run on Heroku.  It is not large or demanding, so we
do not need to pay for anything, yet.  The launch command that is needed for the
Bot to run on Heroku is stored in the `Procfile` file, and the version of Python
needed to run is specified in the `runtime.txt` file.

CircleCI
--------

This Bot also has continuous integration enabled with CircleCI.  This means that
Heroku can be used to autodeploy when CI tests pass.

Running Locally
---------------

To run this application locally, you need simply run:

```bash
$ python -m xdevbot
```

However, this application uses `click` for its CLI, which means you can get the
full help description with:

```bash
$ python -m xdevbot --help
Usage: xdevbot [OPTIONS]

Options:
  --version          Show the version and exit.
  --host TEXT        Server IP address
  --port INTEGER     Server port number
  --logging INTEGER  Logging output level
  --config PATH      User-defined configuration file location
  --help             Show this message and exit.
```
