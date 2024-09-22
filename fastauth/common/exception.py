class FastAuthError(Exception):
    """
    Base Exception for FastAuth witch all fastauth exceptions should inherit from.
    """

    pass


class DatabaseError(FastAuthError):
    pass


class NotFoundError(FastAuthError):
    pass
