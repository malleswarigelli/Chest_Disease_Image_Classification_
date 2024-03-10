
# custom log, no time stamp used in this project (this way new log replaces the old log, saves computing resources)

import os
import sys
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

log_dir = "logs"
log_filepath = os.path.join(log_dir,"running_logs.log")
os.makedirs(log_dir, exist_ok=True)


logging.basicConfig(
    level= logging.INFO,
    format= logging_str,

    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout) # prints log in terminal along with running_logs.log file
    ]
)

logger = logging.getLogger("cnnClassifierLogger")