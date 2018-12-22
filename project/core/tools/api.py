from rest_framework.utils.serializer_helpers import ReturnDict
from rest_framework.views import exception_handler

def problem_exception_handler(exc, context):
    """
    Define our own REST exception handler.

    This way we can return problem json-like responses and handle custom exceptions.
    """
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    # Transform 400 response data into a problem json compatible structure.
    if hasattr(response, "status_code") and response.status_code == 400:
        errors = []

        # Handle return dictionaries.
        if isinstance(response.data, ReturnDict):
            for field in response.data:
                for message in response.data[field]:
                    errors.append({
                        "message": message,
                        "field": field
                    })

        # Overwrite the response data with our custom structure.
        response.data = {
            "errors": errors
        }

    return response
