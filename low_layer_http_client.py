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
        'header': '',
        'encode': 'utf-8'
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

    def connect():
        '''Connect to target server.'''
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((host, port))

    def send(self, body):
        '''Send HTTP request'''
        encode = self.request['encode']
        self.sock.send(encode)
