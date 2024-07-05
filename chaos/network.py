import logging
import random
import time

from chaos import chaos_state

log = logging.getLogger(__name__)


def add_latency(min_delay=0.1, max_delay=0.5):
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Introduce random delay
            if chaos_state['active']:
                delay = random.uniform(min_delay, max_delay)
                time.sleep(delay)
            return func(*args, **kwargs)

        return wrapper
    return decorator
