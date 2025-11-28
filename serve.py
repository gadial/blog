#!/usr/bin/env python3
"""
Simple HTTP server to preview the generated site locally.
"""
import http.server
import socketserver
from pathlib import Path
import sys
import webbrowser
import threading
import time

PORT = 8000
DIRECTORY = "docs"

def open_browser():
    """Open browser after a short delay."""
    time.sleep(1)
    webbrowser.open(f'http://localhost:{PORT}')

if __name__ == '__main__':
    # Change to docs directory
    docs_path = Path(__file__).parent / DIRECTORY
    if not docs_path.exists():
        print(f"Error: {DIRECTORY}/ directory not found. Run 'python build.py' first.")
        sys.exit(1)
    
    # Create handler
    Handler = http.server.SimpleHTTPRequestHandler
    
    # Start server
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Serving site at http://localhost:{PORT}/")
        print(f"Directory: {docs_path.absolute()}")
        print("Press Ctrl+C to stop")
        print()
        
        # Open browser in background
        threading.Thread(target=open_browser, daemon=True).start()
        
        # Change to docs directory and serve
        import os
        os.chdir(docs_path)
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down server...")
