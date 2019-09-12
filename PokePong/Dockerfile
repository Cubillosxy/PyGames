# AUTHOR:   Edwin Cubillos
# SETUP:
#
#   docker build -t .
#
#
#   UBUNTU:
#   docker run -it -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=unix$DISPLAY pyg /bin/bash
#
#   MAC:
#       brew install socat
#       socat TCP-LISTEN:6000,reuseaddr,fork UNIX-CLIENT:\"$DISPLAY\"
#
#   in other window
#       run ifcongi and look for the ip of vboxnet0, say 192.168.99.1
#       docker run -i -t -e DISPLAY=192.168.99.1:0 pyg /bin/bash
#

# FROM ubuntu:18.04
FROM python3

MAINTAINER Edwin Cubillos

RUN apt-get update && apt-get install -y \
    mercurial \
    libav-tools \
    libsdl-image1.2-dev \
    libsdl-mixer1.2-dev \
    libsdl-ttf2.0-dev \
    libsmpeg-dev \
    libsdl1.2-dev \
    libportmidi-dev \
    libswscale-dev \
    libavformat-dev \
    libavcodec-dev \
    libplib-dev \
    libopenal-dev \
    libalut-dev \
    libvorbis-dev \
    libxxf86vm-dev \
    libxmu-dev \
    libgl1-mesa-dev \
    python-dev \
    python-pip \
    python-pygame \
    git


ENTRYPOINT ["/bin/bash"]