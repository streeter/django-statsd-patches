from django.template import Template
from django_statsd.clients import statsd


def key_for_template_name(name):
    if not name.endswith('.html'):
        return None
    return name.replace('/', '.')[:-5]


def new_template_init(self, template_string, origin=None, name='<Unknown Template>'):
    key = key_for_template_name(name)
    if key is None:
        return self._old_init(template_string, origin, name)

    # We've got a key, so time the template parsing
    with statsd.timer('template.{0}.parse'.format(key)):
        return self._old_init(template_string, origin, name)


def new_render(self, context):
    key = key_for_template_name(self.name)
    if key is None:
        return self._old_render(context)

    # We've got a key, so time the template parsing
    with statsd.timer('template.{0}.render'.format(key)):
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
