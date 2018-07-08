import os
import sys
import pexpect

branch = 'test1'
password = 'moments9021'

def main(branch, password):
    try:
        os.system('git init')
        os.system('git add .')
        os.system('git commit -m "$(date)"')
        child = pexpect.spawn('git push origin master:%s' % branch)
        child.expect('.*name.*')
        child.sendline('1230221121@stu.cjlu.edu.cn')
        child.expect('.*word.*')
        child.sendline('%s' % password)
    except Exception as e:
        print(e)
    
if __name__ == "__main__":
    main(branch, password)