import argparse
from args_action import do_action

# 启动命令
# python3 parser.py -b aaa -v mmm

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='构建 docker 的参数')
    # parser.add_argument('--branchname', '-b', help='分支名', required=True)
    parser.add_argument('--branchname', '-b', help='分支名', required=False)
    # parser.add_argument('--venv', '-v', help='环境 lls or cdl', required=True)
    parser.add_argument('--venv', '-v', help='环境 lls or cdl', required=False)

    args = parser.parse_args()
    # print(dir(args))
    # print(getattr(args, 'branchname'))
    # print(getattr(args, 'venv'))
    do_action(args)