# How I deploy changes to my website

I decided not long ago to create a personal website to serve a short description of myself
as well as to provide a few links to my profiles on other platforms. I originally
developed this small web app directly on my VPS hosted by DigitalOcean, but I wanted to look into
the possibilities of deploying changes to the server when pushing changes to Git.

So I created a [repository](https://github.com/chinatsu/web-sight) over at GitHub
and started writing the app in the clean environment. To provide a little context,
the app I had written on the VPS was more like a playground, so there were bits and
pieces of code in the web app that weren't really used for this new site. These
were shed when moving the code to the repository.

I cloned the repository onto the server, and set up a little bit of infrastructure
around it. My initial idea was that when I push changes to the remote master,
a [GitHub Action](https://github.com/features/actions) would execute some
commands on my VPS:

* `cd` to repository
* `git pull`
* `systemctl --user restart website.service`

I wanted to avoid using `sudo` or run anything as `root` at this level, so I
started out with a user service controlling the [uWSGI](https://uwsgi-docs.readthedocs.io/en/latest/) instance.

This did not pan out the way I wanted, however. Running `systemctl --user` did not allow the service to
run the processes with the `www-data` group. This is an important part, because nginx runs as `www-data`
and requires read and write access to the UNIX socket to communicate with uWSGI. Running the service
as my own user would make the socket owned by my user both as user and as group, leaving `www-data` as
an "outsider" group attempting access. With `660` as the file mode, nginx would have neither read nor
write access to the socket. I didn't want to open the file up completely either. Even adding my user to 
the group did not yield any results, although with my user being a member of the group, I could 
`chown` the socket after a service restart to give group ownership to `www-data`.

I can't say I was particularly satisfied with this. The GitHub Action turned out to do a little more than
I really wanted. The "working" sequence went something like this

```
cd repo
git pull
systemctl --user restart website.service
sleep 10 # ensure service to be completely restarted
chown myuser:www-data website.sock
```

It was clear that running the website service as user was not a desirable route at this point.

## Enter website-watcher

I decided that I would go back to an infrastructure closer to what the service for my playground webapp
looked like. This service is a system service and runs as my user and as the `www-data` group, which
results in the sockets having the right owners and the right file modes. This kind of conflicts
with my desire to leave `sudo` out of my GitHub Action, and prompted me to do a search to see
if there is a way to trigger restarts some other way.

I stumbled across this [superuser](https://superuser.com/a/1276457) answer, which
fit my requirements perfectly. In addition to my website service, I defined a website-watcher service
with directions to restart the website service when run. In addition, I defined a website-watcher *path-file*,
which defines when to run the website-watcher *service*. I set the PathModified parameter to wait for changes
in my repository's `.git/refs/head/master`.

The result is that when the latest commit hash changes (`git pull`), that triggers a restart of my website service 
through website-watcher. The GitHub action is then reduced to the following.

```
cd repo
git pull
```

No `sudo` in sight, and everything else is taken care of by systemd!