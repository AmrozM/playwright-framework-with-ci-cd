#conftest.py

import os
import pytest
from playwright.sync_api import sync_playwright, Playwright, Browser, BrowserContext, Page
from config.constants import BASE_URL, DEFAULT_TIMEOUT

def _to_bool(val: str | None, default=False) -> bool:
    if val is None:
        return default
    return val.strip().lower() in ("1", "true", "yes", "y", "on")

@pytest.fixture(scope="session")
def browser_settings():
    """Configure browser behavior via environment variables."""
    return {
        "headless": _to_bool(os.getenv("HEADLESS"), True),
        "headed": _to_bool(os.getenv("HEADED"),False),
        "slowmo": int(os.getenv("SLOWMO", "0")), 
        "base_url": os.getenv("BASE_URL", BASE_URL),
        "viewport": {"width": 1366, "height": 768},
        "video": _to_bool(os.getenv("VIDEO"), False),
          }

@pytest.fixture(scope="session")
def browser(playwright_instance: Playwright, browser_settings):
    browser = playwright_instance.chromium.launch(
        headless= not browser_settings["headed"] and browser_settings["headless"],
        slow_mo=browser_settings["slowmo"],
    )
    yield browser
    browser.close()

@pytest.fixture(scope="function")
def context(browser: Browser, browser_settings) -> BrowserContext:
    context = browser.new_context(
        viewport=browser_settings["viewport"],
        base_url=browser_settings["base_url"],
        )
    yield context
    context.close()

@pytest.fixture(scope="function")
def page(context: BrowserContext) -> Page:
    page = context.new_page()
    page.set_default_timeout(DEFAULT_TIMEOUT)
    yield page
    page.close()
    
@pytest.fixture(scope="session")
def playwright_instance() -> Playwright:
    with sync_playwright() as p:
     yield p