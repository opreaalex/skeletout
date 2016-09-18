#skeletout
A skeleton generator written in Go for Flask web applications
==========

Description
-----------

This project was created quickly bootstrap a project.
Right now, it only supports the creation of Flask (Python micro-framework) projects.
I started working on skeleout because I wanted to learn the Go programming language.

Installation
------------

Use "go get" to bring the project to your machine:

    go get github.com/opreaalex/skeletout
    
Documentation
-------------

To use skeletout, you must first build the project:

    cd $GOPATH/src/github.com/opreaalex/skeletout

    go build

And finally, to run it we do:

    ./skeletout -a test-application -o $HOME/test-application

This command will generate a ready to use Flask web application.
The generated app is based on mattupstate's overholt, which can be found here: https://github.com/mattupstate/overholt

License
-------

The MIT License (MIT)

See LICENCE for more.

Author
------

Alexandru Oprea
