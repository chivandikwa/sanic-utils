# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestClass::test_valid_json_no_exception_returns_object 1'] = {
    'identifier': 'test_id',
    'name': 'test_name'
}
