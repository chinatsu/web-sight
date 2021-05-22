<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <meta name="language" content="english">
    <meta name="description" content="my personal website">
    <meta name="viewport" content="width=device-width">
    <title>viridescent</title>
    <link rel="stylesheet" type="text/css" href="/static/style.css">
    <link href="https://fonts.googleapis.com/css2?family=Oswald:wght@600&family=Poppins&display=swap" rel="stylesheet">
    <link href="https://cdn.jsdelivr.net/npm/remixicon@2.5.0/fonts/remixicon.css" rel="stylesheet">
  </head>
  <body>
    <main id="scroll-container">
        <div id="scroll-down"></div>
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
        <section class="centered secondary">
            {% for social in socials_left %}{{ social }}{% endfor %}
        </section>
        <section class="centered primary">
            {% for social in socials_right %}{{ social }}{% endfor %}
        </section>
    </main>
  </body>
  <script>
    var wrapper = document.getElementById('scroll-container');
    var arrow = document.getElementById('scroll-down');

    wrapper.onscroll = function (evt) {
        if (wrapper.scrollTop + window.innerHeight >= wrapper.scrollHeight - 100) {
            if (!arrow.classList.contains("fade-out")) {
                arrow.classList.add("fade-out");
            }
        } else {
            if (arrow.classList.contains("fade-out")) {
                arrow.classList.remove("fade-out");
            }
        }
    }

    arrow.onclick = function (evt) {
        wrapper.scrollBy(0, window.innerHeight);
    }
  </script>
</html>