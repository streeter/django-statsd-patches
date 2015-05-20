from django.template import Template
from django_statsd.clients import statsd
from django.conf import settings

SAMPLE_RATE = getattr(settings, 'STATSD_TEMPLATE_SAMPLE_RATE', 1)


def key_for_template_name(name):
    if not name or not name.endswith('.html'):
        return None
    return name.replace('/', '.')[:-5]


def new_template_init(self, *args, **kwargs):
    if len(args) >= 3:
        key = key_for_template_name(args[2])
    else:
        key = key_for_template_name(kwargs.get('name', '<Unknown Template>'))
    if key is None:
        return self._old_init(*args, **kwargs)

    # We've got a key, so time the template parsing
    with statsd.timer('template.{0}.parse'.format(key), rate=SAMPLE_RATE):
        return self._old_init(*args, **kwargs)


def new_render(self, context):
    key = key_for_template_name(self.name)
    if key is None:
        return self._old_render(context)

    # We've got a key, so time the template parsing
    with statsd.timer('template.{0}.render'.format(key), rate=SAMPLE_RATE):
        return self._old_render(context)


def patch():
    if getattr(Template, '__patched', False):
        return

    # Monkey patch Django
    Template.__patched = True

    # Patch __init__
    Template._old_init = Template.__init__
    Template.__init__ = new_template_init

    # Patch _render
    Template._old_render = Template._render
    Template._render = new_render
