from __future__ import with_statement

import os

from cStringIO import StringIO
from glob import glob
from os import path, environ
from os.path import abspath
from re import compile
from shutil import copy
from subprocess import call, STDOUT
from tempfile import TemporaryFile
from testfixtures import TempDirectory, compare
from xlrd import Book, biff_dump

initial = os.getcwd()
base = abspath(path.join(path.dirname(abspath(__file__)), os.pardir))
runner = abspath(path.join(base, 'bin', 'py'))
examples = path.join(base, 'students')
expected = path.join(base, 'tests', 'expected')

sub_res = [
    (compile('0+x[0-9A-Fa-f]+'), '...'),
    (compile('".+'+os.sep.replace('\\','\\\\')+'(.+.py)"'), '"\\1"'),
    ]

def get_biff_records(data):
    outfile = StringIO()
    bk = Book()
    bk.biff2_8_load(file_contents=data, logfile=outfile, )
    biff_dump(bk.mem, bk.base, bk.stream_len, 0, outfile, unnumbered=True)
    return outfile.getvalue()
    
def check_example(package, filename):
    example_dir = path.join(examples, package)
    expected_dir = path.join(expected, package)
    expected_base = path.join(expected_dir, path.splitext(filename)[0])
        
    try:
        
        with TempDirectory() as actual:
            # copy files to the directory
            copy(path.join(example_dir, filename), actual.path)
            for pattern in ('*.xls', '*.bmp'):
                for fixture in glob(path.join(example_dir, pattern)):
                    copy(fixture, actual.path)

            os.chdir(actual.path)
            output = TemporaryFile('w+')

            # run the example
            before_listing = set(os.listdir(actual.path))
            call([runner, filename], stdout=output, stderr=STDOUT)
            after_listing = set(os.listdir(actual.path))

            # check the console output
            output.seek(0)
            actual_output = output.read().strip().replace('\r', '')
            for re, rp in sub_res:
                actual_output = re.sub(rp, actual_output)
            expected_path = expected_base+'.txt'
            if not path.exists(expected_path):
                expected_output = ''
            else:
                expected_output = open(expected_path).read().strip().replace('\r', '')
            compare(expected_output, actual_output)

            # check the files created
            created = after_listing.difference(before_listing)

            expected_names = set()
            if os.path.exists(expected_base):
                expected_names = set(os.listdir(expected_base))
                
            for name in created:
                with open(path.join(actual.path, name), 'rb') as af:
                    actual_data = af.read()

                if name in expected_names:
                    expected_path = path.join(expected_base, name)
                    expected_data = open(expected_path, 'rb').read()
                    expected_names.remove(name)
                    if actual_data != expected_data:
                        if environ.get('REPLACE_EXAMPLES'):
                            with open(expected_path, 'wb') as new_expected:
                                new_expected.write(actual_data)
                        compare(
                            get_biff_records(expected_data),
                            get_biff_records(actual_data),
                            )
                else:
                    raise AssertionError("unexpected output: %s" % name)
            
            for name in expected_names:
                if name != '.svn':
                    print created
                    raise AssertionError("expected output missing: %s" % name)
        
            
    finally:
        os.chdir(initial)
    
def test_examples():
    for package in ('xlrd', 'xlwt', 'xlutils'):
        for py in glob(path.join(examples, package, '*.py')):
            yield check_example, package, path.split(py)[1]
        
