# Use Ubuntu as the base image
FROM ubuntu:22.04

# Set environment variables
ENV DEBIAN_FRONTEND=noninteractive
ENV WINEDEBUG=-all
ENV WINEARCH=win64
ENV WINEPREFIX=/root/.wine

# Install required packages
RUN apt-get update && apt-get install -y \
    wget \
    gnupg2 \
    software-properties-common \
    winbind \
    cabextract \
    xvfb \
    python3 \
    python3-pip \
    python3-setuptools \
    && rm -rf /var/lib/apt/lists/*

# Install WINE
RUN dpkg --add-architecture i386 && \
    mkdir -pm755 /etc/apt/keyrings && \
    wget -O /etc/apt/keyrings/winehq-archive.key https://dl.winehq.org/wine-builds/winehq.key && \
    wget -NP /etc/apt/sources.list.d/ https://dl.winehq.org/wine-builds/ubuntu/dists/jammy/winehq-jammy.sources && \
    apt-get update && \
    apt-get install -y --install-recommends winehq-stable && \
    rm -rf /var/lib/apt/lists/*

# Install winetricks
RUN wget https://raw.githubusercontent.com/Winetricks/winetricks/master/src/winetricks -O /usr/local/bin/winetricks && \
    chmod +x /usr/local/bin/winetricks

# Create WINE prefix and install Windows Python
RUN wine wineboot --init && \
    sleep 5 && \
    winetricks -q win10

# Download and install Python for Windows
RUN wget https://www.python.org/ftp/python/3.10.11/python-3.10.11-amd64.exe -O /tmp/python-installer.exe && \
    wine /tmp/python-installer.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0 && \
    sleep 10 && \
    rm /tmp/python-installer.exe

# Create working directory
WORKDIR /app

# Copy your application files
COPY . /app/

# Install Windows Python packages
RUN wine python -m pip install pyinstaller selenium

# Build the exe with PyInstaller
RUN xvfb-run wine python -m PyInstaller --noconfirm --onefile --windowed --add-data "./iphone_notification.mp3;." vierdaagse.py

# Set the entrypoint
ENTRYPOINT ["bash", "-c", "echo 'Build complete! Your exe is in the dist folder.' && tail -f /dev/null"]