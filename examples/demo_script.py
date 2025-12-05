# DEMO SCRIPT – KEY FUNCTIONS

import sys
import os

# Add project ROOT to Python path (not src directly)
script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(script_dir, ".."))
sys.path.append(project_root)

from src.library_name import (
    check_password_strength,
    advanced_password_evaluation,
    generate_strong_password,
    is_common_password
)
