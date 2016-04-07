import html5lib
import random
import re

from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe
from django.utils.html import conditional_escape


def render_mail_as_js(dom_id, email, text=None, autoescape=None):
    text = text or email
    if autoescape:
        email = conditional_escape(email)
        text = conditional_escape(text)

    emailArrayContent = ''
    textArrayContent = ''
    r = lambda c: '"' + str(ord(c)) + '",'

    for c in email: emailArrayContent += r(c)
    for c in text: textArrayContent += r(c)

    result = """
             var _tyjsdf=[%s], _qplmks=[%s];
             var content='<a href="&#x6d;&#97;&#105;&#x6c;&#000116;&#111;&#x3a;';
             for(_i=0;_i<_tyjsdf.length;_i++){content+=('&#'+_tyjsdf[_i]+';');}
             content+='">';
             for(_i=0;_i<_qplmks.length;_i++){content+=('&#'+_qplmks[_i]+';');}
             content+='</a>';
             document.getElementById('%s').innerHTML=content;
             """ % (re.sub(r',$', '', emailArrayContent),
                    re.sub(r',$', '', textArrayContent),
                    dom_id)
    result = ''.join(result.replace('  ', '').splitlines())
    return mark_safe(result)
