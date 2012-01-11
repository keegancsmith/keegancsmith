:Date: 2012-01-11 15:00:00

==================================
 DNS Caching with Network Manager
==================================

I have been finding the DNS server on my router to be a bit flaky. It can take
up-to 2 seconds to resolve a domain name and does no caching. This leads to
slower network performance in applications that don't do there own DNS
caching.

There is an easy fix to this in Linux, just install dnsmasq_, enable its DNS
server and add `127.0.0.1` to your `/etc/resolv.conf`. dnsmasq then uses the
nameservers specified in `/etc/resolv.conf` (other than itself) to lookup
hostnames.

Unfortunately if you use Network Manager, it manages your `/etc/resolv.conf`
and there doesn't seem to be a way to add in custom entries on top of the ones
Network Manager receives from DHCP. However, each time Network Manager brings
up a network interface it runs the scripts in `/etc/network/if-up.d/`. The
script below prepends the nameservers `127.0.0.1` (dnsmasq's DNS server) and
`8.8.4.4` (Google's open DNS server) to `/etc/resolv.conf`.

.. literalinclude:: dnsmasq-cache
   :language: bash

Here are some step by step instructions to get it working in Ubuntu/Debian::

  $ sudo apt-get install dnsmasq
  $ # Add `listen-address=127.0.0.1` to `/etc/dnsmasq.conf`
  $ sudo /etc/init.d/dnsmasq restart
  $ # Copy the above script into a file called dnsmasq-cache
  $ chmod +x dnsmasq-cache
  $ sudo mv dnsmasq-cache /etc/network/if-up.d/

Now when Network Manager brings up an interface it should enable use of
dnsmasq's caching DNS server. Take care when configuring dnsmasq to not enable
it's DHCP server unless you intend on using it. This can cause havoc on some
LANs.

Now DNS records which haven't expired should be super quick after the first
access. On a simple test over crappy tethered internet I go from 952 msec to 0
msec for a query::

  $ dig www.uct.ac.za | grep 'Query time'
  ;; Query time: 952 msec
  $ dig www.uct.ac.za | grep 'Query time'
  ;; Query time: 0 msec

.. _dnsmasq: http://thekelleys.org.uk/dnsmasq/doc.html
