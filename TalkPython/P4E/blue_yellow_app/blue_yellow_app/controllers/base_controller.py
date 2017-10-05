from ..infrastructure.static_cache import build_cache_id
from ..infrastructure.supressor import suppress
import pyramid.renderers


class BaseController:

    def __init__(self, request):
        self.request = request
        self.build_cache_id = build_cache_id

        layout_render = pyramid.renderers.get_renderer("blue_yellow_app:templates/shared/_layout.pt")
        impl = layout_render.implementation()
        self.layout = impl.macros['layout']

    @property
    def is_logged_in(self):
        return False

    @suppress
    def do_not_expose_as_web_action_base(self):
        print("Called do_not_expose_as_web_action_base")
