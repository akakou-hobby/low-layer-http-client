'''Low Layer HTTP Client

low_layler_http_client.py
    This program send HTTP request with TCP and get response.
'''


class TCP():
    '''Send http request with TCP and get response.'''
    request = {
        'url': '',
        'host': '',
        'port': 80,
        'header': ''
    }

    response = {
        'header': '',
        'body': '',
        'encode': 'utf-8'
    }

    def __init__(self, url, host, port):
        '''Get arguments and set information for response packet.'''
        self.request['url'] = url
        self.request['host'] = host
        self.request['port'] = port
