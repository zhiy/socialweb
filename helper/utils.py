#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
def pprint(obj):
    return json.dumps(obj,sort_keys=True,indent=4)
