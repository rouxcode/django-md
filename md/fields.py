from __future__ import unicode_literals

from django import forms
from django.db import models
from django.utils.encoding import force_unicode, python_2_unicode_compatible
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _

from markdown import markdown

from .extensions import AutomailExtension
from .widgets import MDWidget


__all__ = ['MDField',]


@python_2_unicode_compatible
class MDText(object):

    def __init__(self, value, *args, **kwargs):
        self.md = value

    def __str__(self):
        return self.md

    @property
    def html(self):
        extensions = [AutomailExtension(), 'mdx_gfm',]
        html = markdown(force_unicode(self.md), extensions,
                        output_format='html5', safe_mode=True,
                        enable_attributes=True)
        return mark_safe(''.join(html.splitlines()))


class MDField(models.Field):

    description = "Markdown formatted text"

    def __init__(self, *args, **kwargs):
        self.conf = kwargs.pop('conf', None)
        super(MDField, self).__init__(*args, **kwargs)

    def get_internal_type(self):
        return "TextField"

    def formfield(self, **kwargs):
        defaults = {
            'form_class': forms.CharField,
            'max_length': self.max_length,
            'widget': MDWidget(conf=self.conf),
        }
        defaults.update(kwargs)
        return super(MDField, self).formfield(**defaults)

    def from_db_value(self, value, expression, connection, context):
        if value is None:
            return value
        return MDText(value)

    def to_python(self, value):
        if isinstance(value, MDText):
            return value
        if value is None:
            return value
        return MDText(value)

    def get_prep_value(self, value):
        return value.md
