# Directories
from pathlib import Path
"""
Centralised configuration for project paths and constants.

All file system paths are defined relative to the project root
to ensure reproducibility across environments and IDEs.
"""
# Base Root
BASE_DIR = Path(__file__).resolve().parent.parent
print(BASE_DIR)

# Other
FIGURE_DIR = BASE_DIR / "figures"
DATA_DIR = BASE_DIR / "data"
DATA_ADZUNA_DIR = BASE_DIR / "data/ADZUNA_data"
