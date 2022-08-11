=============
 AmarokQuilt
=============

:Author: Keegan Carruthers-Smith <keegan.csmith@gmail.com>
:Version: 0.0.2
:Date: September 2008
:URL: http://people.cs.uct.ac.za/~ksmith/projects/AmarokQuilt.html
:Download: http://www.kde-apps.org/content/show.php/AmarokQuilt?content=83429
:Mercurial: https://github.com/keegancsmith/AmarokQuilt


.. contents::


Description
===========

A Full Screen mode for Amarok which displays a quilt of your album covers as
well as the current playing track.

In beta stage, **expect bugs**.


Installation
============

Run the following commands::

  $ qmake
  $ make

Then to run it run::

  $ ./amarokquilt

To install the screen saver copy *AmarokQuilt.desktop* to
*~/.kde/share/applnk/System/ScreenSavers/* and make sure *amarokquilt* is
somewhere on the path.


Changelog
=========

* Version 0.0.2 (8 September 2008)

  - Border around covers
  - Screensaver support
  - Picks album size with regards to screensize
  - Reduces the chances of showing an album cover more than once
  - Unicode support

* Version 0.0.1 (16 June 2008)

  - Initial release featuring basic animations
