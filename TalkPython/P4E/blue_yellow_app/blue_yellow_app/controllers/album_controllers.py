import pyramid_handlers

from ..infrastructure.supressor import suppress
from .base_controller import BaseController
from ..services.albums_service import AlbumsService


class AlbumController(BaseController):

    @pyramid_handlers.action(renderer='templates/albums/index.pt')
    def index(self):
        # data/service access
        albums = AlbumsService.get_albums()

        # return the model
        return {"albums": albums}
