

# import os

# def print_deep_structure(root_dir, indent=""):
#     try:
#         for item in sorted(os.listdir(root_dir)):
#             path = os.path.join(root_dir, item)
#             if os.path.isdir(path):
#                 print(f"{indent}📁 {item}/")
#                 print_deep_structure(path, indent + "    ")
#             else:
#                 print(f"{indent}📄 {item}")
#     except PermissionError:
#         print(f"{indent}⛔ [Permission Denied] {root_dir}")
#     except Exception as e:
#         print(f"{indent}⚠️ [Error] {root_dir}: {e}")

# # Example usage
# if __name__ == "__main__":
#     root_path = "src"  # You can change this to any folder you want to explore
#     print(f"\n📦 Project structure under: {root_path}\n")
#     print_deep_structure(root_path)


# import os

# def generate_tree(root_dir, indent=""):
#     for item in sorted(os.listdir(root_dir)):
#         path = os.path.join(root_dir, item)
#         if os.path.isdir(path):
#             print(f"{indent}├── {item}/")
#             generate_tree(path, indent + "│   ")
#         else:
#             print(f"{indent}├── {item}")

# # Example usage
# if __name__ == "__main__":
#     root_path = "."  # Current directory (project root)
#     print(f"{os.path.basename(os.path.abspath(root_path))}/")
#     generate_tree(root_path)


import os
import sys
from pathlib import Path

# Set absolute path
PROJECT_ROOT = Path(r"E:\7. ML practise Daily\7. GEN AI\10. End to End project")
sys.path.insert(0, str(PROJECT_ROOT / "src"))

# Test the fixed constants
import src.mlProject.constants as constants
constants.CONFIG_FILE_PATH = PROJECT_ROOT / "config" / "config.yaml"

print("Testing ConfigurationManager with fixed paths...")
from mlProject.config.configuration import ConfigurationManager

try:
    config_manager = ConfigurationManager()
    print("✅ ConfigurationManager works!")
    
    # Test data ingestion config
    data_ingestion_config = config_manager.get_data_ingestion_config()
    print("✅ Data ingestion config:", data_ingestion_config)
    
except Exception as e:
    print(f"❌ Error: {e}")