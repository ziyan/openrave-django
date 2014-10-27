FROM debian

RUN \
    apt-get -y update && \
    apt-get -y install build-essential cmake pkg-config wget curl htop vim git libboost-dev libboost-thread-dev libboost-python-dev libboost-date-time-dev libxml2-dev libboost-regex-dev libboost-filesystem-dev libboost-system-dev octave python-dev python-pip libqt4-dev libsoqt4-dev libpcre3-dev python-scipy python-numpy xvfb && \
    rm -rf /var/lib/apt/lists/* && \
    pip install sympy

RUN \
    cd /tmp && \
    wget http://downloads.sourceforge.net/project/opende/ODE/0.13/ode-0.13.tar.bz2 && \
    tar xvpf ode-0.13.tar.bz2 && \
    cd ode-0.13 && \
    ./configure --enable-shared && \
    make && \
    make install && \
    rm -rf /tmp/ode-0.13

RUN \
    cd /tmp && \
    git clone --depth=1 --branch=latest_stable https://github.com/rdiankov/openrave.git && \
    cd openrave && \
    git checkout -qf latest_stable && \
    make && \
    make install && \
    rm -rf /tmp/openrave
