# this script should be run as:
# bin\py runall.py

import os

from glob import glob
from os.path import join as j, abspath
from re import compile
from subprocess import call,STDOUT
from tempfile import TemporaryFile
from testfixtures import diff

runner = abspath(j(os.path.split(__file__)[0], 'bin', 'py'))

sub_res = [
    (compile('0+x[0-9A-Fa-f]+'),'...'),
    (compile('".+'+os.sep.replace('\\','\\\\')+'(.+.py)"'),'"\\1"'),
    ]

base = os.path.abspath('..')
for path in ('xlrd','xlwt','xlutils'):
    dir = j(base,'students',path)
    expected_dir = j(base,'expected',path)
    os.chdir(dir)
    for py in glob(j(dir,'*.py')):
        name = os.path.split(py)[1]

        before_listing = set(os.listdir(dir))
        print py
        
        output = TemporaryFile('w+')
        expected_base = j(expected_dir,os.path.splitext(name)[0])

        call([runner,py],stdout=output,stderr=STDOUT)

        after_listing = set(os.listdir(dir))
        created = after_listing.difference(before_listing)

        expected_names = set()
        if os.path.exists(expected_base):
            expected_names = set(os.listdir(expected_base))
        for name in created:
            ap = j(dir,name)
            af = open(ap,'rb')
            actual = af.read()
            af.close()
            if name in expected_names:
                expected = open(j(expected_base,name),'rb').read()
                expected_names.remove(name)
                if actual==expected:
                    os.remove(ap)
                else:
                    print 'different:',name
            else:
                print "unexpected:",name
        for name in expected_names:
            if name!='.svn':
                print "missing:",name
        
        output.seek(0)
        output = output.read().strip().replace('\r','')
        for re,rp in sub_res:
            output = re.sub(rp,output)
        expected_path = j(expected_base+'.txt')
        if not os.path.exists(expected_path):
            expected = ''
        else:
            expected = open(expected_path).read().strip().replace('\r','')
        if output!=expected:
            print '='*len(name)
            print diff(expected,output)
            print '='*len(name)
        
