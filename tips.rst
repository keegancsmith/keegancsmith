.. -*- mode: rst -*-

=================
 Tips and Tricks
=================

:Author: Keegan Carruthers-Smith <ksmith@cs.uct.ac.za>
:Info: A collection of useful things documented so I don't forget.


.. contents::


I use the Emacs notation for key bindings (shortcuts). For example
"C-c C-a" means press control and c at the same time, then push
control and a at the same time. "M-<space>" means press the modifier
key (alt on most keyboards) and space at the same time. I also don't
include any links because Google works. This document was written in
Emacs using reST with the rst mode. To see the reST/plain text version
look at tips.rst



KDE
===

Useful Programs
---------------

kioslaves
  Read up on the different KIO-Slaves. Awesome ones include fish, smb and info.
Yakuake
  Drop down console, quake style.
Katapult
  Searches menu for quick launching. Press M-space to activate. Pressing C-c
  while its activated to configure.
Amarok
  Best music manager for large collections.


SSH
===

Useful Programs
---------------

fish://
  KIO-Slave in KDE for browsing remote file systems over SSH in konqueror.
sshfs
  FUSE file system from mounting file systems over SSH.
tramp
  Emacs mode for editing remote files. Sometimes sshfs makes more sense, but
  otherwise tramp is quick and painless


Useful Flags
------------

-n  Redirects stdin from /dev/null. Useful in scripts where SSH is called many
    times. Without the flag a script will terminate after the first instance
    of SSH has executed.
-C  Compression
-L  Local tunnel. port:host:hostport
-R  Remote tunnel. port:host:hostport
-D  SOCKS server. specify the port to listen on.
-N  Prevents execution of remote commands (Nice for tunneling)
-A  Forward ssh-agent
-X  Enable X11 Forwarding
-o  Passing extra options. StrictHostKeyChecking=no to prevent host key checks.

ssh_config
----------

An example SSH config that I use in the TSL lab. Read man page for
ssh_config for more.  This file is stored in ~/.ssh/config ::

  # Any PC on the uct.ac.za sub domain defaults to using my student number as my
  # username
  Host *.uct.ac.za
  User smtkee002

  # SSH public keys for actual PC's in the TSL lab seem to change often. This
  # ignores changes in the host key. This option is prone to man in the middle
  # attacks! (It disables the yes/no prompt about known hosts)
  Host pc??.tsl.uct.ac.za
  StrictHostKeyChecking no

  # Makes it possible to type 'ssh tsl' instead of 'ssh tsl.uct.ac.za'
  Host tsl
  User smtkee002
  Hostname tsl.uct.ac.za

  # Makes it possible to type 'ssh casper' instead of 'ssh casper.cs.uct.ac.za'
  Host casper
  User ksmith
  Hostname casper.cs.uct.ac.za


Tunneling
---------

Useful for making connections look like they are coming from another
machine.  A common usage is for accessing machines which are
firewalled off from you. There are a few proxies that are only
accessible from certain IP's at UCT, this makes it possible for you to
access them from any machine with SSH.

For example, say you can't access the proxy *cache* which is on port
*3128*. You can ssh into *remote* which can access it. If you run ::

  ssh -C -L 9999:cache:3128 remote -N

and then set your HTTP proxy to be *localhost* on port *9999* you will
have a working proxy.


SSH into multiple machines
--------------------------

Here's some *bash* for executing a command on a few machines. The
command run is *last* which returns a list of the last few logins. ::

  for host in "pc1 pc2 pc3"; do echo ------ $host -----; ssh -n $host last -a -n 10; done



Screen
======

Useful Key Bindings
-------------------

C-a d
  Detach a screen instance. (Put it into the background). To re-attach run
  screen -r
C-a c
  Create a new window
C-a n
  Go to next window
C-a p
  Go to previous window
C-a C-a
  Switch to last active window


Emacs
=====

Useful Key Bindings
-------------------

General
~~~~~~~

C-x C-f
  Open file
C-x C-s
  Save file
C-x C-c
  Close Emacs
C-h b
  Show a list of all defined keys, with what command they call.
M-x command
  Makes it possible to run any interactive command that is defined. This
  supports tab completion.

Formatting
~~~~~~~~~~

C-space
  Mark the start of a region
C-w
  Cut from the start of a region to the cursor
M-w
  Copy from the start of a region to the cursor
C-k
  Cut from the cursor to the end of the line
C-y
  Paste
M-y
  Scroll through kill ring. (Use after C-y)
C-_
  Undo
M-q
  Reformat a paragraph so that it fits in 80-columns. (Can do comments as well)

Window
~~~~~~

C-x 0
  Close the current window (If its not the only one)
C-x 1
  Make this window the only open one.
C-x 2
  Split window into horizontally
C-x 3
  Split window vertically
C-x o
  Go to next window
C-x b
  Switch to another buffer

Macros
~~~~~~

C-x (
  Start defining a keyboard macro
C-x )
  End the definition of a keyboard macro
C-x e
  Execute the most recent keyboard macro
