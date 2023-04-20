from typing import Dict
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED

from .custom_config import HTTPResponseCode
# from shared.custom_jaeger import create_tags_response
from .helpers import decode_errors as format_errors


def response(code, data=None, message=None, status=False, meta=None,
             errors=None, sys_errors=None, count=None, extra: Dict = None, error=None, attributes=None):
    if code in (HTTP_200_OK, HTTP_201_CREATED):
        status = True

    if errors:
        errors = format_errors(errors)

    else:
        if sys_errors:
            message = sys_errors

    if message is None:
        message = get_response_message(code)

    result = []
    if data or code == HTTP_200_OK:
        result = getattr(data, 'data', None) or data

    response = {'code': code, 'message': message, 'success': status, 'meta': meta, 'result': result}

    if errors:
        response['errors'] = errors

    if error:
        response['error'] = error

    if count:
        response['count'] = count

    if result:
        response['result'] = result

    if extra:
        response.update(extra)

    if attributes:
        response['attributes'] = attributes

    response_body = response.copy()
    # create_tags_response(response_body, code)

    return response


def get_response_message(code):
    message = next(iter(
        [res.value.get("message") for res in HTTPResponseCode if res.value.get("code") == code]
    ), "")
    return message


def decode_errors(errors):
    temp_errors = []
    if isinstance(errors, list):
        for error_detail in errors:
            for key, value in error_detail.items():
                item = {
                    "field": key,
                    "message": value
                }
                temp_errors.append(item)
    else:
        temp_errors.append(errors)

    return temp_errors
