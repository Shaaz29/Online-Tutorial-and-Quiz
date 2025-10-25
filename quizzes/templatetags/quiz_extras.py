from django import template

register = template.Library()

@register.filter
def get_item(dictionary, key):
    try:
        return dictionary.get(str(key)) if hasattr(dictionary, 'get') else None
    except Exception:
        return None
