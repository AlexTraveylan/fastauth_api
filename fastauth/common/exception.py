class FastAuthError(Exception):
    """
    Base Exception for FastAuth witch all fastauth exceptions should inherit from.
    """

    def __init__(self, status_code: int, message: str):
        self.status_code = status_code
        self.message = message
