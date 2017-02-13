import os
import string

from ..exceptions import TemplateNotFound


def load_template(template_name):
    tpl_dir = os.environ.get('SQLTEMPLATE_DIR', os.getcwd())
    try:
        with open(os.path.join(tpl_dir, template_name)) as fh:
            return string.Template(fh.read())
    except IOError:
        raise TemplateNotFound(template_name)


def create_template_from_string(x):
    return string.Template(x)


def render_template(template, context):
    return template.substitute(context)


def do_query(sql, query_params, using=None):
    if not using:
        raise ValueError('Connection object is required')
    cursor = using.cursor()
    return cursor.execute(sql, query_params)
