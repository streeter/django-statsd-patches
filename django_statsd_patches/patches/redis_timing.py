try:
    from redis import StrictRedis
except ImportError:
    REDIS_AVAILABLE = False
else:
    REDIS_AVAILABLE = True

import time
from django.conf import settings
from django_statsd.clients import statsd

SAMPLE_RATE = getattr(settings, 'STATSD_REDIS_SAMPLE_RATE', 1)


def new_execute_command(self, *args, **options):
    # The key is the name of the command in lowercase
    key = args[0].lower()

    # Start the timer
    start = time.time()

    # Run the command
    ret = self._old_execute_command(*args, **options)

    # Get the time
    ms = int(round((time.time() - start) * 1000))  # delta in ms

    # Log the stats
    statsd.timing('redis.execute', ms, SAMPLE_RATE)
    statsd.timing('redis.execute.' + key, ms, SAMPLE_RATE)

    # Done
    return ret


def patch():
    if not REDIS_AVAILABLE or getattr(StrictRedis, '__patched', False):
        return

    # Monkey patch Redis
    StrictRedis.__patched = True

    # Patch execute_command
    StrictRedis._old_execute_command = StrictRedis.execute_command
    StrictRedis.execute_command = new_execute_command
