Title: Docker on Raspberry Pi 3
Date: 2019-08-06
Category: Docker, Raspberry
Tags: docker, raspberry, electronics, system
Slug: docker-raspberry
Summary: Installing Docker on Raspberry Pi 3
Status: published

## Docker on Raspberry Pi 3

### What and why?

Docker is a tool similar to virtual machine but without its performance overhead.
It allows to create totally separated conteneraized environments which use a host machine kernel.
So it is as fast as when you run it natively while creating containers or using already built images is a quite easy and pleasant process.
For more information about Docker, check sources at the bottom of the page.

Docker is great, so why not use it on Raspberry (RPi)?
Usually when I play with RPi I break something in the system or SD card stops working, so I have to reinstall the system and go again through the installation steps.
It is not difficult and there are plenty of tutorials which show how do it.
I've found that almost everyone of them is different and most don't work from start to end as they are supossed to.
So to make my life slightly easier I prepared a short description how to set-up RPi and a short python script which installs Docker and docker-compose while I go to the kitchen and prepare hot cup of tea.
Moreover, this script does not have to be downloaded, just copy-paste one line to the terminal and your earl gray is ready to be brewed.

### Setting up Raspbian

Download [*Raspbian Buster Lite*](https://www.raspberrypi.org/downloads/raspbian/) and create a bootable SD-card. For this purpose you can use for e.g. ***Startup Disk Creator*** (Ubuntu) or ***Etcher*** (Windows, Mac, Linux).

If you use a headless RPi it is possible to enable SSH and Wi-Fi before the first boot.\
To enable SSH you have to put an empty file named `ssh` onto the boot partition without any extension.

For Wi-Fi you need to define `wpa_supplicant.conf` (configuration file for Wi-Fi Protected Access client and IEEE 802.1X supplicant) on the boot partition as well.
This file shall contain credentials for your network.

```
# wpa_supplicant.conf

ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
country=«your_ISO-3166-1_two-letter_country_code»

network={
    ssid="«your_SSID»"
    psk="«your_PSK»"
    key_mgmt=WPA-PSK
}
```

### Docker installation

Installation is provided by a simple script which executes just 6 shell commands. I will describe each one of them briefly.

<script src="https://gist.github.com/TobKed/75337ec7b73a0ac59a415b837927e4ee.js"></script>

The meaning of particular commands:

<ul>
  <li><code>sudo apt-get update</code>
  downloads the package lists from the repositories and "updates" them to get information on the newest versions of packages and their dependencies.
    <ul>
      <li> <code>sudo</code> - executes command as the superuser.</li>
      <li> <code>apt-get</code> -  the command-line tool for handling packages.</li>
      <li> <code>update</code> - option used to re-synchronize the package index files from their sources.</li>
    </ul>
  </li>
  <li> <code>curl -sSL https://get.docker.com | sh</code> 
    installs docker by executing Docker installation script from an online source.
    <ul>
      <li> <code>curl</code> - tool to transfer data from or to a server.
      <li> <code>--s/--silent</code> - silent or quiet mode. Doesn't show progress meter or error messages.</li>
      <li> <code>-S/--show-error</code> - when used with -s it makes curl show an error message if it fails.</li>
      <li> <code>-L/--location</code> - if the server reports that the requested page has moved to a different location (indicated with a Location: header and a 3XX response code), this option will make curl redo the request on the new place.</li>
      <li> <code>|</code> - pipes '|' send the output of one command as input of another command.</li>
      <li> <code>sh</code> - Bourne shell.</li>
    </ul>
  </li>
  <li> sudo usermod -aG docker $USER`\
  adds your user to the docker group which is created during the installation to run docker commands without without prepending sudo (as non-root user)
    <ul>
      <li> <code>usermod</code> - modified a user account.</li>
      <li> <code>--a, --append</code> - adds the user to the supplementary group(s). Use only with the -G option.</li>
      <li> <code>-G, --groups</code> - a list of supplementary groups.</li>
      <li> <code>docker</code> - group name.</li>
      <li> <code>$USER</code> - environmental variable with username.</li>
    </ul>
  </li>
  <li> <code>sudo systemctl enable docker</code>\
    configures Docker to start on boot
    <ul>
      <li> <code>systemctl</code> - may be used to introspect and control the state of the "systemd" system and service manager.</li>
      <li> <code>enable NAME..., enable PATH...</code> - Enables one or more units or unit instances.</li>
      <li> <code>docker</code> - deamon process name.</li>
    </ul>
  </li>
  <li> <code>sudo apt-get install -y python3-pip</code>
    installs package installer for Python 3
    <ul>
      <li> <code>install</code> -  this option is followed by one or more packages desired for installation.</li>
      <li> <code>-y, --yes, --assume-yes</code> automatic yes to prompts. Assume "yes" as answer to all prompts and run non-interactively.</li>
      <li> <code>python3-pip</code> - Python3 package installer.</li>
    </ul>
  </li>
  <li> <code>sudo pip3 install docker-compose</code>
    installs docker-compose through Python package installer
      <ul>
        <li> <code>pip3</code> - a recursive acronym for "Pip Installs Packages"</li>
        <li> <code>install</code> - argument for pip3, self-explanatory.</li>
        <li> <code>docker-compose</code> - name of package to be installed.</li>
      </ul>  
  </li>
</ul>

To run this script you just have to copy-paste the following line in the RPi terminal:

```bash
curl -sSL https://gist.githubusercontent.com/TobKed/75337ec7b73a0ac59a415b837927e4ee/raw/docker_on_raspbian.py | python3
```

It executes (similar to `curl -sSL https://get.docker.com | sh`) this script posted on [github gist](https://gist.github.com/TobKed/75337ec7b73a0ac59a415b837927e4ee#file-docker_on_raspbian-py).

After script successfully finishes you can run subshell as a docker user by executing `newgrp docker` (`newgrp` - change the current group ID (GID) during a login session) or restart RPi by `sudo shutdown -r now` (recommended).

<br>

______________________________________________________________________

#### Sources:

<ul>
  <li><a href="https://www.docker.com/">docker homepage</a></li>
  <li><a href="https://pythonspeed.com/docker/">Docker packaging guide for Pythond</a></li>
  <li><a href="https://www.raspberrypi.org/downloads/raspbian/">Raspbian download</a></li>
  <li><a href="https://en.wikipedia.org/wiki/Startup_Disk_Creator">Startup Disk Creator</a></li>
  <li><a href="https://www.balena.io/etcher/">Etcher</a></li>
  <li><a href="https://www.raspberrypi.org/documentation/remote-access/ssh/README.md">SSH (Secure Shell) - Raspberry Pi Documentation</a></li>
  <li><a href="https://www.raspberrypi.org/documentation/configuration/wireless/headless.md">Setting up a Raspberry Pi headless - Raspberry Pi Documentation</a></li>
  <li><a href="https://www.systutorials.com/docs/linux/man/8-wpa_supplicant/">wpa_supplicant - systutorials.com</a></li>
  <li><a href="https://www.systutorials.com/docs/linux/man/5-wpa_supplicant.conf/">wpa_supplicant.conf - systutorials.com</a></li>
  <li><a href="https://raspberrypi.stackexchange.com/questions/10251/prepare-sd-card-for-wifi-on-headless-pi">Prepare SD card for Wifi on Headless Pi - Raspberry Pi Stack Exchangev</a></li>
  <li><a href="https://linux.die.net/man/8/apt-get">apt-get(8) - Linux man page</a></li>
  <li><a href="https://linux.die.net/man/1/curl">curl(1) - Linux man page</a></li>
  <li><a href="https://www.geeksforgeeks.org/piping-in-unix-or-linux/">Piping in Unix or Linux - GeeksforGeeks</a></li>
  <li><a href="https://www.computerworld.com.au/article/279011/-z_programming_languages_bourne_shell_sh">The A-Z of Programming Languages: Bourne shell, or sh - Computerworld</a></li>
  <li><a href="https://linux.die.net/man/8/usermod">usermod(8) - Linux man page</a></li>
  <li><a href="https://docs.docker.com/install/linux/linux-postinstall/#configure-docker-to-start-on-boot">Post-installation steps for Linux - Configure Docker to start on boot - docker.com</a></li>
  <li><a href="http://man7.org/linux/man-pages/man1/login.1.html#DESCRIPTION">($USER) login(1) - Linux manual page</a></li>
  <li><a href="https://packages.debian.org/buster/python3-pip"> Details of package python3-pip in buster - Debian</a></li>
  <li><a href="https://pip.pypa.io/en/stable">pip - The Python Package Installer documentation</a></li>
  <li><a href="https://pip.pypa.io/en/stable/reference/pip_install/">pip install - The Python Package Installer documentation</a></li>
  <li><a href="https://pypi.org/project/docker-compose/">docker-compose · PyPI</a></li>
  <li><a href="https://www.computerhope.com/unix/unewgrp.htm">Linux newgrp command help and examples - computerhope</a></li>
  <li><a href="https://www.youtube.com/watch?v=3N3n9FzebAA">dotScale 2013 - Solomon Hykes</a>
    <div class="videoWrapper" style="height:0; padding-bottom:56.25%; padding-top:25px; position:relative" height="0">
      <iframe style="position:absolute; top:0; width:100%" height="100%" width="100%" src="https://www.youtube-nocookie.com/embed/3N3n9FzebAA" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </div>
  </li>
  <li><a href="https://www.youtube.com/watch?v=VhabrYF1nms">Building Python apps with Docker - PyTexas</a>
    <div class="videoWrapper" style="height:0; padding-bottom:56.25%; padding-top:25px; position:relative" height="0">
      <iframe style="position:absolute; top:0; width:100%" height="100%" width="100%" src="https://www.youtube-nocookie.com/embed/VhabrYF1nms" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </div>
  </li>
</ul>
