import os
import sys
from pathlib import Path

PROJECT_ROOT = Path(r"E:\7. ML practise Daily\7. GEN AI\10. End to End project")
sys.path.insert(0, str(PROJECT_ROOT))
sys.path.insert(0, str(PROJECT_ROOT / "src"))

from mlProject.config.configuration import ConfigurationManager
from mlProject.components.data_ingestion import DataIngestion
from mlProject import logger

try:
    logger.info("Starting pipeline...")
    config = ConfigurationManager()
    data_config = config.get_data_ingestion_config()
    data_ingestion = DataIngestion(config=data_config)
    data_ingestion.download_file()
    data_ingestion.extract_zip_file()
    logger.info(" SUCCESS!")
except Exception as e:
    print(f"Error: {e}")
