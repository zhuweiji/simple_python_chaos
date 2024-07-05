import logging
import os
import sys
from pathlib import Path

import yaml

# Initialize chaos_state as a global variable
chaos_state = {}


logging.basicConfig(
    format='%(name)s-%(levelname)s|%(lineno)d:  %(message)s', level=logging.INFO)
log = logging.getLogger(__name__)


def load_chaos_config():
    global chaos_state

    # Get the directory of the script that's importing this package
    if hasattr(sys.modules['__main__'], '__file__'):
        start_dir = Path(sys.modules['__main__'].__file__).parent.absolute()
    else:
        # Fallback to current working directory if __main__ has no __file__ (e.g., in REPL)
        start_dir = Path.cwd()

    # Look for chaos.config.yml starting from the importing script's directory up to the root
    config_file = None
    current_dir = start_dir
    while current_dir != current_dir.parent:  # Stop at root directory
        potential_config = current_dir / 'chaos.config.yml'
        if potential_config.exists():
            config_file = potential_config
            break
        current_dir = current_dir.parent

    if config_file:
        try:
            with open(config_file, 'r') as f:
                chaos_state.update(yaml.safe_load(f))
            log.info(f"Loaded chaos configuration from {config_file}")
            log.info(f"Chaos Configuration:")
            log.info(f"{chaos_state}")

        except Exception as e:
            log.info(f"Error loading chaos configuration: {e}")
    else:
        log.info("No chaos.config.yml file found")

# Function to access the chaos_state


def get_chaos_state():
    return chaos_state


# Load the configuration when the package is imported
load_chaos_config()

# You can add other initialization code here if needed
