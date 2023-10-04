from django import template
from menu_app.models import MenuItem
from django.urls import NoReverseMatch, reverse
from django.utils.safestring import mark_safe

register = template.Library()


def render_menu(menu_items):
    menu_html = "<ul>"
    for item in menu_items:
        try:
            menu_url = reverse(item.url)
            menu_html += f'<li><a href="{menu_url}">{item.title}</a>'
        except NoReverseMatch:
            menu_html += f'<li><a href="{item.url}">{item.title}</a>'
        children = MenuItem.objects.filter(parent=item)
        if children:
            menu_html += render_menu(children)
        menu_html += "</li>"
    menu_html += "</ul>"
    return menu_html


@register.simple_tag
def draw_menu(menu_name):
    root_items = MenuItem.objects.filter(parent__isnull=True)
    menu_items = root_items.filter(title=menu_name)
    if menu_items.exists():
        menu_items = menu_items[0].children.all()
    else:
        menu_items = []

    return mark_safe(render_menu(menu_items))
