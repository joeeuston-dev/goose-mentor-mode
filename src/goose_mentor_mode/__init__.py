import argparse
from .server import mcp
from .mentor_toolkit import MentorToolkit
from .mentor_engine import MentorConfig

def main():
    """Goose Mentor Mode: AI-powered mentor extension that transforms automation into guided learning."""
    parser = argparse.ArgumentParser(
        description="AI-powered mentor extension for Goose that transforms automation into guided learning."
    )
    parser.parse_args()
    mcp.run()

if __name__ == "__main__":
    main()
