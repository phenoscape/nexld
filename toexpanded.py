from __future__ import print_function
from pyld import jsonld
import json
import sys
compacted = json.load(open(sys.argv[1], 'r'))
print(compacted)
expanded = jsonld.expand(compacted)
print(json.dumps(expanded, indent=2))
