import pyramid_handlers

from .base_controller import BaseController
from ..infrastructure.supressor import suppress


class HomeController(BaseController):

    @pyramid_handlers.action(renderer='templates/home/index.pt')
    def index(self):
        return {'value': 'HOME'}

    @pyramid_handlers.action(renderer='templates/home/contact.pt')
    def contact(self):
        return {'value': 'CONTACT'}

    @pyramid_handlers.action(renderer='templates/home/about.pt')
    def about(self):
        return {'value': 'ABOUT'}

    @suppress
    def do_not_expose_as_web_action(self):
        print("Called do_not_expose_as_web_action")
