try:
    from redis import StrictRedis
except ImportError:
    REDIS_AVAILABLE = False
else:
    REDIS_AVAILABLE = True

from django_statsd.clients import statsd


def new_execute_command(self, *args, **options):
    # The key is the name of the command in lowercase
    key = args[0].lower()
    with statsd.timer('redis.{0}'.format(key)):
        return self._old_execute_command(*args, **options)


def patch():
    if not REDIS_AVAILABLE:
        return
    if getattr(StrictRedis, '__patched', False):
        return

    # Monkey patch Redis
    StrictRedis.__patched = True

    # Patch execute_command
    StrictRedis._old_execute_command = StrictRedis.execute_command
    StrictRedis.execute_command = new_execute_command
