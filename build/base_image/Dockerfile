
# Use Kali Linux as the base image
FROM kalilinux/kali-rolling

# Avoid tzdata asking for geographic area and timezone
ENV DEBIAN_FRONTEND=noninteractive

# Update and Install Dependencies
RUN apt update \
    && apt install -y --no-install-recommends \
    build-essential \
    wget \
    libssl-dev \
    libffi-dev \
    libsqlite3-dev \
    libbz2-dev \
    libreadline-dev \
    zlib1g-dev \
    nmap \