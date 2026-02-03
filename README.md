# One-Click CI/CD Dockerized Web App

# Overview
This project demonstrates a basic DevOps workflow for a simple Flask web application.
The focus of this project is not the application itself, but how an application can be
containerized, automatically verified, and run reliably using DevOps practices.



# What the App Does
- A simple Flask web application
- Displays a static message in the browser
- Runs on port 5000

The application is intentionally simple so that the focus remains on DevOps concepts.


# DevOps Workflow Implemented

# 1. Containerization (Docker)
- The application is packaged using Docker
- All dependencies (Python, Flask) are included inside the Docker image
- The app runs the same way on any machine with Docker installed

# 2. Continuous Integration (GitHub Actions)
- A CI pipeline is triggered automatically on every push to GitHub
- The pipeline builds the Docker image to verify:
  - Dockerfile correctness
  - Dependency installation
  - Application build validity
- This ensures broken code is detected early

# 3. System Provisioning (Docker Compose)
- Docker Compose is used to define how the system runs
- The entire application can be built and started using a single command
- This removes manual Docker commands and reduces human error

# 4. Debugging & Failure Handling
- The project includes intentional break-and-fix exercises
- Errors in application code, Dockerfile, and configuration were debugged using logs
- This simulates real DevOps troubleshooting scenarios


# How to Run the Project

# Prerequisites
- Docker Desktop installed
- Git installed

# Run with Docker Compose
```bash
docker compose up
