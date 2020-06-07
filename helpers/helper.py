from subprocess import PIPE, STDOUT, run
from os import getcwd

def run_task(path, task, _input):
    cmd = "%s/%s.py" % (path, task)
    return run(['python3', cmd], input = _input.encode('utf-8'), stderr=STDOUT, stdout = PIPE).stdout.decode('utf-8')

if __name__ == '__main__':
    print(run_task('test', '01', 'hello'))

