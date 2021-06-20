from elements import link, article, social, Post
from flask import Flask, render_template, jsonify, send_from_directory, abort
import random
from misaka import Markdown, HtmlRenderer
import os

renderer = HtmlRenderer()
md = Markdown(renderer, extensions=("fenced-code",))
blogpath = "blog"

app = Flask(__name__)


@app.errorhandler(404)
def resource_not_found(e):
    return jsonify(error=str(e)), 404


socials_left = [
    social(
        "https://twitter.com/malpractitioner",
        "twitter",
        "Me on Twitter",
        "I'm probably the most active here",
    ),
    social(
        "https://instagram.com/malpractitioner_",
        "instagram",
        "Me on Instagram",
        "Primarily for food, music and keyboard stories",
    ),
    social(
        "https://github.com/chinatsu",
        "github",
        "Me on GitHub",
        "Work and hobby projects",
    ),
    social(
        "https://steamcommunity.com/id/lomg",
        "steam",
        "Me on Steam",
        "I play Rocket League.. and that's about it",
    ),
    social(
        "https://www.linkedin.com/in/malpractitioner/",
        "linkedin-box",
        "Me on LinkedIn",
        "Typically used to respond to headhunters, not much else",
    ),
]

socials_right = [
    social(
        "https://twitch.tv/cutenice",
        "twitch",
        "Me on Twitch",
        "I used to stream a bit, but not so much anymore",
    ),
    social(
        "https://soundcloud.com/malpractitioner",
        "soundcloud",
        "Me on SoundCloud",
        "I have other accounts too, but this one's the most recently active",
    ),
    social(
        "https://open.spotify.com/user/213p4w55e6upnsr73x6zbplya",
        "spotify",
        "Me on Spotify",
        "My primary source for music",
    ),
    social(
        "https://www.discogs.com/user/cn_",
        "disc",
        "Me on Discogs",
        "Used to document my physical music collection",
    ),
    social(
        "https://codegolf.stackexchange.com/users/91616/chinatsu",
        "stack-overflow",
        "Me on StackExchange",
        "Rarely active, mostly for golfing code",
    ),
]

names = ["Kent", "cn"]


@app.route("/static/<file>")
def serve(file):
    return send_from_directory("files", file)


@app.route("/")
def index():
    genres = [
        link(
            "https://www.youtube.com/playlist?list=PLtkWCVwDMTaO9QpDRitXWw1jasj-6uiwE",
            "korean indie music",
        ),
        "post-rock",
        "sludge metal",
        "the last concert you attended",
        "shoegaze",
        "the nuances between post-avant jazzcore and progressive dreamfunk",
        "math-rock",
        "electronic music like what's on "
        + link(
            "https://open.spotify.com/playlist/2AZzV5T5fGa03uWc5bzprL?si=lHwejEX6R82pAjol4HnIEg",
            "this playlist",
        ),
    ]
    greetings = ["hello", "what up"]
    left = [
        article(f"I'm {random.choice(names)}", random.choice(greetings)),
        article(
            f"I develop software at {link('https://nais.io/', 'NAIS')}",
            f"{link('https://www.nav.no/en/home', 'NAV')}'s Application Infrastructure Service",
        ),
    ]
    right = [
        article(
            "I like Python and Rust",
            "I primarily use Go and god knows what else at work",
        ),
        article(
            f"I like music a lot", f"you can talk to me about {random.choice(genres)}"
        ),
        article(
            "I'm into mechanical keyboards",
            f"I use a {link('https://keyhive.xyz/shop/ut472-kit', 'UT47.2')} with lubed {link('https://splitkb.com/products/gazzew-boba-u4-silent-tactile-switch', 'Gazzew Boba U4')} switches, and {link('https://novelkeys.xyz/products/kat-lich-gb', 'KAT Lich')} keycaps. It looks like {link('https://twitter.com/malpractitioner/status/1384571485658959873', 'this')}",
        ),
        article(
            "I play a lot of Tetris",
            f"I have cleared 40 lines in {link('https://www.youtube.com/watch?v=sNkVBprghyQ', '27.878 seconds')}",
        ),
    ]
    return render_template(
        "index.tpl",
        socials_left=socials_left,
        socials_right=socials_right,
        left=left,
        right=right,
    )


@app.route("/blog/")
def blogindex():
    posts = []
    print(os.path.join(os.getcwd(), blogpath))
    categories = [
        d
        for d in os.listdir(blogpath)
        if os.path.isdir(os.path.join(os.getcwd(), blogpath, d))
    ]

    for category in categories:
        for post in os.listdir(os.path.join(blogpath, category)):
            filepath = os.path.join(blogpath, category, post)
            if os.path.isfile(filepath):
                posts.append(Post(post, category, os.path.getctime(filepath)))

    to_render = sorted(posts, key=lambda x: x.ctime, reverse=True)
    for post in to_render:
        with open(os.path.join(blogpath, post.category, post.name), "r") as f:
            post.set_render(md(f.read()))
    return render_template("blog.tpl", posts=to_render)


@app.route("/blog/<category>/")
def categoryindex(category):
    posts = []
    try:
        for post in os.listdir(os.path.join(blogpath, category)):
            filepath = os.path.join(blogpath, category, post)
            if os.path.isfile(filepath):
                posts.append(Post(post, category, os.path.getctime(filepath)))
    except:
        return abort(404, description="No such category")
    to_render = sorted(posts, key=lambda x: x.ctime, reverse=True)
    for post in to_render:
        with open(os.path.join(blogpath, post.category, post.name), "r") as f:
            post.set_render(md(f.read()))
    return render_template("blog.tpl", posts=to_render)
