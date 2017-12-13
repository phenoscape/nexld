from __future__ import print_function
from pyld import jsonld
import json
import sys
raw = json.load(open(sys.argv[1], 'r'))
expanded = jsonld.expand(raw)
flattened = jsonld.flatten(expanded)
print(json.dumps(flattened, indent=2))
