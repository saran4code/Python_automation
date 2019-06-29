from fabric.api import local


def test():
    local("./manage2.py test my_app")

def commit():
    local("git add manage2.py && git commit -m 'automatic commit message'")

def push():
    local("git push")

def prepare_deploy():
    test()
    commit()
    push()
