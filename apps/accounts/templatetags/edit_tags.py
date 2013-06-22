from django.core.urlresolvers import reverse
from django import template


register = template.Library()


class AdminEdit(template.Node):
    def __init__(self, edit_link_object):
        self.edit_object = template.Variable(edit_link_object)

    def render(self, context):
        try:
            obj = self.edit_object.resolve(context)
            app_name = obj._meta.app_label
            model_name = obj._meta.object_name.lower()
            return reverse('admin:%s_%s_change' % (app_name,
                                                   model_name),
                           args=(1, ))
        except template.VariableDoesNotExist:
            return ''
        except AttributeError:
            return ''


@register.tag
def edit_link(parser, token):
    tagname, admin_object = token.split_contents()
    return AdminEdit(admin_object)
