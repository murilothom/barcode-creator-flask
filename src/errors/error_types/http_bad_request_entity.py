class HttpBadRequestEntityError(Exception):

    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message
        self.name = "BadRequestEntity"
        self.status_code = 400
