# SDET FRAMEWORK

## Project Overview
This project automates UI and API testing. UI tests cover OrangeHRM 
login and Bromcom MIS login with navigation to Student profile across 
multiple environments (Team5, Release, Hotfix). Also with the help of ENV variables test can now run on both Products 
i.e MIS and Vision just by using a single env variable ex: Team5
API tests cover JSONPlaceholder API validation. Custom Playwright fixtures are used 
instead of pytest-playwright plugin. Logger is implemented for 
test execution visibility.

## Tech Stack
- Python
- Playwright (sync_api)
- Pytest
- Requests (API testing)

## Framework Structure
```
sdet_framework/
├── config/         → Environment config (URLs, credentials)
├── pages/          → Page Object Model classes
├── tests/          → Test files
├── test_data/      → json files having test data
├── utils/          → Logger and helpers
├── conftest.py     → Custom Playwright fixtures
├── pytest.ini      → Pytest configuration
└── requirements.txt
```

## How to Run Tests

Run specific test for MIS:
```bash
pytest tests/test_Login_MIS_Team5.py -v
```

Run specific test:
```bash
pytest tests/test_login_vision.py -v
```

Run with logs:
```bash
pytest tests/test_login_vision.py -v -s
```

Run all tests:
```bash
pytest -v
```

## Environment Variables

Set environment (PowerShell):
```powershell
$env:ENV="QA"      # OrangeHRM QA
$env:ENV="Team5"   # MIS Team5 server
$env:ENV="Release" # MIS Release server
$env:ENV="Hotfix"  # MIS Hotfix server
```

Run headed (browser visible):
```powershell
$env:HEADED="true"
pytest tests/test_Login_MIS_Team5.py -v
```