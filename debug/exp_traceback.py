# -*- coding: utf-8 -*-
import traceback


try:
    result = '1' + 2
    print(result)
except Exception as err:
    print(err)
    print(traceback.format_exc())
