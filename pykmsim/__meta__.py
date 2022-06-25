# `name` is the name of the package as used for `pip install package`
name = "pykmsim"
# `path` is the name of the package for `import package`
path = name.lower().replace("-", "_").replace(" ", "_")
# Your version number should follow https://python.org/dev/peps/pep-0440 and
# https://semver.org
version = "0.1.0"
author = "Rachit Jain"
author_email = "rachit.jain@wustl.edu"
description = "This is a python rewrite of kmsim to allow for better maintainbility and usability"  # One-liner
url = "https://github.com/jrachit10/pykmsim"  # your project homepage
license = "MIT"  # See https://choosealicense.com
