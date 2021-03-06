# -*- coding: utf-8 -*-
#
# Univention Admin Modules
#  unit tests: settings/printeruri tests
#
# Copyright 2004-2012 Univention GmbH
#
# http://www.univention.de/
#
# All rights reserved.
#
# The source code of this program is made available
# under the terms of the GNU Affero General Public License version 3
# (GNU AGPL V3) as published by the Free Software Foundation.
#
# Binary versions of this program provided by Univention to you as
# well as other copyrighted, protected or trademarked materials like
# Logos, graphics, fonts, specific documentations and configurations,
# cryptographic keys etc. are subject to a license agreement between
# you and Univention and not subject to the GNU AGPL V3.
#
# In the case you use this program under the terms of the GNU AGPL V3,
# the program is provided in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public
# License with the Debian GNU/Linux or Univention distribution in file
# /usr/share/common-licenses/AGPL-3; if not, see
# <http://www.gnu.org/licenses/>.


from GenericTest import GenericTestCase


class SettingsPrinterURITestCase(GenericTestCase):
	def __init__(self, *args, **kwargs):
		self.modname = 'settings/printeruri'
		super(SettingsPrinterURITestCase,
		      self).__init__(*args, **kwargs)

	def setUp(self):
		super(SettingsPrinterURITestCase,
		      self).setUp()
		self.createProperties = {
			'printeruri': {'append': ['/dev/null', '/dev/zero']},
			}
		self.modifyProperties = {
			'printeruri': {'append': ['/dev/bogus'],
				       'remove': ['/dev/zero']},
			}
		self.name = 'testprinterurisetting'


def suite():
	import sys, unittest
	suite = unittest.TestSuite()
	suite.addTest(SettingsPrinterURITestCase())
	return suite


if __name__ == '__main__':
	import unittest
	unittest.TextTestRunner().run(suite())
