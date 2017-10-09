from .viewmodelbase import ViewModelBase


class RegisterViewModel(ViewModelBase):
    def __init__(self):
        self.email = None
        self.password = None
        self.confirm_password = None
        self.error = None

    def from_dict(self, post_data):
        # Accessing the name attribute in the form
        self.email = post_data.get('email')
        self.password = post_data.get('password')
        self.confirm_password = post_data.get('confirm_password')

    def validate(self):
        self.error = None
        if self.password != self.confirm_password:
            self.error = "Error: The passwords do not match!"
            return

        if not self.email:
            self.error = "Error: email cannot be empty!"

        if not self.password:
            self.error = "Error: password cannot be empty"

