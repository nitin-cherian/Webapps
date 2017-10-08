import pyramid_handlers

from ..infrastructure.supressor import suppress
from .base_controller import BaseController


class AccountController(BaseController):

    @pyramid_handlers.action(renderer='templates/account/index.pt')
    def index(self):
        return {}

    @pyramid_handlers.action(renderer='templates/account/signin.pt')
    def signin(self):
        return {}

    # GET /account/register
    @pyramid_handlers.action(renderer='templates/account/register.pt',
                             request_method='GET',
                             name='register')
    def register_get(self):
        print("Calling register for GET..")
        return {}

    # POST /account/register
    @pyramid_handlers.action(renderer='templates/account/register.pt',
                             request_method='POST',
                             name='register')
    def register_post(self):
        email = self.request.POST.get('email')
        pw = self.request.POST.get('password')
        pw_confirmation = self.request.POST.get('confirm_password')

        print("Calling register for POST.., email={}, password={}, confirm={}".format(email, pw, pw_confirmation))

        # validate no account exists, match passwords
        # Create account in DB
        # send welcome email

        # redirect
        print("Redirecting to account index page..")
        self.redirect('/account')
