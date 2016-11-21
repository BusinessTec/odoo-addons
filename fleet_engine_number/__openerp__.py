# -*- coding:utf-8 -*-
##############################################################################
#
#    Copyright (C) 2015 Sucros Clear Information Technologies PLC.
#    All Rights Reserved.
#
#    This program is free software: you can redistribute it and/or modify it
#    under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Fleet - Vehicle Engine Number',
    'summary': 'Add engine number to vehicle record',
    'description': """
Fleet - Vehicle Engine Number
=============================
This module adds a new field, Engine Number, to a fleet vehicle.
    """,
    'author': 'Sucros Clear Information Technologies PLC',
    'website': 'http://www.clearict.com',
    'version': '1.0',
    'category': 'Managing vehicles and contracts',
    'depends': [
        'fleet',
    ],
    'data': [
        'views/fleet.xml',
    ],
    'test': [
    ],
    'demo_xml': [
    ],
    'installable': True,
    'active': False,
}
