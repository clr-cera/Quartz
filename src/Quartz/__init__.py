import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(dir_path)

__version__ = "1.0.0"
__author__ = __maintainer__ = "clr-cera"

NAME = "Quartz"
DOMAIN = ""
IP = ""
PORT = 9999
IPTYPE = "IPV4"  # Can be IPV4 or IPV6, by default goes to IPV4
VERSION = __version__

CONFDIR = os.path.expanduser(f"~/.config/{NAME.lower()}")
sys.path.append(CONFDIR)


def ConfigSetup(configpath):
    if os.path.exists(f"{configpath}"):
        if os.path.exists(f"{configpath}/plugins"):
            if os.path.exists(f"{configpath}/plugins/__init__.py"):
                return

            else:
                f = open(f"{configpath}/plugins/__init__.py", "w")
                f.close()

        else:
            os.mkdir(f"{configpath}/plugins")
    else:
        os.mkdir(configpath)

    ConfigSetup(configpath)


ConfigSetup(CONFDIR)
