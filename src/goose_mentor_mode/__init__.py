import argparse
from .server import mcp

def main():
    """Goose Mentor Mode: AI-powered mentor extension that transforms automation into guided learning."""
    parser = argparse.ArgumentParser(
        description="AI-powered mentor extension for Goose that transforms automation into guided learning."
    )
    parser.parse_args()
    mcp.run()

if __name__ == "__main__":
    main()
