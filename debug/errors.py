class PydactylError(Exception):
    """Base class for exceptions in this module."""
    pass

class InvalidRequestMethodError(PydactylError):
    """Exception raised for errors in the authentication process.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message="Invalid Request Method"):
        self.message = message
        super().__init__(self.message)