C-u C-x (
  Re-execute last keyboard macro, then add more keys to its definition.



Org-mode
--------

I use the config from
http://www.newartisans.com/blog_files/org.mode.day.planner.php. Here
is a summary of the shortcuts described:

C-M-r
  Adds a new TODO using remember
C-c C-s
  Schedule a task
C-c C-d
  Schedule a deadline
C-c C-x C-s
  Archive tasks
C-c a a
  Weekly agenda view
d
  Switch to day view in the agenda buffer
\.
  Switch to current day in the agenda buffer
\,
  Change priorities of a task in the agenda buffer
C-u t
  Change state of a task in the agenda buffer



Useful Minor-Modes
------------------

flymake
  On the fly syntax checking
flyspell
  On the fly spell checking
column-number
  Displays the column number of the cursor
line-number
  Displays what line number the cursor is on
display-time
  Displays the time
ido-mode
  Better buffer switching and file finding


Flymake
-------
You need this target in your Makefile for flymake to work. CC and CFLAGS need to
be defined by your Makefile. ::

  check-syntax:
        $(CC) $(CFLAGS) -Wextra -fsyntax-only $(CHK_SOURCES)


My .emacs file
--------------

My emacs file is split over more than one file, but this file sets most things
that come installed with emacs. Tested on Emacs CVS (currently v23.0.60.1)

.. code-block:: cl

  ;; emacs general config. Should work with a bare install of emacs
  
  ;; Xft support if using 23
  (if (>= emacs-major-version 23)
      (set-frame-font "Bitstream Vera Sans Mono-9"))
      ;;(set-default-font "Andale Mono-11"))
  
  ;; Email
  (setq user-full-name "Keegan Carruthers-Smith")
  (setq user-mail-address "keegan.csmith@gmail.com")
  
  
  ;; Highlight matching brackets
  (show-paren-mode 1)
  
  
  ;; Get rid of stupid GUI stuff
  (if (fboundp 'scroll-bar-mode) (scroll-bar-mode -1))
  (if (fboundp 'tool-bar-mode) (tool-bar-mode -1))
  (if (fboundp 'menu-bar-mode) (menu-bar-mode -1))
  
  
  ;; Indentation
  (set-variable 'c-basic-offset 4)
  (c-set-offset 'access-label -2)
  (c-set-offset 'case-label '+)
  (add-hook 'html-mode-hook
            (lambda ()
              (setq indent-line-function 'indent-relative)))
  
  
  ;; Yes-or-No queries become Y-or-N
  (fset 'yes-or-no-p 'y-or-n-p)
  
  
  ;; Full Screen Mode
  (defun fullscreen ()
    (interactive)
    (set-frame-parameter nil 'fullscreen
                         (if (frame-parameter nil 'fullscreen) nil 'fullboth))
    (display-time-mode (if (frame-parameter nil 'fullscreen) 1 0)))
  
  
  ;; Shift arrow key to move between windows/panes
  (windmove-default-keybindings)
  
  
  ;; IDO
  (ido-mode t)
  (setq ido-enable-flex-matching t)
  
  
  ;; Misc settings
  (setq
   inhibit-startup-message t
   x-select-enable-clipboard t
   make-backup-files nil
   column-number-mode t
   case-fold-search t
   current-language-environment "English"
   compilation-window-height 18
   compilation-scroll-output t
   save-abbrevs nil
   font-lock-maximum-decoration t
   tramp-default-method "ssh"
   tramp-auto-save-directory "~/.emacs.d/tramp-autosave")
  (global-font-lock-mode 1)
  
  ;; Misc buffer settings
  (setq-default
   fill-column 78
   indent-tabs-mode nil)
  
  
  ;; Shortcuts
  (global-set-key (kbd "<f5>")     'previous-error)
  (global-set-key (kbd "<f6>")     'next-error)
  (global-set-key (kbd "<f7>")     'flymake-mode)
  (global-set-key (kbd "<f8>")     'add-change-log-entry-other-window)
  (global-set-key (kbd "<f9>")     'compile)
  (global-set-key (kbd "<f11>")    'fullscreen)
  (global-set-key (kbd "C-g")      'goto-line)
  (global-set-key (kbd "C-d")      'comment-region)
  (global-set-key (kbd "C-S-d")    'uncomment-region)
  (global-set-key (kbd "<delete>") 'delete-char)
  (global-set-key (kbd "C-c c")    'comment-dwim)
  
  
  ;; Shortcuts for easier window resizing
  (global-set-key (kbd "S-C-<left>")  'shrink-window-horizontally)
  (global-set-key (kbd "S-C-<right>") 'enlarge-window-horizontally)
  (global-set-key (kbd "S-C-<down>")  'shrink-window)
  (global-set-key (kbd "S-C-<up>")    'enlarge-window)
  
  
  ;; Enable Full Screen mode
  (fullscreen)


Bash
====

Read a file line by line ::

  cat file | while read line; do echo $line; done

C-like for loop ::

  for i in $(seq 1 10); do echo $i; done

C-like for loop 2 ::

  for ((i=1; i <= 10; i++)); do echo $i; done


Pathname Expansion
------------------

From the bash man page. *pattern-list* is a list of one or more patterns
separated by a \|.  Composite patterns may be formed using one or more of the
following sub-patterns:

?(pattern-list)
  Matches zero or one occurrence of the given patterns
\*(pattern-list)
  Matches zero or more occurrences of the given patterns
+(pattern-list)
  Matches one or more occurrences of the given patterns
@(pattern-list)
  Matches one of the given patterns
!(pattern-list)
  Matches anything except one of the given patterns
