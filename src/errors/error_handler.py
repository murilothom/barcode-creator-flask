from src.errors.error_types.http_bad_request_entity import HttpBadRequestEntityError
from src.views.http_types.http_response import HttpResponse

def handle_errors(error: Exception) -> HttpResponse:
    if isinstance(error, HttpBadRequestEntityError):
        return HttpResponse(
            status_code=error.status_code,
            body={
                "errors": [{
                    "title": error.name,
                    "detail": error.message
                }]
            }
        )

    return HttpResponse(
        status_code=500,
        body={
            "errors": [{
                "title": "Internal Server Error",
                "detail": str(error)
            }]
        }
    )
