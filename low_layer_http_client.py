'''Low Layer HTTP Client

low_layler_http_client.py
    This program send HTTP request with TCP and get response.
'''
import socket


class TCP():
    '''Send http request with TCP and get response.'''
    request = {
        'host': '',
        'port': 80,
        'header': '',
        'encode': 'utf-8'
    }

    response = {
        'raw': '',
        'all': '',
        'header': '',
        'body': '',
        'decode': 'utf-8'
    }

    def __init__(self, host, port):
        '''Get arguments and set information for response packet.'''
        self.request['host'] = host
        self.request['port'] = port

    def connect(self):
        '''Connect to target server.'''
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.request['host'], self.request['port']))

    def send(self, body):
        '''Send HTTP request'''
        self.request['body'] = body
        encode = self.request['encode']
        self.sock.send(body.encode(encode))

    def get_response(self):
        '''Get HTTP Response'''
        data = []

        chunk = 'null'
        while chunk!=b'':
            chunk = self.sock.recv(4096)
            data.append(chunk)

        self.response['raw'] = b''.join(data)
        decode = self.response['decode']
        self.response['all'] = self.response['raw'].decode(decode)
        divide_response = self.response['all'].split('\r\n\r\n')

        self.response['header'] = ''.join(divide_response[0])
        self.response['body'] = ''.join(divide_response[1:])

        return self.response

    def close(self):
        '''Close HTTP connection'''
        self.sock.close()
