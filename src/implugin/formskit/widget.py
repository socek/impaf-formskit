from implugin.jinja2.widget import MultiWidget


class FormWidget(MultiWidget):

    prefix = ''

    templates = {
        'field_error': 'implugin.formskit:templates/field_error.jinja2',
        'form_error': 'implugin.formskit:templates/form_error.jinja2',
        'begin': 'implugin.formskit:templates/begin.jinja2',
        'end': 'implugin.formskit:templates/end.jinja2',
        'text': 'implugin.formskit:templates/text.jinja2',
        'password': 'implugin.formskit:templates/password.jinja2',
        'select': 'implugin.formskit:templates/select.jinja2',
        'hidden': 'implugin.formskit:templates/hidden.jinja2',
        'submit': 'implugin.formskit:templates/submit.jinja2',
    }

    def __init__(self, form):
        super().__init__()
        self.form = form

    def get_tag_id(self, name):
        return '%s_%s' % (self.form.get_name(), name)

    def begin(self, tagid=None, style=None):
        data = {}
        data['action'] = getattr(self.form, 'action', None)
        data['id'] = tagid
        data['name'] = self.form.get_name()
        data['style'] = style
        return self.render_for(self.templates['begin'], data)

    def end(self):
        return self.render_for(self.templates['end'], {})

    def text(self, name, disabled=False, autofocus=False):
        return self._input('text', name, disabled, autofocus)

    def password(self, name, disabled=False, autofocus=False):
        return self._input('password', name, disabled, autofocus)

    def select(self, name, disabled=False, autofocus=False):
        return self._input('select', name, disabled, autofocus)

    def _base_input(self, name):
        data = {}
        data['name'] = self.form.fields[name].get_name()
        data['value'] = self.form.get_value(name, default='')
        data['values'] = self.form.get_values(name)
        data['field'] = self.form.fields[name]
        data['templates'] = self.templates
        return data

    def _input(
        self,
        input_type,
        name,
        disabled=False,
        autofocus=False,
        prefix=None,
        **kwargs
    ):
        data = self._base_input(name)
        field = data['field']

        data['id'] = self.get_tag_id(name)
        data['label'] = field.label
        data['error'] = field.error
        data['messages'] = field.get_error_messages()
        data['value_messages'] = field.get_value_errors(default=[])
        data['disabled'] = disabled
        data['autofocus'] = autofocus
        data.update(kwargs)
        return self.render_for(self.templates[input_type], data, prefix=prefix)

    def hidden(self, name):
        data = self._base_input(name)
        return self.render_for(self.templates['hidden'], data)

    def csrf_token(self):
        return self.hidden('csrf_token')

    def submit(self, label='', cls='btn-success', base_cls='btn btn-lg'):
        return self.render_for(
            self.templates['submit'],
            {
                'label': label,
                'class': cls,
                'base_class': base_cls
            }
        )

    def form_error(self):
        data = {}
        data['error'] = True if self.form.success is False else False
        data['messages'] = self.form.get_error_messages()
        return self.render_for(self.templates['form_error'], data)
