docker-ircpdb
=============

Playground for ircpdb. You may easily pop up a repl in
irc friendly environments :)

Usage
-----

Update the python file to the server you want to join

Build and run image with::

    docker build -t ircpdb .
    docker run ircpdb

Alternative
-----------

You may do something with python 2::

    docker run -it --rm --name python-script -v "$PWD":/usr/src/widget_app python:2 python script.py

Or python 3::

    docker run -it --rm --name python-script -v "$PWD":/usr/src/widget_app python:3 python script.py

