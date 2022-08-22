import urllib.parse


class ParseData:

    @staticmethod
    def parse_data(data: str):
        result = {}
        if data:
            for item in data.split('&'):
                k, v = item.split('=')
                result[k] = v
        return result


class GetRequests(ParseData):

    @staticmethod
    def get(environ):
        query_string = environ['QUERY_STRING']
        request_params = GetRequests.parse_data(query_string)
        return request_params


class PostRequests(ParseData):

    @staticmethod
    def get_bytes_string(env) -> bytes:
        content_length_data = env.get('CONTENT_LENGTH')
        content_length = int(content_length_data) if content_length_data else 0
        data = env.get('wsgi.input').read(content_length) if content_length > 0 else b''
        return data

    def get(self, environ):
        data = self.get_bytes_string(environ)
        if data:
            data_str = data.decode(encoding='utf-8')
            data = {k: urllib.parse.unquote(v) for k, v in self.parse_data(data_str).items()}
        return data
