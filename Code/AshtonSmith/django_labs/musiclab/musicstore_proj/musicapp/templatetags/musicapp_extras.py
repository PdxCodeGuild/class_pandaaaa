from django import template
import string
from ..api import request_song
register = template.Library()

@register.simple_tag
def get_slug(value):
    temp = ''
    for i in value:
        if i == '0' or i== '1' or i == '2' or i== '3' or i == '4' or i == '5' or i == '6' or i == '7' or i == '8' or i == '9':
            temp += i
    return temp

@register.simple_tag
def get_liked_songs(list):
    my_list =  str(list).split(",")
    final_list = []
    for i in my_list:
        final_list.append(request_song(i))
    return final_list
