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
        print(f"Error: {DIRECTORY}/ directory not found. Run 'python build_local.py' first.")
        sys.exit(1)
    
    # Check if site was built for local (check index.html for baseurl)
    index_file = docs_path / 'index.html'
    if index_file.exists():
        with open(index_file, 'r', encoding='utf-8') as f:
            content = f.read(1000)  # Read first 1000 chars
            if '/new_blog/' in content:
                print("=" * 60)
                print("WARNING: Site built for production (has /new_blog/ prefix)")
                print("For local testing, rebuild with: python build_local.py")
                print("=" * 60)
                print()
    
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
