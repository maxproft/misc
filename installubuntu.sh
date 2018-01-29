#!/bin/bash

sudo apt-get --yes remove unity-webapps-common #amazon
sudo apt-get --yes remove indicator-messages #envelope
sudo apt-get --yes install vlc liferea wine cowsay audacity chromium-browser stellarium geogebra youtube-dl gummi ubuntu-restricted-extras gtk-recordmydesktop gimp kolourpaint4 openshot pdfshuffler vim git anki synaptic vnstat openssh-client openssh-server


sudo add-apt-repository --yes ppa:ian-berke/ppa-drawers
sudo apt-get --yes update
sudo apt-get --yes install drawers

#add in github account
git config --global user.email “email@address”
git config --global user.name “maxproft”


#Python packages
sudo apt-get --yes install python-imaging python-numpy python-scipy python-matplotlib ipython ipython-notebook python-pandas python-sympy python-nose python-matplotlib python-opencv

sudo apt-get --yes update
sudo apt-get --yes upgrade
