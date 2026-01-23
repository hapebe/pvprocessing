# Exploring Fast-API

I follow i.a. https://hellocoding.de/blog/coding-language/python/fastapi .

## Installation

~~I decided not to worry about virtualenv etc.; ~~ Turns out I had to (?) use venv on my debian testing VM:

```
# in ./fastapi101 :
python -m venv .venv
source .venv/bin/activate
```


I did not use sudo to do the following:

```
pip install fastapi
pip install "uvicorn[standard]"
```

We might want to exit our venv again:
```
deactivate
```

<br>
At that point I already learned about ASGI (https://asgi.readthedocs.io/) servers in the Python universe.

<br><br>
<hr>

### systemd service

A sample / template unit file is included here, see [example.service](./example.service).

Run as root:

```
# maybe:
systemctl daemon-reload
systemctl start sonnenstand.service
# check if everything is well:
systemctl status sonnenstand.service
# enable auto-running the service:
systemctl enable sonnenstand.service
```