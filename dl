#!#!/srv/conda/bin/python
import os, pexpect

child = pexpect.spawnu('git clone https://github.com/bobpip/stores')
child.expect('.*Username.*')
child.sendline('cathowlet1@163.com')
child.expect('.*Password.*')
child.sendline('kdijbxJIDhHDL2938')
child.interact()
