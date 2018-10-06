#!/srv/conda/bin/python
import pexpect

child = pexpect.spawnu('git push origin master')
child.expect('.*Username.*')
child.sendline('cathowlet1@163.com')
child.expect('.*Password.*')
child.sendline('kdijbxJIDhHDL2938')
child.interact()
