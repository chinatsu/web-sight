from elements import link, article, social
from flask import Flask, render_template, jsonify, send_from_directory
import random

app = Flask(__name__)


@app.errorhandler(404)
def resource_not_found(e):
    return jsonify(error=str(e)), 404


socials_left = [
    social(
        "https://twitter.com/malpractitioner",
        "Twitter",
        "I'm probably the most active here",
    ),
    social(
        "https://instagram.com/malpractitioner_",
        "Instagram",
        "Primarily for food, music and keyboard stories",
    ),
    social(
        "https://github.com/chinatsu",
        "GitHub",
        "Work and hobby projects",
    ),
    social(
        "https://steamcommunity.com/id/lomg",
        "Steam",
        "I play Rocket League.. and that's about it",
    ),
    social(
        "https://www.linkedin.com/in/malpractitioner/",
        "LinkedIn",
        "Typically used to respond to headhunters, not much else",
    ),
]

socials_right = [
    social(
        "https://twitch.tv/cutenice",
        "Twitch",
        "I used to stream a bit, but not so much anymore",
    ),
    social(
        "https://soundcloud.com/malpractitioner",
        "SoundCloud",
        "I have other accounts too, but this one's the most recently active",
    ),
    social(
        "https://open.spotify.com/user/213p4w55e6upnsr73x6zbplya",
        "Spotify",
        "My primary source for music",
    ),
    social(
        "https://www.discogs.com/user/cn_",
        "Discogs",
        "Used to document my physical music collection",
    ),
    social(
        "https://codegolf.stackexchange.com/users/91616/chinatsu",
        "StackExchange",
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
            f"I have cleared 40 lines in {link('https://www.youtube.com/watch?v=4BE9O9t3k2Q', '26.513 seconds')}",
        ),
    ]
    return render_template(
        "index.tpl",
        socials_left=socials_left,
        socials_right=socials_right,
        left=left,
        right=right,
    )