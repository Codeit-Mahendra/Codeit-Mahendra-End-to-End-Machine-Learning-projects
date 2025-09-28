
# from pathlib import Path

# CONFIG_FILE_PATH = Path("config/config.yaml")
# PARAMS_FILE_PATH = Path("params.yaml")
# SCHEMA_FILE_PATH = Path("schema.yaml")


from pathlib import Path
import os

# In src/mlProject/constants/__init__.py

def get_project_root():
    """Get absolute path to project root"""
    current_file = Path(__file__)
    # 4 parents are used because __file__ is in: __init__.py -> constants -> mlProject -> src -> Project_Root
    # YOU MIGHT NEED TO CHANGE THIS '4' TO '3' OR '5'
    return current_file.parent.parent.parent.parent

PROJECT_ROOT = get_project_root()

# Use absolute paths
CONFIG_FILE_PATH = PROJECT_ROOT / "config" / "config.yaml"
PARAMS_FILE_PATH = PROJECT_ROOT / "params.yaml"
SCHEMA_FILE_PATH = PROJECT_ROOT / "schema.yaml"

# Verify paths
print(f"Project root: {PROJECT_ROOT}")
print(f"Config path: {CONFIG_FILE_PATH}")
print(f"Config exists: {CONFIG_FILE_PATH.exists()}")