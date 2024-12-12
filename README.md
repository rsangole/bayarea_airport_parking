# Bay Area Airport Parking

[![Docker Image CI](https://github.com/rsangole/bayarea_airport_parking/actions/workflows/docker-image.yml/badge.svg)](https://github.com/rsangole/bayarea_airport_parking/actions/workflows/docker-image.yml)
[![Build Status](https://github.com/rsangole/bayarea_airport_parking/actions/workflows/fetch_data.yml/badge.svg)](https://github.com/rsangole/bayarea_airport_parking/actions/workflows/fetch_data.yml)
[![Docker Pulls](https://img.shields.io/docker/pulls/hatmatrix/bayarea_airport_parking)](https://hub.docker.com/r/hatmatrix/bayarea_airport_parking)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/)


## Overview

This project fetches and processes parking data for San Francisco International Airport (SFO). The time-series data is collected and stored in a CSV file for further analysis.

## Features

- Fetches real-time parking data from SFO's website every hour.
- Processes and stores the data in a CSV file.
- Uses Docker for containerization.
- Automated data fetching using GitHub Actions.


## Usage

The main script `fetch_data.py` fetches the parking data and appends it to `data.csv`. The script ensures that the directory exists and handles appending data correctly.

## GitHub Actions

The project uses GitHub Actions to automate the data fetching process. The workflow is defined in `fetch_data.yml` and runs every hour to update the file.

## License

This project is licensed under the MIT License.