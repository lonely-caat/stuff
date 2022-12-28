#!/usr/bin/env python

import re
import optparse

parser = optparse.OptionParser()
parser.add_option('-f', '--file', help='enter file location and file name , e.g. /home/test/lama.py', dest="location",
    action='store', type='str')
parser.add_option('-p', '--prefix', help='prefix to add to the test name , e.g. lama', dest="prefix",
    action='store', type='str')
parser.add_option('-R', '--reset', help='Reset all IDs', dest="reset",
    action='store_true')

opts, args = parser.parse_args()

if not opts.location or not opts.prefix:
    print "mandatory option is missing\n"
    parser.print_help()
    exit(-1)

print 'Processing %s ...' % opts.prefix

with open(opts.location, 'r') as fh:
    c = 1
    new_l = ''

    for line in fh.readlines():
        if re.match(r".*@attr\(", line):
            if not re.match(r".*id='%s-" % opts.prefix, line) or opts.reset:
                line = re.sub(r"id='[^']+'( ,|,)", "id='%s-%s'," % (opts.prefix, c), line)
            c += 1
        new_l += line

with open(opts.location, 'w') as f_out:
    f_out.writelines(new_l)

#EOF