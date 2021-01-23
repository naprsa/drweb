try:
    from .dev import *
except ImportError:
    from .prod import *
except ImportError:
    print("Missing production settings file! Exit!")
    quit()
