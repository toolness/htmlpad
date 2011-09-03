from fabric.context_managers import settings, cd
from fabric.api import task, env
from fabric.operations import run

env.proj_root = '/var/htmlpad.org'
REPO_URL = "git://github.com/hackasaurus/htmlpad.git"
DJANGO_REPO = "/var/repositories/django"

def run_manage_cmd(cmd):
    with cd('%s/htmlpad_dot_org' % env.proj_root):
        run('python manage.py %s' % cmd)

@task
def clone():
    run('git clone %s %s' % (REPO_URL, env.proj_root))
    with cd(env.proj_root):
        run('git submodule init')
        run('git config submodule.vendor/django.url %s' % DJANGO_REPO)
        run('git submodule update')

@task
def update():
    with cd(env.proj_root):
        run('git pull')

@task
def deploy():
    update()
    run_manage_cmd('collectstatic --noinput')
    run_manage_cmd('test')
    run('touch %s/wsgi/htmlpad.wsgi' % env.proj_root)
