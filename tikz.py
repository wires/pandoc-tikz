#!/usr/bin/env python3

"""
Pandoc filter to process raw latex tikz environments into images.
Assumes that pdflatex is in the path, and that the standalone
package is available.  Also assumes that ImageMagick's convert
is in the path. Images are put in the tikz-images directory.
"""

import os
import re
import shutil
import sys
from subprocess import call
from tempfile import mkdtemp

import pandocfilters
from pandocfilters import toJSONFilter, Para, Image, get_filename4code, get_extension

lg = open('log.txt', 'w+')

def tikz2image(tikz_src, filetype, outfile):
    tmpdir = mkdtemp()
    olddir = os.getcwd()
    os.chdir(tmpdir)

    f = open('tikz.tex', 'w')
    f.write("""\\documentclass{standalone}
             \\usepackage{tikz}
             \\begin{document}
             """)
    f.write(tikz_src)
    f.write("\n\\end{document}\n")
    f.close()
    lg.write('-------------------\n')
    call(["pdflatex", 'tikz.tex'], stdout=lg)#sys.stderr)
    lg.write('-------------------\n')
    lg.write('files={}\n'.format(os.listdir(tmpdir)))
    os.chdir(olddir)
    lg.write("olddir='{}', tmpdir='{}'\n".format(olddir, tmpdir))
    lg.write("filetype='{}', file='{}'\n".format(filetype, 'tikz.tex'))
    if filetype == 'pdf':
        f1 = os.path.join(tmpdir, 'tikz.pdf')
        f2 = '{}.pdf'.format(outfile)
        lg.write('copied {} to {}'.format(f1, f2))
        shutil.copyfile(f1, f2)
    else:
        f1 = os.path.join(tmpdir, 'tikz.pdf')
        f2 = '{}.{}'.format(outfile, filetype)
        lg.write('---------------------\n --- converting {} to {} --- \n'.format(f1, f2))
        call(["convert", f1, f2], stderr=lg, stdout=lg)
        lg.write('---------------------\n')
    shutil.rmtree(tmpdir)


def tikz(key, value, format, _):
    if key == 'CodeBlock':
        [fmt, code] = value
        if "tikz" in fmt[1]:
            outfile = get_filename4code("tikz", code)
            filetype = get_extension(format, "png", html="png", latex="pdf")
            src = outfile + '.' + filetype
            if not os.path.isfile(src):
                tikz2image(code, filetype, outfile)
                sys.stderr.write('Created image ' + src + '\n')
            return Para([Image(['', [], []], [], [src, ""])])

if __name__ == "__main__":
    lg.write('started\n')
    toJSONFilter(tikz)
    lg.close()
