#!/usr/bin/env python3
"""
Youth Unemployment Dashboard Launcher
=====================================

Quick launcher script for the Streamlit dashboard.

Usage:
    python run_dashboard.py

Or simply:
    streamlit run app.py

Requirements:
    - Python 3.7+
    - Install dependencies: pip install -r requirements.txt
"""

import subprocess
import sys
import os
from pathlib import Path

def check_requirements():
    """Check if required packages are installed."""
    required_packages = ['streamlit', 'pandas', 'plotly', 'numpy']
    missing_packages = []

    for package in required_packages:
        try:
            __import__(package)
        except ImportError:
            missing_packages.append(package)

    if missing_packages:
        print("❌ Missing required packages:")
        for package in missing_packages:
            print(f"   - {package}")
        print("\n📦 Install with: pip install -r requirements.txt")
        return False

    return True

def check_data_file():
    """Check if the data file exists."""
    data_file = Path("data/youth_unemployment_cleaned.csv")
    if not data_file.exists():
        print("❌ Data file not found: data/youth_unemployment_cleaned.csv")
        print("📂 Please ensure you have the cleaned dataset file.")
        return False
    return True

def launch_dashboard():
    """Launch the Streamlit dashboard."""
    print("🚀 Launching Youth Unemployment Dashboard...")
    print("📊 Opening in your default web browser...")
    print("⏹️  Press Ctrl+C to stop the server")
    print("-" * 50)

    try:
        # Launch Streamlit
        cmd = [sys.executable, "-m", "streamlit", "run", "app.py"]
        subprocess.run(cmd, check=True)
    except KeyboardInterrupt:
        print("\n\n👋 Dashboard stopped by user")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error launching dashboard: {e}")
        print("💡 Try running: streamlit run app.py")
    except FileNotFoundError:
        print("❌ Streamlit not found. Please install with: pip install streamlit")

def main():
    """Main launcher function."""
    print("🌍 Global Youth Unemployment Analysis Dashboard")
    print("=" * 55)

    # Check requirements
    print("🔍 Checking requirements...")
    if not check_requirements():
        sys.exit(1)

    if not check_data_file():
        sys.exit(1)

    print("✅ All checks passed!")

    # Launch dashboard
    print("\n🌐 Starting dashboard server...")
    launch_dashboard()

if __name__ == "__main__":
    main()
