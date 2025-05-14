
import os

ENV = bool(os.environ.get("ENV", False))

if ENV:
    from sample_config import config  # noqa
elif os.path.exists("config.py"):
    try:
        try:
            from config import Development as config # type: ignore
        except ModuleNotFoundError:
            raise ModuleNotFoundError("The 'config.py' file could not be found. Please ensure it exists in the correct directory.")
    except ImportError:
        raise ImportError("The 'config.py' file exists but could not be imported. Please ensure it is in the correct location and properly configured.")