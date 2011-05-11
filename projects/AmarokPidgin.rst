==============
 AmarokPidgin
==============

:Author: Keegan Carruthers-Smith <keegan.csmith@gmail.com>
:Version: 0.2.2
:Date: March 2009
:URL: http://people.cs.uct.ac.za/~ksmith/projects/AmarokPidgin.html
:Download: http://www.kde-apps.org/content/show.php?content=48025
:Mercurial: http://bitbucket.org/keegan_csmith/amarokpidgin/overview/

.. contents::

Description
===========

A plugin for Amarok 1 and 2 that updates your Pidgin status message with what
you are currently listening to.

If you want to update your Gaim status message, look for the AmarokGaim
package.


Dependencies
============

* Amarok (Tested on Amarok 1.4.10 or Amarok 2.0-SVN-Neon Jan 14 2009)
* Pidgin with D-Bus support (Tested on Pidgin 2.5.2)
* Python with D-Bus support (Tested on Python 2.5.2 (Should also work with
  Python 2.4))
* DCOP client (If using Amarok 1. Tested on KDE 3.5.10)
* Optionally depends on chardet for better character
  decoding. [http://chardet.feedparser.org/]


Configuration
=============

* Supported variables in **STATUS_MESSAGE** are:

  - $album
  - $artist
  - $genre
  - $title
  - $track
  - $year
  - $nowPlaying
  - $lyricsURL
  - $lyrics
  - $rating
  - $score

* *$lyrics* variable displays a single line from the lyrics of the song. The
  lyrics must be fetched by Amarok first.
* More configuartion options can be found in *AmarokPidgin.ini*, which can be
  found in *~/.kde/share/apps/amarok/scripts-data/*
* To edit the list of expletives edit *censor_words* in
  *AmarokPidgin.ini*. Words are | separated


Variable Map
============

All variables that go in the **STATUS_MESSAGE** can now be filtered by a user
supplied function. This is done using the configuration options
**variable_map** and **variable_imports**. **variable_map** is a function
which accepts 2 strings (Variable, Value) and returns a
string. **variable_imports** runs possible imports required for
**variable_map**.

Examples
--------

* Quote ::

   variable_map = lambda x,y : y and ("'"+y+"'") or ''

* Unknown String ::

   variable_map = lambda x,y : y or ("Unknown " + x.capitalize())

* iPodify strings ::

   variable_map = lambda x,y : ' '.join(['i' + s.capitalize() for s in y.split()])


Amarok 2
========

AmarokPidgin now has rudimentary Amarok 2 support. It does not support many of
the variables, updating your buddy icon and configuration from Amarok. To
configure you have to edit *AmarokPidgin.ini*, which can be found in
*~/.kde/share/apps/amarok/scripts/AmarokPidgin*.


License
=======

This software is distributed under the GPLv2. Please read COPYING for more
information.


Changelog
=========

* Version 0.2.2 (Development)

  - Buddy Icon support for Amarok 2.

  - Passive Popup in Amarok 1 when a user tries to configure who does not have
    kdialog installed.

* Version 0.2.1 (03/03/2009)

  - Executible bit was not switched on! So could not install in Amarok 1.

* Version 0.2 (11/02/2009)

  - Your Buddy Icon can now be set to the currently playing song's album
    cover. Set *cover_icon* to true in the config file to enable.
  - Made Media status type "tune". To update:

    + Stop AmarokPidgin in Amarok
    + Delete Media status in Pidgin
    + Start AmarokPidgin in Amarok

  - New variables $rating and $score.

* Version 0.1.9 (16/05/2008)

  - New variables: $year, $nowPlaying, $lyricsURL and $lyrics. Based on a
    patch by Hieu Hoang.
  - Variable Map. Based on work by Ryan Davis.
  - Seems to work with Pidgin 2.4.0 now.
  - Media status is of type Avaliable now by default.

* Version 0.1.8 (09/02/2008)

  - Can use chardet library to decode strings.
  - Testing of the new decoding routine thanks to David Partain.
  - Fixed bug with status not returning to Media.
  - Quick hack to prevent crashes on debugging output.

* Version 0.1.7 (02/08/2007)

  - Closes script when Amarok sends SIGTERM. (Thanks to Kiyoshi Murata)
  - Only media status is updated. No changing status anymore on song change.
  - Pausing only changes status if status is on Media. (Thanks to Vasilis
    Vasaitis)

* Version 0.1.6 (27/05/2007)

  - Changed project name to AmarokPidgin
  - Updated codebase to use purple. With thanks to the following
    contributors:

    + Tony Bassette
    + Thomas Bird
    + Luigi Capriotti

* Version 0.1.5 (05/04/2007)

  - Can now change nick instead of status message.
  - Updates to unicode handling.
  - Updates status type if necessary (Thanks to Vasilis Vasaitis)

* Version 0.1.4 (20/11/2006)

  - Fixed a bug with misbehaving kdialogs. (Thanks to Kartik Mohta)
  - Now changes Gaim's status back too default when script closes.
  - Updates status if a song is playing when the script starts.

* Version 0.1.3 (14/11/2006)

  - Now can block expletives in status message.
  - Fixed a bug when reading in the configuration file.

* Version 0.1.2 (02/11/2006)

  - Fixed unicode strings bug. (Thanks too Tim Su)
  - Added basic configuration

* Version 0.1.1 (30/10/2006)

  - Forgot to comment out logging =/

* Version 0.1 (25/10/2006)

  - Initial Release
