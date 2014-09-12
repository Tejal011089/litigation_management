# Copyright (c) 2013, GNU and Contributors
# See license.txt

import frappe
import unittest

test_records = frappe.get_test_records('Litigator')

class TestLitigator(unittest.TestCase):
	pass
