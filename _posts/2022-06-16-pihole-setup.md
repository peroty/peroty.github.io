---
title: Pi-hole setup
date: 2022-06-16 16:06:00 - 500
categories: [Pi-hole, docker] 
tag: [Pi-hole, setup] # All lowercase
layout: post

---

I decided it was time to setup a Pi-hole on the raspberry pi zero w that's been sitting idle. I wanted to get it running on both my Pi4 running docker and this pi zero as a backup so if one was out of comission, reboot, or (most likely) if I broke something, I wouldn't lose my DNS server.

## Pi-hole on a Pi Zero W

The Pi Zero W installation went smoothly.

I was confident I could install Pi-hole, but I wasn't sure how best to get unbound up and running. So I followed Craft Computing's excellent walkthrough.

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/FnFtWsZ8IP0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

The key was to grab the [unbound configuration from the example](https://docs.pi-hole.net/guides/dns/unbound/#configure-unbound) site without a single edit.

Seriously, take this whole file, save it where they tell you and restart. I am sure there is some editing or tweaking I can (should?) be doing. But as for going from Zero to Working, this could not have been easier.

## Pi-hole on Docker on a Pi 4

For Pi-hole on Docker, I am using the excellent template compiled by Novaspirit Tech as part of his [pi-hosted youtube series](https://www.youtube.com/playlist?list=PL846hFPMqg3jwkxcScD1xw2bKXrJVvarc).

[novaspirit/pi-hosted: Raspberry Pi Self Hosted Server Based on Docker / Portainer.io](https://github.com/novaspirit/pi-hosted/)

If you need a tutorial, I used the [pi-hole and unbound installation](https://github.com/novaspirit/pi-hosted/blob/master/docs/pi-hole.md#pi-hole-unbound-installation)

For the Pi-hole on docker, I ran into a bit of a problem. Everything worked, but there was still an error message I was seeing.

`[1655407674] unbound[537:0] warning: so-rcvbuf 1048576 was not granted. Got 360448. To fix: start with root permissions(linux) or sysctl bigger net.core.rmem_max(linux) or kern.ipc.maxsockbuf(bsd) values.
`

I had only a vague notion of what this meant to so I went looking and found a straight forward answer from [Telesphoreo](https://github.com/MatthewVance/unbound-docker-rpi/issues/4#issuecomment-1001879602).

> For anyone who is having this problem (even on non Docker) the solution is to edit the `/etc/sysctl.conf` file and add this line somewhere in the file: `net.core.rmem_max=1048576`
> 
> After I rebooted, you can now run `sudo service unbound status` and no more error! I'm posting the solution here since this is the first thing that shows up on google when you search for it hope that's okay

Perfect. I connected to the console of the docker container in Portainer, tried to run nano, installed nano with from apt, then made the correction and restarted the docker container. No more error. :)

### Next Steps

* Accessorize!
    
    I plan to get either a hat for pi zero to give it ethernet, or get a USB to ethernet adapter. For now, it's a backup and runs off wifi but I'd like to get it wired and then stash it next to my router.

* Sync!

    I saw Techno Tim has a video about syncing instances of Pi-hole together. [High Availability Pi-Hole? Yes please!](https://www.youtube.com/watch?v=IFVYe3riDRA) Now that I've got two instances running, I'd like them to know about each other and sync them. If I make changes, I don't want to have to remember to do this twice.

* WAF Testing

    Similar to User Acceptance Testing, the Wife Acceptance Factor is a vital part of anything that affect the entire house. Last time I played with Pi-hole, it broke weird things when she'd click through things from Instagram and other places.

* Groups

    I see that Pi-hole has groups so that might be part of the answer. Setup some devices to run through this DNS and adblocker and send some directly through to the internet.

* Add Pi-hole to Wireguard VPN

    When I [setup wireguard](https://github.com/novaspirit/pi-hosted/blob/master/docs/wireguard-install.md) I did not have a working Pi-hole installation at the time so I skipped it. Now that I have not one, but two Pi-holes, I want to run the VPN through them so when I am connecting remotely, I will get the additional ad-blocking features. Since I use [Google Fi](https://g.co/fi/r/Y0HHPW) as my cell phone provider, any ads and auto-playing videos I can block will save me money on my bill.