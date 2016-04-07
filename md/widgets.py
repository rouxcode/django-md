from django.forms import widgets


class MDWidget(widgets.Textarea):

    def __init__(self, *args, **kwargs):
        self.conf = kwargs.pop('conf', None)
        super(MDWidget, self).__init__(*args, **kwargs)
