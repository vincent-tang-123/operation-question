
def do_action(args):
    if getattr(args, 'branchname'):
        print(getattr(args, 'branchname'))
    else:
        print('no branchname')
    if getattr(args, 'venv'):
        print(getattr(args, 'venv'))
    else:
        print('no venv')

