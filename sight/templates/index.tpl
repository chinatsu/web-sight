<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <meta name="language" content="english">
    <meta name="description" content="my personal website">
    <meta name="viewport" content="width=device-width">
    <title>viridescent</title>
    <link rel="stylesheet" type="text/css" href="/static/style.css">
    <link rel="icon" href="data:;base64,iVBORw0KGgo=">
  </head>
  <body>
    <main id="scroll-container">
        <section class="content primary">
            <header><h1>viridescent<!-- <span><a href="/blog">blog</a></span> --></h1></header>
            <section>
                {% for article in left %}{{ article }}{% endfor %}
            </section>
        </section>
        <section class="content secondary">
            <header></header>
            <section>
                {% for article in right %}{{ article }}{% endfor %}
            </section>
        </section>
        
        <section class="content centered secondary">
            <header><h1>Me on other platforms</h1></header>
            <section>
                {% for social in socials_left %}{{ social }}{% endfor %}
            </section>
        </section>
        <section class="centered primary">
            {% for social in socials_right %}{{ social }}{% endfor %}
        </section>
        <button id="scroll-down" aria-label="Scroll down"></button>
        <div id="smokescreen" class="primary"></div>
    </main>
  </body>
</html>
