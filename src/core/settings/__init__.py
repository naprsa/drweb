dev_import_error = False

try:
    from .dev import *
except ImportError:
    dev_import_error = True

if dev_import_error:
    try:
        from .prod import *
    except ImportError:
        print("Missing production settings file! Exit!")
        quit()
