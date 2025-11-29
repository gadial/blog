#!/usr/bin/env python3
"""
Build script for local development (without baseurl prefix).
"""
import os
import sys

# Set environment variable to use local config
os.environ['USE_LOCAL_CONFIG'] = '1'

# Import and run the main build
from pathlib import Path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

from generator.site_generator import main

if __name__ == '__main__':
    print("=" * 60)
    print("LOCAL DEVELOPMENT BUILD")
    print("=" * 60)
    main()
