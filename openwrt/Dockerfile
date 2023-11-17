# Start with a slim base image for efficiency
FROM debian:buster-slim

# Set environment variables for better script handling
ENV DEBIAN_FRONTEND=noninteractive

# Set file path for python script
ENV FLASK_APP=../server/app.py

# Update system and install specific version of QEMU
# Replace 'x.x.x' with the desired version number
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y --no-install-recommends qemu-system-x86=1:3.1+dfsg-8+deb10u8 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Copy the OpenWrt image into the container
COPY openwrt-image.img /opt/

# Set up networking configuration
# This example sets up user-mode networking with port forwarding
CMD ["qemu-system-x86_64", \
     "-hda", "/opt/openwrt-image.img", \
     "-boot", "c", \
     "-m", "512", \
     "-net", "nic", \
     "-net", "user,hostfwd=tcp::8080-:80,hostfwd=tcp::2222-:22"]

# Create a volume for persistent OpenWrt data
VOLUME /opt/openwrt-data

# Expose ports for SSH and HTTP
EXPOSE 8080 2222 80 22

# Update opkg
RUN opkg update

# Install Python and PIP package
RUN opkg install python3 python3-pip

# Install Flask
RUN pip3 install flask

# Copy the Python script via ENV into the container
COPY ${FLASK_APP} /opt/server

# Run the Python script
RUN python3 /opt/server/app.py