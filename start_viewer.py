#!/usr/bin/env python3
"""
Start local HTTP server for Golden Data Viewer
"""

import http.server
import socketserver
import webbrowser
import os
from pathlib import Path

PORT = 8000

def main():
    # Change to doc directory
    doc_dir = Path(__file__).parent
    os.chdir(doc_dir)

    Handler = http.server.SimpleHTTPRequestHandler

    print("=" * 60)
    print("CardioWatch 287-2B - Golden Data Viewer")
    print("=" * 60)
    print()
    print(f"Starting HTTP server on port {PORT}...")
    print(f"Server URL: http://localhost:{PORT}/golden_data_viewer.html")
    print()
    print("Press Ctrl+C to stop the server")
    print()

    # Open browser automatically
    try:
        webbrowser.open(f"http://localhost:{PORT}/golden_data_viewer.html")
        print("[OK] Browser opened automatically")
    except:
        print("[INFO] Please open the URL manually in your browser")

    print()
    print("-" * 60)

    # Start server
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n\nServer stopped.")
            print("Thank you for using Golden Data Viewer!")

if __name__ == "__main__":
    main()
