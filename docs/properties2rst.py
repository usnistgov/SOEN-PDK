import xmltodict
import os
import sys
from glob import iglob

techtop_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
default_propdir = os.path.join(techtop_dir, 'properties')
default_rstdir = os.path.join(techtop_dir, 'docs', 'src', 'properties')
all_propfiles = [os.path.basename(file) for file in iglob(default_propdir + '/*.xml')]

def convert_all(_):
    for filename in all_propfiles:
        properties2rst(os.path.join(default_propdir, filename))


def properties2rst(xmlfile, outdir=None, title=None):
    xmlfile = os.path.realpath(xmlfile)
    filename_base = os.path.splitext(os.path.basename(xmlfile))[0]
    if title is None:
        title = filename_base.lower()

    # Read the XML
    with open(xmlfile, 'r') as fx:
        topdict = xmltodict.parse(fx.read(), process_namespaces=True)
    # strip the top layer
    member_entry = topdict.pop(list(topdict.keys())[0])
    # The next level is usually a list of similar things
    member_list = member_entry.pop(list(member_entry.keys())[0])
    if not isinstance(member_list, list):
        member_list = [member_list]

    # Make outputs
    outlines = []
    outlines.append(title)
    outlines.append('=' * len(title))
    for memb in member_list:
        myname = memb.pop('name')
        outlines.append(myname)
        outlines.append('-' * len(myname))
        outlines.extend(dict2bullets(memb))
        outlines.append('')

    # Write outputs
    if outdir is None:
        # outdir = os.path.dirname(xmlfile)
        outdir = default_rstdir
        print(outdir)
    outfile = os.path.join(outdir, filename_base + '.rst')
    print('writing to', outfile)
    with open(outfile, 'w') as fx:
        fx.write('\n'.join(outlines))


def dict2bullets(d, depth=0):
    ''' Prints a dicttobulletsed list from a nested ordered dictionary '''
    lines = []
    for k, v in d.items():
        base_str = depth * '    ' + '* ' + str(k)
        if isinstance(v, list):
            for val in v:
                lines.append(base_str)
                lines.extend(dict2bullets(val, depth+1))
        elif isinstance(v, dict):
            lines.append(base_str)
            lines.append('')
            lines.extend(dict2bullets(v, depth+1))
        else:
            lines.append(base_str + ' = ' + str(v))
    return lines


if __name__ == '__main__':
    properties2rst(sys.argv[1])
