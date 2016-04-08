from __future__ import unicode_literals

import os
import json

from django.forms import widgets
from django.forms.utils import flatatt
from django.template.loader import render_to_string
from django.utils.encoding import force_text, python_2_unicode_compatible
from django.utils.html import conditional_escape, format_html, html_safe
from django.utils.safestring import mark_safe
from django.utils.translation.trans_real import get_language

#from .conf import FIELD_CONFIGURATION
from . import conf

__all__ = ['MDWidget',]


class MDWidget(widgets.Textarea):
    widget = widgets.Textarea
    template_name = 'md/widgets/mdwidget.html'

    class Media:
        js = (
            #'{0}js/marked.js'.format(conf.STATIC_URL),
            '{0}js/md.js'.format(conf.STATIC_URL),
        )
        css = {
            'screen': ('{0}css/mdwidget.css'.format(conf.STATIC_URL), )
        }

    def __init__(self, *args, **kwargs):
        self.conf = kwargs.pop('conf', {})
        attrs = {
            'cols': '120',
            'rows': '25',
            'class': 'md-textarea',
        }
        super(MDWidget, self).__init__(attrs)

    def render(self, name, value, attrs=None):
        if value is None:
            value = ''
        final_attrs = self.build_attrs(attrs, name=name)

        context = {
            'value': force_text(value),
            'attrs': final_attrs,
            'conf': self.conf,
            'js_conf': mark_safe(json.dumps(self.conf)),
            'help_url': conf.HELP_URL,
        }
        return render_to_string(self.template_name, context)
