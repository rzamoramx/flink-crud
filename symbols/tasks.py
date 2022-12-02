
def log_request(sender, environ, **kwargs):
    method = environ['REQUEST_METHOD']
    host = environ['HTTP_HOST']
    path = environ['PATH_INFO']
    query = environ['QUERY_STRING']
    query = '?' + query if query else ''
    print('New Request -> {method} {host}{path}{query}'.format(
        method=method,
        host=host,
        path=path,
        query=query,
    ))
