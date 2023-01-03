# sample.py
from django import template

register = template.Library()


@register.simple_tag
def dir_eliminate_path(dirpath, phase):
    return dirpath.split("\\",phase)[phase].split("\\",phase)[1]


@register.filter
def echo_test(value):
    return value + 'test'