#!/usr/bin/env python3
"""
Build script to generate the static site.
"""
import sys
from pathlib import Path

# Add the project root to the Python path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

from generator.site_generator import main

if __name__ == '__main__':
    main()
