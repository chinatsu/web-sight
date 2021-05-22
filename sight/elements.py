from datetime import datetime


def social(link, icon, label, description):
        return f"<article><a href='{link}' target='_blank' aria-label='{label}'><i class='ri-{icon}-fill'></i> {label}</a><p>{description}</p></article>"


article = lambda title, subtitle: f"<article><h2>{title}</h2><p>{subtitle}<p></article>"

link = lambda url, label: f"<a href='{url}' target='_blank'>{label}</a>"


class Post:
    def __init__(self, name, category, mtime, rendered=None):
        self.name = name
        self.category = category
        self.ctime = datetime.fromtimestamp(mtime)
        self.rendered = rendered

    def set_render(self, render):
        self.rendered = render
