import pyramid_handlers

from .. import static_cache


class HomeController:
    def __init__(self, request):
        self.request = request

    @pyramid_handlers.action(renderer="templates/home/index.pt")
    def index(self):
        return {
            'value': "HOME",
            'build_cache_id': static_cache.build_cache_id
        }

    @pyramid_handlers.action(renderer="templates/home/about.pt")
    def about(self):
        return {
            'value': "ABOUT",
            'build_cache_id': static_cache.build_cache_id
        }

    @pyramid_handlers.action(renderer="templates/home/contact.pt")
    def contact(self):
        return {
            'value': "CONTACT",
            'build_cache_id': static_cache.build_cache_id
        }
