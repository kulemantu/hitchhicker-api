# OpenWrt Docker Compose Setup

This directory contains the resources for setting up an OpenWrt virtual machine within a Docker container using Docker Compose. This setup uses QEMU to virtualize OpenWrt.

## Overview

The `Dockerfile` and `docker-compose.yml` files streamline the process of building and running an OpenWrt VM. Docker Compose simplifies the management of service configuration, network settings, and persistent storage.

## Prerequisites

- Docker and Docker Compose installed on your machine.
- The OpenWrt `.img` file placed in this directory, named `openwrt-image.img`.

## OpenWrt Image File

Download the OpenWrt image file compatible with QEMU from the following URL (replace the placeholder URL with the actual link):

`[Download OpenWrt Image](https://downloads.openwrt.org/releases/23.05.2/targets/x86/generic/)`

## Building and Running with Docker Compose

### Create a Docker network hitchnet

Create the Docker network used by the OpenWRT machine and other common containers.

```bash
docker network create hitchnet
```

### Building the Docker Image

Navigate to this directory and run the following command:

```bash
docker-compose build
```

This command uses the `Dockerfile` to build an image named `openwrt-qemu`.

### Running the OpenWrt Container

To start the OpenWrt virtual machine, execute:

```bash
docker-compose up
```

Add `-d` to the command to run the container in detached mode.

### Accessing OpenWrt

Once the container is up, access the OpenWrt web interface via `http://localhost:8080` and SSH at `localhost` on port `2222`.

## Configuration

### Ports

The `docker-compose.yml` file is configured to forward the following ports:

- Port `8080` on the host to port `80` on the container for the web interface.
- Port `2222` on the host to port `22` on the container for SSH.

### Persistent Storage

A Docker volume named `openwrt_data` is used for persistent storage. This volume is mapped to `/opt/openwrt-data` inside the container.

### Health Check

The container includes a health check command. Replace the placeholder in `docker-compose.yml` with a suitable command for your OpenWrt setup.

## Stopping the Container

Use the following command to stop and remove the container:

```bash
docker-compose down
```

## Additional Information

For more details on configuration options, networking, and troubleshooting, refer to the OpenWrt, QEMU, and Docker documentation.

---

_**Note:** This README assumes a basic understanding of Docker, Docker Compose, and command-line operations._
