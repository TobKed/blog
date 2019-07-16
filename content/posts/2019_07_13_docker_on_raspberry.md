Title: Docker on Raspberry Pi 3
Date: 2019-07-13
Modified: 2010-7-13 16:24
Category: Docker, Raspberry
Tags: docker, raspberry, electronics, system
Slug: docker-raspberry
Summary: Installing Docker on Raspberry Pi 3
Status: draft


## Docker on Raspberry Pi 3

### What and why?

### Setting up Raspbian
Download <a>[*Raspbian Buster Lite*](https://www.raspberrypi.org/downloads/raspbian/) <a name="1">[[1]](#raspbian)</a> and create bootable SD-card. For this purpose you can use for e.g. ***Startup Disk Creator*** (Ubuntu) or ***Etcher*** (Windows, Mac, Linux).

If you use headless PI it is possible enable SSH and Wifi before first boot.
Put onto the boot partition a file named `ssh` without any extension.
For Wifi you need to define `wpa_supplicant.conf` on the boot partition as well. This file shall contain credentials for you network

```
network={
    ssid="«your_SSID»"
    psk="«your_PSK»"
}
```

### Docker installation

<a name="1">[[2]](#docker)


<br>

----------------
#### Sources:
* <a name="raspbian">[[1]](#1)</a> [Raspbian download](https://www.raspberrypi.org/downloads/raspbian/)
* <a name="raspbian">[[2]](#2)</a> [docker.com](https://www.docker.com/)
* https://www.balena.io/etcher/
* https://en.wikipedia.org/wiki/Startup_Disk_Creator
* https://www.raspberrypi.org/documentation/remote-access/ssh/README.md
* https://www.raspberrypi.org/documentation/configuration/wireless/headless.md
