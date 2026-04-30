\# Advanced MLOps: Continuous Delivery for ML Models



\## Overview

This repository contains an advanced Continuous Integration and Continuous Delivery (CI/CD) pipeline for a Machine Learning sentiment analysis model. The application is built using \*\*FastAPI\*\* for high performance and concurrency, and is containerized using a \*\*multi-stage Docker build\*\* to optimize image size.



\## Features

\- \*\*FastAPI Web Framework:\*\* Asynchronous and fast request handling.

\- \*\*Advanced Testing:\*\* Comprehensive test suite using `pytest` (Normal inputs, edge cases, stress testing, and robustness).

\- \*\*Multi-stage Docker Build:\*\* Minimized production image size.

\- \*\*GitHub Actions CI/CD:\*\* Fully automated pipeline that runs tests, builds the Docker image, and pushes it to Docker Hub.



\## Project Structure

\- `/webapp/app.py`: FastAPI application serving the ONNX model.

\- `/tests/test\_app.py`: Pytest suite for functional and stress testing.

\- `Dockerfile`: Multi-stage Docker configuration.

\- `.github/workflows/advanced-ci.yml`: GitHub Actions pipeline.



\## How to Run Locally



1\. \*\*Install Requirements:\*\*

&#x20;  ```bash

&#x20;  pip install -r requirements.txt

