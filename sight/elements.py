def social(link, icon, label, copy=False):
    if copy:
        return f"<li><button class='btn' data-clipboard-text='{link} aria-label='{label}'><i class='ri-{icon}-fill'></i></button></li>"
    else:
        return f"<li><a href='{link}'' target='_blank' aria-label='{label}'><i class='ri-{icon}-fill'></i></a></li>"


article = lambda title, subtitle: f"<article><h2>{title}</h2><p>{subtitle}<p></article>"

link = lambda url, label: f"<a href='{url}' target='_blank'>{label}</a>"
