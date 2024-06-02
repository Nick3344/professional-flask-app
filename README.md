# Professional Flask App CI/CD Pipeline

This repository contains the source code and configuration for setting up a CI/CD pipeline for a professional Flask application using GitHub Actions.

## Overview

This CI/CD pipeline automates the testing, building, and deployment processes for a Flask application. It includes the following steps:

1. **Continuous Integration (CI)**:
   - On each push to the `main` branch or pull request, the CI workflow is triggered.
   - The workflow checks out the code, sets up the Python environment, installs dependencies, runs tests, and builds the Docker image.

2. **Continuous Deployment (CD)**:
   - After successful CI, the CD workflow is triggered.
   - The workflow deploys the Docker image to a Kubernetes cluster using AWS EKS.

## Prerequisites

Before setting up the CI/CD pipeline, ensure you have the following prerequisites installed and configured:

- Python 3.8 or higher
- Docker
- AWS account with permissions to deploy to EKS
- Docker Hub account for storing Docker images

## Setup Instructions

1. **Clone the Repository:**
   ```bash
   git clone <repository-url>
   cd professional-flask-app
