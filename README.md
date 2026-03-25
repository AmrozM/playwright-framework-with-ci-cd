# Scalable Test Automation Framework using Playwright (Python), Pytest, CI, Docker & AWS

![Playwright
Tests](https://github.com/AmrozM/SDET_Folder_Structure/actions/workflows/playwright_tests.yml/badge.svg)

## Project Overview

This project is a production-ready scalable test automation framework
built using Playwright (Python) and Pytest. It supports UI and API
testing, integrates with CI pipelines, runs in Docker containers, and
supports cloud execution using AWS.

## Key Features

-   UI automation for Bromcom MIS and MAT Vision
-   API testing using Requests
-   Environment-based execution (Team5, Release, Hotfix)
-   Page Object Model (POM) design pattern
-   Custom Playwright fixtures (no pytest-playwright dependency)
-   Data-driven testing using JSON
-   Centralized logging system
-   CI integration using GitHub Actions
-   Dockerized test execution
-   AWS-based test execution (EC2)
-   Secure credential handling using GitHub Secrets

## Tech Stack

-   Python
-   Playwright
-   Pytest
-   Requests
-   GitHub Actions (CI)
-   Docker
-   AWS (EC2)
-   JSON

## Framework Architecture

-   Page Object Model (POM) for maintainability
-   Separation of concerns (tests, pages, data, utils)
-   Fixtures for browser and test setup
-   Environment-based configuration
-   Reusable utility functions

## Project Structure

    sdet_framework/
    ├── config/
    ├── pages/
    ├── tests/
    ├── test_data/
    ├── utils/
    ├── conftest.py
    ├── pytest.ini
    └── requirements.txt

## How to Run Tests

### Set Environment

    $env:ENV="Team5"

### Run All Tests

    pytest -v

### Run Specific Test

    pytest tests/test_Login_MIS_Team5.py -v

### Run in Headed Mode

    $env:HEADED="true"
    pytest -v

### Generate Report

    pytest --html=report.html

## Docker Execution

### Build Image

    docker build -t playwright-tests .

### Run Tests in Container

    docker run playwright-tests

## CI Integration

-   GitHub Actions pipeline runs on every push
-   Executes full test suite automatically
-   Uses GitHub Secrets for credentials
-   Provides execution visibility via logs and status badge

## AWS Execution

-   Tests executed on AWS EC2 instance
-   Supports scalable execution
-   Enables cloud-based testing environments

## Why This Project?

This project demonstrates real-world SDET capabilities:

-   Scalable automation framework design
-   CI/CD pipeline integration
-   Containerized execution using Docker
-   Cloud-based test execution using AWS
-   Clean, maintainable, and reusable code structure

## Author

Amroz -- QA Engineer transitioning to SDET
