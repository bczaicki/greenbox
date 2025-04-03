"""
Command-line interface for GreenBox.
"""

import argparse
import logging
import sys

import yaml

from ..controller import GreenBoxController


def setup_logging(verbose=False):
    """Set up logging configuration."""
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(
        level=level,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler("greenbox.log"),
        ],
    )


def load_config(config_file):
    """Load configuration from YAML file."""
    try:
        with open(config_file, "r") as f:
            return yaml.safe_load(f)
    except Exception as e:
        logging.error(f"Error loading config file: {e}")
        return {}


def main():
    """Main entry point for the CLI."""
    parser = argparse.ArgumentParser(
        description="GreenBox - Raspberry Pi Plant Monitor"
    )
    parser.add_argument(
        "-c", "--config", help="Path to config file", default="config.yaml"
    )
    parser.add_argument(
        "-v", "--verbose", help="Enable verbose logging", action="store_true"
    )

    args = parser.parse_args()

    # Set up logging
    setup_logging(args.verbose)

    # Load configuration
    config = load_config(args.config)

    try:
        # Create and start controller
        controller = GreenBoxController(config)
        controller.start()
    except KeyboardInterrupt:
        logging.info("GreenBox stopped by user")
        return 0
    except Exception as e:
        logging.error(f"Error: {e}")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
