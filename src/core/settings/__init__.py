from .base import *

try:
    from .dev import *
except ModuleNotFoundError:
    pass

try:
    from .prod import *
except ModuleNotFoundError:
    print("Missing production settings file! Exit!")
    quit()
