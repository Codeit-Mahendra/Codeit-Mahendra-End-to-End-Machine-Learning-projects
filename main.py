import sys
import os

# Dynamically add 'src' to the Python path
src_path = os.path.join(os.path.dirname(__file__), 'src')
sys.path.append(src_path)

from mlProject.logging import logger

logger.info("This is our custom log! _ My name Mahendra")