import os
from string import Template


class TemplatesMixin:
    TEMPLATES_DIR = "."

    def _read_template(self, template_path):
        with open(os.path.join(self.TEMPLATES_DIR, template_path)) as template:
            return template.read()

    def render(self, path, **kwargs):
        return Template(self._read_template(path)).substitute(**kwargs)
