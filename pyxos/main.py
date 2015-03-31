import uwsgi


def application(env, start_response):
    start_response('200 OK', [('Content-Type','text/html')])
    uwsgi.mule_msg("calling leader", 1)
    return [b"Hello World"]
