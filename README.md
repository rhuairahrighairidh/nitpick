#nitpick - A visualisation library for [NuPIC](https://github.com/numenta/nupic)

A library of plots and automatic model state saving (courtesy of [Cerebro2](https://github.com/numenta/nupic.cerebro2)) designed to make it easy to visualize what is going on inside a HTM model.
This library was designed to be straght forwards to use and easy to contribute to.

For an idea of what this can do (and to see some nice pictures) see the [HotGymDemo](http://nbviewer.ipython.org/github/rhuairahrighairidh/nitpick/blob/master/nitpick/documentation/HotGymDemo.ipynb)

Or to start using it, follow the installation instructions below then and have a look at
 - the [Introduction Demo](http://nbviewer.ipython.org/github/rhuairahrighairidh/nitpick/blob/master/nitpick/documentation/IntroductionDemo.ipynb)
 - and [the documentation](http://nbviewer.ipython.org/github/rhuairahrighairidh/nitpick/blob/master/nitpick/documentation/ContentsPage.ipynb)

This project is still very much in the proof of concept phase.  
If you'd like to help out then then have a look at the [HowToAddANewPlot](http://nbviewer.ipython.org/github/rhuairahrighairidh/nitpick/blob/master/nitpick/documentation/HowToAddANewPlot.ipynb) guide.

Note: all IPython notebook in this repo can be viewed using IPython's nb viewer website here:  http://nbviewer.ipython.org/github/rhuairahrighairidh/nitpick/tree/master/

This project is part of the 2014 Season of NuPIC.


##Installation Instructions

This library can be fully installed using the standard python package manager ```pip```

To install run the following:

    pip install https://github.com/rhuairahrighairidh/nitpick/archive/master.zip

To uninstall run:

    pip uninstall nitpick

This library is designed to be used alongside IPython. It doesn't require IPython to be installed but if you want to install ipython run:

    pip install ipython[all]
    
This installs ipython and makes sure all its dependencies are installed. (just running ```pip install ipython``` will not allow you to run the ipython notebook)

###Additional guidlines:

The above works fine but using virtualenv is generally a better method.
For an introduction see [A non-magical introduction to Pip and Virtualenv for Python beginners](http://www.dabapps.com/blog/introduction-to-pip-and-virtualenv-python/)

If you install this in a virtualenv then it will install numpy and matplotlib as well. This takes a while. You can get round the wait if you have these two installed on your system. In this case tell virtualenv to use the system packages by adding on the option "--system-site-packages" when creating your virtualenv. Like this

    virtualenv myNewEnv --system-site-packages

Now when a package is not found in the virtualenv, python will look in the system wide location as well.


##Contributor Installation
The above installation will work fine if you want to use this library. But if you might contribute then follow these instructions:

uninstall nitpick if its already installed

    pip uninstall nitpick

clone the repo

    git clone https://github.com/rhuairahrighairidh/nitpick
    
use pip to install

    pip install -e path/to/the/cloned/nitpick/repo

This will install nitpick but point the installation at the files in the repo. So if you modify anything it doesn't need reinstalling

Again you might want to do this inside a virtual env.


