:Date: 2012-10-26 10:00:00

================================
 Suspend on Lid Close in Ubuntu
================================

I just got a new laptop (Lenovo T420s) and installed Ubuntu 12.10. The default
behaviour when closing the lid is to show a black screen and nothing else. I
don't know who prefers this use case (maybe external monitor users?) My issue
might also be that I don't use gnome-power-manager which may override the
default behaviour. What I would prefer is suspending and showing a lock screen
when the lid is opened up again.

So how do we go about fixing this? Well closing the lid sends an ACPI event,
and on Ubuntu there are a bunch of shell scripts in `/etc/acpi` which get
called depending on the event. In the case of a lid close it runs
`/etc/acpi/lid.sh`. Reading that file we can see that it runs a file
`/etc/acpi/local/lid.post.sh` if it exists and is executable.

If we save `/etc/acpi/local/lid.post.sh` as

.. literalinclude:: lid.post.sh
   :language: bash

then on suspend we run `pm-suspend` as root and `gnome-screensaver-command
--lock` for every user which has an X session running. Remember to make the
file executable::

  $ sudo chown root:root /etc/acpi/local/lid.post.sh
  $ sudo chmod 0755 /etc/acpi/local/lid.post.sh

You can pretty much do anything on lid close (and other acpi events) if you
know a bit of scripting. An example of something would be checking if any
external monitors are connected, and if they are don't suspend and switch off
the laptop screen (just a bit of xrandr magic).
