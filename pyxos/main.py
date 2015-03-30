import uwsgi


def application(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    uwsgi.mule_msg("mule message", 1)
    return [b"Hello World"]
