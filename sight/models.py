class Social:
    def __init__(self, link, icon, label, copy=False):
        self.link = link
        self.icon = icon
        self.copy = copy
        self.label = label

    def render(self):
        if self.copy:
            return f"<li><button class='btn' data-clipboard-text='{self.link} aria-label='{{self.label}}'><i class='ri-{self.icon}-fill'></i></button></li>"
        else:
            return f"<li><a href='{self.link}'' target='_blank' aria-label='{self.label}'><i class='ri-{self.icon}-fill'></i></a></li>"


class Article:
    def __init__(self, title, subtitle):
        self.title = title
        self.subtitle = subtitle

    def render(self):
        return f"""<article><h2>{self.title}</h2><p>{self.subtitle}<p></article>"""


link = lambda url, label: f"<a href='{url}' target='_blank'>{label}</a>"
