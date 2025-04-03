"""
Configuration for tests.
"""

import os
import sys

# Add parent directory to path so we can import from src
path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, path)
