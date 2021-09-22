from django import template
from django.utils.safestring import mark_safe
register=template.Library()


@register.filter(name="imgHtml")
def imgHtml(url,size):
    return mark_safe("""
        <div class="pictures" >
            <a href="detail/{0}" target="_blank"  >
                <img src="/static/img/fake/{0}" alt="">
                <div class="size">  {1}</div>
            </a>
        </div>""".format(url,size)
)
