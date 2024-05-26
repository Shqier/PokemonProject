from sqlalchemy.types import TypeDecorator, VARCHAR
import json
# https://docs.sqlalchemy.org/en/20/core/custom_types.html#marshal-json-strings

class JSONString(TypeDecorator):
    """Represents an immutable structure as a json-encoded string.

    Usage:

        JSONEncodedDict(255)

    """

    impl = VARCHAR

    cache_ok = True

    def process_bind_param(self, value, dialect):
        if value is not None:
            value = json.dumps(value)

        return value

    def process_result_value(self, value, dialect):
        if value is not None:
            value = json.loads(value)
        return value
