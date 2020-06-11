from models import link, Article, Social
from flask import Flask, render_template, send_from_directory
import random

app = Flask(__name__)


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
        Article("I'm Kent", random.choice(greetings)),
        Article(
            "I'm a software developer at " + link("https://nav.no/", "Nav"),
            "the Norwegian Labour and Welfare Administration",
        ),
        Article(
            "I'm an admin at " + link("https://harddrop.com/", "HardDrop"),
            "the largest Tetris community in the west",
        ),
    ]
    right = [
        Article(
            "I like Python and Rust",
            "I primarily use Kotlin and TypeScript/React at work",
        ),
        Article(
            "I like music a lot", f"you can talk to me about {random.choice(genres)}"
        ),
        Article(
            "I'm into mechanical keyboards",
            "although my daily driver is a Topre keyboard",
        ),
        Article("I play a lot of Tetris", "I have cleared 40 lines in 29.042 seconds"),
    ]
    socials = [
        Social("https://twitter.com/malpractitioner", "twitter", "my twitter profile"),
        Social(
            "https://instagram.com/malpractitioner_",
            "instagram",
            "my instagram profile",
        ),
        Social(
            "cn#9999",
            "discord",
            "click to copy my discord username to clipboard",
            copy=True,
        ),
        Social("https://github.com/chinatsu", "github", "my github profile"),
        Social(
            "https://codegolf.stackexchange.com/users/91616/chinatsu",
            "stack-overflow",
            "my codegolf profile on stackexchange",
        ),
        Social("https://steamcommunity.com/id/lomg", "steam", "my steam profile"),
        Social("https://twitch.tv/cutenice", "twitch", "my twitch profile"),
        Social(
            "https://soundcloud.com/uwaa", "soundcloud", "one of my soundcloud profiles"
        ),
        Social(
            "https://open.spotify.com/user/213p4w55e6upnsr73x6zbplya",
            "spotify",
            "my spotify profile",
        ),
        Social(
            "chinatsun",
            "snapchat",
            "click to copy my snapchat profile to clipboard",
            copy=True,
        ),
    ]
    return render_template("index.tpl", socials=socials, left=left, right=right)
