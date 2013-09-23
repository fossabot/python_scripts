import os
import difflib
import sys
import re
import filecmp

for dirname, dirnames, filenames in os.walk(sys.argv[1]):
  for filename in filenames:
    match = re.search('.map$', filename)
    if match:
      newfile = dirname + '/' + filename
      #newfile = os.file.join(dirname, filename)
      oldfile = newfile + '.old'
      result = filecmp.cmp(newfile, oldfile)
      if not result:
        print newfile + ' > ' + oldfile
      diff = difflib.unified_diff(open(newfile).readlines(), open(oldfile).readlines())
      sys.stdout.writelines(diff)

      #result = os.system('diff ' + newfile + ' ' + oldfile)
