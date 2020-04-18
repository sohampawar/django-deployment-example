from django import template

register = template.Library()

#With decorators
@register.filter(name='cut')

# Function for Custon Template Filter

def cut(value,arg):
    """
    This cuts out all values of "arg" from the string!

    """
    return value.replace(arg,'')

# Without decorators
# register.filter('cut',cut)
