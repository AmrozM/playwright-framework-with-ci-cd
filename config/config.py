#config.py
from dotenv import load_dotenv
import os

load_dotenv()
ENV = os.getenv("ENV", "QA")

ENV_CONFIG = {
    "QA": { 
        "BASE_URL" :  "https://opensource-demo.orangehrmlive.com",
        "SCHOOL_ID" : None,
        "USERNAME" : "Admin",
        "PASSWORD" :"admin123",
        },   

      "Team5": {
          "MIS":{
            "MIS_URL": os.getenv("MIS_TEAM5_URL"),
            "SCHOOL_ID": os.getenv("MIS_TEAM5_SCHOOL_ID"),
            "MIS_USERNAME": os.getenv("MIS_TEAM5_USERNAME"),
            "MIS_PASSWORD": os.getenv("MIS_TEAM5_PASSWORD"),
                },
            "VISION":{
                "VISION_URL" : os.getenv("VISION_TEAM5_URL"),
                "CUSTOMER_CODE" : os.getenv("VISION_TEAM5_CUSTOMER_CODE"),
                "VISION_USERNAME": os.getenv("VISION_TEAM5_USERNAME"),
                "VISION_PASSWORD" : os.getenv("VISION_TEAM5_PASSWORD"),
                    }
             },
        "Release": {
            "MIS": {
            "MIS_URL": os.getenv("MIS_RELEASE_URL"),
            "SCHOOL_ID": os.getenv("MIS_RELEASE_SCHOOL_ID"),
            "MIS_USERNAME": os.getenv("MIS_RELEASE_USERNAME"),
            "MIS_PASSWORD": os.getenv("MIS_RELEASE_PASSWORD"),
            },
        "VISION": {
                "VISION_URL" : os.getenv("VISION_RELEASE_URL"),
                "CUSTOMER_CODE" : os.getenv("VISION_RELEASE_CUSTOMER_CODE"),
                "VISION_USERNAME": os.getenv("VISION_RELEASE_USERNAME"),
                "VISION_PASSWORD" : os.getenv("VISION_RELEASE_PASSWORD"),        }
        },
        "Hotfix" : {
            "MIS": {
            "MIS_URL": os.getenv("MIS_HOTFIX_URL"),
            "SCHOOL_ID": os.getenv("MIS_HOTFIX_SCHOOL_ID"),
            "MIS_USERNAME": os.getenv("MIS_HOTFIX_USERNAME"),
            "MIS_PASSWORD": os.getenv("MIS_HOTFIX_PASSWORD"),
            },
        "VISION": {
            "VISION_URL" : os.getenv("VISION_HOTFIX_URL"),
            "CUSTOMER_CODE" : os.getenv("VISION_HOTFIX_CUSTOMER_CODE"),
            "VISION_USERNAME": os.getenv("VISION_HOTFIX_USERNAME"),
            "VISION_PASSWORD" : os.getenv("VISION_HOTFIX_PASSWORD"),
        }
        }
}

# Final selected environment configuration
CONFIG = ENV_CONFIG[ENV]
ORANGE_URL = CONFIG.get("BASE_URL")

MIS_URL = CONFIG.get("MIS", {}).get("MIS_URL")
SCHOOL_ID = CONFIG.get("MIS", {}).get("SCHOOL_ID")
MIS_USERNAME = CONFIG.get("MIS", {}).get("MIS_USERNAME")
MIS_PASSWORD = CONFIG.get("MIS", {}).get("MIS_PASSWORD")
DEFAULT_TIMEOUT = 10000  # 10 seconds
VISION_URL = CONFIG.get("VISION", {}).get("VISION_URL")
CUSTOMER_CODE = CONFIG.get("VISION", {}).get("CUSTOMER_CODE")
VISION_USERNAME = CONFIG.get("VISION", {}).get("VISION_USERNAME")
VISION_PASSWORD = CONFIG.get("VISION", {}).get("VISION_PASSWORD")