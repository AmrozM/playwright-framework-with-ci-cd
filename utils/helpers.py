from pathlib import Path
from datetime import datetime

def to_ms(seconds:float) -> int:
    return int(seconds *1000)

def take_screenshot(page, name):
    Path("screenshots").mkdir(exist_ok=True)
    page.screenshot(path=f"screenshots/{name}_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.png")
    