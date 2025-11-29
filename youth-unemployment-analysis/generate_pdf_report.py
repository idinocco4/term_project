#!/usr/bin/env python3
"""
PDF Report Generation Script

This script converts the Markdown report to PDF format using pandoc.
Requires pandoc and LaTeX to be installed.

Usage:
    python generate_pdf_report.py

Requirements:
    - pandoc (https://pandoc.org/)
    - LaTeX distribution (e.g., MacTeX on macOS, TeX Live on Linux)
    - Python packages: subprocess, pathlib

Alternative: Use online Markdown to PDF converters or export from tools like Typora.
"""

import subprocess
import sys
from pathlib import Path

def generate_pdf_report():
    """Convert Markdown report to PDF using pandoc."""

    # Define file paths
    script_dir = Path(__file__).parent
    markdown_file = script_dir / "reports" / "youth_unemployment_report.md"
    pdf_file = script_dir / "reports" / "youth_unemployment_report.pdf"

    # Check if markdown file exists
    if not markdown_file.exists():
        print(f"Error: Markdown file not found at {markdown_file}")
        return False

    try:
        # Pandoc command to convert Markdown to PDF
        cmd = [
            "pandoc",
            str(markdown_file),
            "-o", str(pdf_file),
            "--pdf-engine=pdflatex",
            "--variable", "geometry:margin=1in",
            "--variable", "fontsize=11pt",
            "--variable", "colorlinks=true",
            "--variable", "linkcolor=blue",
            "--variable", "urlcolor=blue",
            "--variable", "citecolor=blue",
            "--toc",
            "--toc-depth=2",
            "--number-sections"
        ]

        print("Converting Markdown to PDF...")
        print(f"Input: {markdown_file}")
        print(f"Output: {pdf_file}")

        # Run pandoc command
        result = subprocess.run(cmd, capture_output=True, text=True)

        if result.returncode == 0:
            print("✅ PDF report generated successfully!")
            print(f"📄 File saved to: {pdf_file}")
            return True
        else:
            print("❌ Error generating PDF:")
            print("STDOUT:", result.stdout)
            print("STDERR:", result.stderr)
            return False

    except FileNotFoundError:
        print("❌ Error: pandoc not found. Please install pandoc:")
        print("   macOS: brew install pandoc")
        print("   Ubuntu: sudo apt-get install pandoc texlive-latex-base")
        print("   Windows: Download from https://pandoc.org/installing.html")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False

def check_requirements():
    """Check if required tools are installed."""
    requirements = ["pandoc", "pdflatex"]
    missing = []

    for tool in requirements:
        try:
            result = subprocess.run([tool, "--version"],
                                  capture_output=True, text=True, check=True)
        except (subprocess.CalledProcessError, FileNotFoundError):
            missing.append(tool)

    if missing:
        print("⚠️  Missing requirements:")
        for tool in missing:
            print(f"   - {tool}")
        print("\nPlease install missing tools and try again.")
        return False

    print("✅ All requirements satisfied.")
    return True

if __name__ == "__main__":
    print("PDF Report Generation Tool")
    print("=" * 30)

    # Check requirements
    if not check_requirements():
        sys.exit(1)

    # Generate PDF
    success = generate_pdf_report()

    if success:
        print("\n🎉 Report generation complete!")
        print("📖 The PDF report is ready for distribution.")
    else:
        print("\n💥 Report generation failed.")
        print("🔧 Please check the error messages above.")
        sys.exit(1)
