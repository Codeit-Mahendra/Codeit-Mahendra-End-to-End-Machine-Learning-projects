import os
import sys
import logging

# Define log format
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

# Create logs directory if it doesn't exist
log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)

# Define log file path
log_filepath = os.path.join(log_dir, "running_logs.log")

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

# Create logger instance
logger = logging.getLogger("mlProjectLogger")