import logging
import os
from datetime import datetime
import sys

LOG_FILE = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
logs_dir = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_dir, exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s]  %(lineno)d %(name)s %(levelname)s - %(message)s",
    level=logging.INFO,
)

class customException(Exception):
    def __init__(self, message, sys_module):
        super().__init__(message)
        self.sys_module = sys_module
        

    