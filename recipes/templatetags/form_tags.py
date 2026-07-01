from django import template
from django.forms import TextInput, Textarea, Select, CheckboxSelectMultiple, FileInput, NumberInput, EmailInput

register = template.Library()


@register.filter
def add_class(field, css_classes):
    """
    Template filter to add CSS classes to form fields.
    Usage: {{ form.field|add_class:"form-control form-control-lg" }}
    """
    if not hasattr(field, 'field'):
        return field
    
    widget = field.field.widget
    attrs = widget.attrs.copy() if widget.attrs else {}
    
    # Get existing classes
    existing_classes = attrs.get('class', '')
    
    # Add new classes
    attrs['class'] = f"{existing_classes} {css_classes}".strip()
    
    # Create a new widget with updated attributes
    widget.attrs = attrs
    
    return field


@register.filter
def split(value, arg):
    """
    Custom filter to split a string by a separator.
    Usage: {{ text|split:"," }}
    """
    return value.split(arg) if value else []


