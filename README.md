# Advanced MLOps: Continuous Delivery for ML Models

## Overview
This repository contains an advanced CI/CD pipeline for a Machine Learning sentiment analysis model. The application is built using **FastAPI** for high performance and concurrency, and is containerized using a **multi-stage Docker build** to optimize image size.

## Features
- **FastAPI Web Framework:** Asynchronous and fast request handling.
- **Advanced Testing:** Comprehensive test suite using `pytest` (Normal inputs, edge cases, stress testing, and robustness).
- **Multi-stage Docker Build:** Minimized production image size (Python 3.11-slim).
- **GitHub Actions CI/CD:** Fully automated pipeline (Test -> Build -> Push to Docker Hub).

##  Prerequisites
- Python 3.11+
- Docker Desktop
- Git

##  Project Structure
- `/webapp/app.py`: FastAPI application serving the ONNX model.
- `/tests/test_app.py`: Pytest suite for functional and stress testing.
- `Dockerfile`: Multi-stage Docker configuration (optimized for production).
- `.github/workflows/advanced-ci.yml`: GitHub Actions pipeline definition.

##  How to Run Locally

1. **Install Requirements:**
   ```bash
   pip install -r requirements.txt