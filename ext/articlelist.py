# Copyright (c) 2011 Keegan Carruthers-Smith. All rights reserved.
# This file is licensed using the 2-clause BSD license.
# Hacked together from reading sphinx.ext.todo and the feed extension from
# sphinx-contrib

from docutils import nodes

from sphinx.util.compat import Directive, make_admonition

class articlelist(nodes.General, nodes.Element): pass

class ArticleList(Directive):
    has_content = False
    required_arguments = 0
    optional_arguments = 0
    final_argument_whitespace = False
    option_spec = {}

    def run(self):
        return [articlelist('')]

def process_articlelist_nodes(app, doctree, fromdocname):
    import dateutil.parser
    date_parser = dateutil.parser.parser()

    def get_articles():
        for docname, metadata in app.builder.env.metadata.iteritems():
            if 'date' not in metadata:
                continue
            try:
                pub_date = date_parser.parse(metadata['date'])
            except ValueError, exc:
                app.builder.warn('date parse error: %s in %s' %
                                 (str(exc), docname))
                continue

            yield (pub_date, docname)

    articles = None

    for node in doctree.traverse(articlelist):
        if articles is None:
            articles = list(get_articles())
            articles.sort(reverse=True)

        listnode = nodes.bullet_list(classes=['article-list'])
        for pub_date, docname in articles:
            par = nodes.paragraph()
            date_str = pub_date.strftime('%B %Y')
            datenode = nodes.inline(classes=['date'])
            datenode += nodes.Text(date_str, date_str)
            par += datenode

            title = app.builder.env.titles.get(docname, None)
            if title is None:
                title = docname
            else:
                title = title.astext()

            # Create a reference
            newnode = nodes.reference('', '', internal=True)
            innernode = nodes.Text(title, title)
            try:
                newnode['refuri'] = app.builder.get_relative_uri(
                    fromdocname, docname)
            except NoUri:
                # ignore if no URI can be determined, e.g. for LaTeX output
                pass
            newnode.append(innernode)
            par += newnode

            listnode += nodes.list_item('', par)

        node.replace_self(listnode)



def setup(app):
    app.add_node(articlelist)

    app.add_directive('articlelist', ArticleList)
    app.connect('doctree-resolved', process_articlelist_nodes)
