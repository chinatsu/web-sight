from elements import link, article, social, Post
from flask import Flask, render_template, jsonify, send_from_directory
import random
from misaka import Markdown, HtmlRenderer
import os

renderer = HtmlRenderer()
md = Markdown(renderer, extensions=("fenced-code",))
blogpath = "blog"

app = Flask(__name__)

socials = [
    social("https://twitter.com/malpractitioner", "twitter", "my twitter profile"),
    social(
        "https://instagram.com/malpractitioner_", "instagram", "my instagram profile",
    ),
    social(
        "cn#9999",
        "discord",
        "click to copy my discord username to clipboard",
        copy=True,
    ),
    social("https://github.com/chinatsu", "github", "my github profile"),
    social(
        "https://codegolf.stackexchange.com/users/91616/chinatsu",
        "stack-overflow",
        "my codegolf profile on stackexchange",
    ),
    social("https://steamcommunity.com/id/lomg", "steam", "my steam profile"),
    social("https://twitch.tv/cutenice", "twitch", "my twitch profile"),
    social(
        "https://soundcloud.com/uwaa", "soundcloud", "one of my soundcloud profiles"
    ),
    social(
        "https://open.spotify.com/user/213p4w55e6upnsr73x6zbplya",
        "spotify",
        "my spotify profile",
    ),
    social(
        "chinatsun",
        "snapchat",
        "click to copy my snapchat profile to clipboard",
        copy=True,
    ),
]


@app.route("/static/<file>")
def serve(file):
    return send_from_directory("files", file)


@app.route("/")
def index():
    genres = [
        "korean indie music",
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
        article("I'm Kent", random.choice(greetings)),
        article(
            "I'm a software developer at " + link("https://nav.no/", "Nav"),
            "the Norwegian Labour and Welfare Administration",
        ),
        article(
            "I'm an admin at " + link("https://harddrop.com/", "HardDrop"),
            "the largest Tetris community in the west",
        ),
    ]
    right = [
        article(
            "I like Python and Rust",
            "I primarily use Kotlin and TypeScript/React at work",
        ),
        article(
            "I like music a lot", f"you can talk to me about {random.choice(genres)}"
        ),
        article(
            "I'm into mechanical keyboards",
            "although my daily driver is a Topre keyboard",
        ),
        article("I play a lot of Tetris", "I have cleared 40 lines in 28.437 seconds"),
    ]
    return render_template("index.tpl", socials=socials, left=left, right=right)


@app.route("/blog/")
def blogindex():
    posts = []
    categories = [
        d for d in os.listdir(blogpath) if os.path.isdir(os.path.join(blogpath, d))
    ]

    for category in categories:
        for post in os.listdir(os.path.join(blogpath, category)):
            filepath = os.path.join(blogpath, category, post)
            if os.path.isfile(filepath):
                posts.append(Post(post, category, os.path.getctime(filepath)))

    to_render = sorted(posts, key=lambda x: x.mtime, reverse=True)
    for post in to_render:
        with open(os.path.join(blogpath, post.category, post.name), "r") as f:
            post.set_render(md(f.read()))
    return render_template("blog.tpl", posts=to_render, socials=socials)
