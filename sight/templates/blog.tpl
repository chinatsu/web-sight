<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <meta name="language" content="english">
    <meta name="description" content="my personal website">
    <title>viridescent</title>
    <link rel="stylesheet" type="text/css" href="/static/blog.css">
    <link href="https://fonts.googleapis.com/css2?family=Oswald:wght@600&family=Poppins&display=swap" rel="stylesheet">
    <link href="https://cdn.jsdelivr.net/npm/remixicon@2.5.0/fonts/remixicon.css" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/clipboard@2/dist/clipboard.min.js"></script>
  </head>
  <body>
    <header id="header"><h1><a href="/">viridescent</a></h1><h1>blog</h1></header>
    <section id="content">
    {% for post in posts %}
        <article>
          <p class="posted">Last modified {{ post.mtime.strftime("%Y-%m-%d, %H:%M") }} in {{ post.category }}</p>
          {{ post.rendered }}
        </article>
    {% endfor %}
    </section>    
    <footer id="footer">
      <nav>
        <ul>
          {% for social in socials %}{{ social }}{% endfor %}
        </ul>
      </nav>
    </footer>
  </body>
</html>
