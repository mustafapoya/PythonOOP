import inspect

import justpy as jp

from instant_dictionary_web.webapp.about import About
from instant_dictionary_web.webapp.dictionary import Dictionary
from instant_dictionary_web.webapp.home import Home
from instant_dictionary_web.webapp.home import Page

imports = list(globals().values())

for obj in imports:
    if inspect.isclass(obj):
        if issubclass(obj, Page) and obj is not Page:
            jp.Route(obj.path, obj.serve)

# jp.Route(Home.path, Home.serve)
# jp.Route(About.path, About.serve)
# jp.Route(Dictionary.path, Dictionary.serve)
jp.justpy(port=8001)