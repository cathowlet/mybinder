#!/srv/conda/bin/python
import pexpect
import os

os.system('git config --global user.email "you@example.com" && git config --global user.name "Your Name" && git add . && git commit -m "0"')
child = pexpect.spawnu('git push origin master')
child.expect('.*Username.*')
child.sendline('cathowlet1@163.com')
child.expect('.*Password.*')
child.sendline('kdijbxJIDhHDL2938')
child.interact()
