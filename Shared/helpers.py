import time


def decode_errors(data_errors, map_fields={}):
    """
    Decode errors from serializer
    :param data_errors: errors serializer
    :param map_fields: dict to map fields to new one
    :return: list of error
    """

    if not data_errors:
        return []

    if isinstance(data_errors, list):
        errors = []
        for error_detail in data_errors:
            errors += mapping_error_message(error_detail, map_fields)
        return errors
    else:
        return mapping_error_message(data_errors, map_fields, validate=True)


def mapping_error_message(error_detail, map_fields, validate=False):
    errors = []

    for key, value in error_detail.items():
        message = mapping_message_item(map_fields, key, value, validate)
        errors.append(message)
    return errors


def mapping_message_item(map_fields, key, value, validate):
    if isinstance(value, list) and validate:
        value = str(value[0])

    new_key = map_fields.get(key, key)
    item = {
        "field": new_key,
        "message": value
    }
    return


def generate_order_number():
    return f'ORD-{int(time.time())}'