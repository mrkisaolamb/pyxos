import uwsgi
from roles.scout import Scout

def mule_loop():
    while True:
        print "mule: Waiting for messages... yawn."
        message = uwsgi.mule_get_msg()
        scout = Scout(message)

if __name__ == '__main__':
    mule_loop()
