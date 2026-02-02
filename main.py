"""Main entry point for the application."""

import sys
from Backend.main import start_backend


def main():
    """Main application function."""
    print("Starting application...")
    print("Backend initialization...")
    start_backend()
    print("Application running successfully!")


if __name__ == "__main__":
    main()