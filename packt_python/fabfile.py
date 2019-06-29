from fabric.api import run


def hello():
    print("Hello World")


def host_type():
    run('uname -s')


# fab -H localhost host_type
