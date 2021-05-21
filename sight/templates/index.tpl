<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <meta name="language" content="english">
    <meta name="description" content="my personal website">
    <title>viridescent</title>
    <link rel="stylesheet" type="text/css" href="/static/style.css">
    <link href="https://fonts.googleapis.com/css2?family=Oswald:wght@600&family=Poppins&display=swap" rel="stylesheet">
    <link href="https://cdn.jsdelivr.net/npm/remixicon@2.5.0/fonts/remixicon.css" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/clipboard@2/dist/clipboard.min.js"></script>
  </head>
  <body>
    <header id="header--left">
        <h1>viridescent<span><a href="/blog">blog</a></span></h1>
    </header>
    <header id="header--right">
        <nav>
            <ul>
                {% for social in socials %}{{ social }}{% endfor %}
            </ul>
        </nav>
    </header>
    <section id="content--left">
        {% for article in left %}{{ article }}{% endfor %}
    </section>
    <section id="content--right">
        {% for article in right %}{{ article }}{% endfor %}
    </section>
    <script>
    var btns = document.querySelectorAll('.btn');

    for (var i = 0; i < btns.length; i++) {
        btns[i].addEventListener('mouseleave', clearTooltip);
        btns[i].addEventListener('blur', clearTooltip);
    }
    function clearTooltip(e) {
        e.currentTarget.setAttribute('class', 'btn');
        e.currentTarget.removeAttribute('aria-label');
    }

    function showTooltip(elem, msg) {
        elem.setAttribute('class', 'btn tooltipped tooltipped-s');
        elem.setAttribute('aria-label', msg);
    }
    var clipboard = new ClipboardJS('.btn');
    clipboard.on('success', function(e) {
        e.clearSelection();
        showTooltip(e.trigger, 'copied');
    });
    </script>
  </body>
</html>