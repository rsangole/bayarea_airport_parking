# Source: https://www.rhosignal.com/posts/uv-in-docker/

# Use a multi-stage build to first get uv
FROM ghcr.io/astral-sh/uv:0.5.7 as uv
# Choose your python version here
FROM python:3.12-slim-bookworm
# Create a virtual environment with uv inside the container
RUN --mount=from=uv,source=/uv,target=./uv \
    ./uv venv /opt/venv
# We need to set this environment variable so that uv knows where
# the virtual environment is to install packages
ENV VIRTUAL_ENV=/opt/venv
# Make sure that the virtual environment is in the PATH so
# we can use the binaries of packages that we install such as pip
# without needing to activate the virtual environment explicitly
ENV PATH="/opt/venv/bin:$PATH"

# Copy the requirements file into the container
COPY requirements.txt .
# Install the packages with uv using --mount=type=cache to cache the downloaded packages
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=from=uv,source=/uv,target=./uv \
    ./uv pip install  -r requirements.txt

RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    vim \
    wget \
    sudo\
    jq\
    curl\
    libgit2-dev \
    make \
    tmux \
    && rm -rf /var/lib/apt/lists/*
