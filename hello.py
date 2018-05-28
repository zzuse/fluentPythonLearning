import bobo

'''
    bobo -f hello.py -p 9999
'''
@bobo.query('/')
def hello(person):
    return 'Hello %s!' % person
