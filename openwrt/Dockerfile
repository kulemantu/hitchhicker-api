# Start with a slim base image for efficiency
FROM debian:buster-slim

# Set environment variables for better script handling
ENV DEBIAN_FRONTEND=noninteractive

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
# Adjust the ports as needed
CMD ["qemu-system-x86_64", \
     "-hda", "/opt/openwrt-image.img", \
     "-boot", "c", \
     "-m", "512", \
     "-net", "nic", \
     "-net", "user,hostfwd=tcp::8080-:80,hostfwd=tcp::2222-:22"]

# Create a volume for persistent OpenWrt data
VOLUME /opt/openwrt-data

# Health check to ensure the container is running properly
# Replace 'your_health_check_command' with an appropriate command
HEALTHCHECK --interval=60s --timeout=15s --retries=3 \
  CMD your_health_check_command || exit 1
