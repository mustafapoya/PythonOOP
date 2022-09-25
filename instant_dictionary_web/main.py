import justpy as jp

from instant_dictionary_web.webapp.about import About
from instant_dictionary_web.webapp.dictionary import Dictionary
from instant_dictionary_web.webapp.home import Home


jp.Route(Home.path, Home.serve)
jp.Route(About.path, About.serve)
jp.Route(Dictionary.path, Dictionary.serve)
jp.justpy(port=8001)