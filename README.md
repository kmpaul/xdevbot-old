XdevBot
=======

This is the NCAR Xdev Bot (v2).  The Bot exists to help organize Xdev activities and
work, making it easier to track issues/PRs by project.

Flask
-----

The Xdev Bot is a Flask application.  To run it, you need to first create an environment
(e.g., `conda`) with the appropriate requirements, as specified in the `requirements.txt`
file.  For exmaple, from the root directory of your clone of the `xdevbot` repository:

```bash
$ conda create --name xdevbot python
$ conda activate xdevbot
$ pip install -r requirements.txt
```

Then, to actually run the Flask application locally:

```bash
$ flask run
```

For instructions on how a Flask application works, see this tutorial:

https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world
