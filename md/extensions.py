from __future__ import unicode_literals

import markdown
import random
import re

from django.utils.safestring import mark_safe
from .utils import render_mail_as_js


__all__ = ['AutomailExtension',]


MAIL_RE = r'\b(?i)([a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]+)\b'


class AutomailPattern(markdown.inlinepatterns.Pattern):
    def handleMatch(self, m):
        email = m.group(2)
        el = markdown.util.etree.Element('span')
        dom_id = "_tyjsdfss-" + str(random.randint(1000, 9999999999999999))
        el.set('id', dom_id)
        js_el =  markdown.util.etree.Element('script')
        js_el.text = markdown.util.AtomicString(render_mail_as_js(dom_id,
                                                                  email))
        el.append(js_el)
        return el


class AutomailExtension(markdown.Extension):
    """
    An extension that turns email addresses into spam protected links.
    """

    def extendMarkdown(self, md, md_globals):
        automail = AutomailPattern(MAIL_RE, md)
        md.inlinePatterns.add('md-automail', automail, '_end')
