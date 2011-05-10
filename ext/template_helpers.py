import dateutil.parser

from sphinx.jinja2glue import BuiltinTemplateLoader

# Modified from django.contrib.humanize
def ordinal(value):
    t = ('th', 'st', 'nd', 'rd', 'th', 'th', 'th', 'th', 'th', 'th')
    if value % 100 in (11, 12, 13): # special case
        return u"%d%s" % (value, t[0])
    return u'%d%s' % (value, t[value % 10])

def format_date(date_str):
    date_parser = dateutil.parser.parser()
    d = date_parser.parse(date_str)
    day = ordinal(d.day)
    month = d.strftime('%B')
    return '%s of %s %d' % (day, month, d.year)

class TemplateBridge(BuiltinTemplateLoader):
    def init(self, *args, **kwargs):
        super(TemplateBridge, self).init(*args, **kwargs)
        self.environment.filters['format_date'] = format_date
