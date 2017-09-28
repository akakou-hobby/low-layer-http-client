# LowLayerHTTPClient
TCP control for http client !
It send request tcp layer, and catch the response.

## Usage
### Installation
  This module has no installer yet, so you can install only yourself.

## Specification
### Instance Variable
#### request
  * host: access point host or ip address
  * port: access point port
  * header: HTTP request header for `send()`
  * encode: coding encode

#### response
  * raw: response binary data
  * all: response coded string data.
  * header: HTTP response header (string).
  * body: HTTP response body(string).
  * decode: coding encode

### Methods
#### \_\_init\_\_(self, host='localhost', port=80, request=False)
It makes new LowLayerHTTPClient instance.
##### Arguments
| name      | type          | description                                                       |
| --------- |:-------------:| ----------------------------------------------------------------- |
| host      | str           | This is host name or ip address that is ownershiped access point. |
| port      | int           | This is port that is ownershiped access point.                    |
| request   | dict(request) | It has request data.                                              |

#### connect(self)
It begin connecting access point.

#### send(self, header=False)
It send just HTTP(on tcp) request.  

##### Arguments
| name      | type          | description                                                                                 |
| --------- |:-------------:| ------------------------------------------------------------------------------------------- |
| header    | str or bool   | If it is not `false`, send the it data as HTTP header, or it choose self.request.header.


#### get_response(self)
It get response while response streamed.

#### close(self)
It close HTTP(TCP) connection.

### Example
Access example.com page.
#### Patern 1
```python
import http_client

client = http_client.LowLayerHTTPClient(host='example.com', port=80)
client.connect()
client.send('GET / HTTP/1.1\r\nHost: www.example.com\r\nConnection: close\r\n\r\n')
response = client.get_response()

print(response['all'])
```

#### Patern 2
```python
import http_client

request = {
    'host': 'example.com',
    'port': 80,
    'header': 'GET / HTTP/1.1\r\nHost: www.example.com\r\nConnection: close\r\n\r\n',
    'encode': 'utf-8'
}

client = http_client.LowLayerHTTPClient(request=request)
client.connect()
client.send(request['header'])
response = client.get_response()
client.close()

print(response['all'])
```
