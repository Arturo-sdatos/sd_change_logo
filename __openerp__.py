# -*- encoding: utf-8 -*-
##############################################################################
#
#    Sistemas de Datos, Open Source Management Solution
#    Copyright (C) 2014 Sistemas de Datos (http://www.sdatos.com).
#    
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see http://www.gnu.org/licenses/.
#
##############################################################################

{
    'name': 'Change Logo',
    'version': "1.0",
    'author': 'Arturo Esparragón Goncalves',
    'category': "Tools",        
    'description': """
    This module change the default logo to the Sistemas de Datos.
    """,
    'website': 'http://www.sdatos.com',
    'depends': ['web'],    
    'data': [],
    'qweb': ['static/src/xml/base.xml'],
    'css': ['static/src/css/login.css'],
    'demo': [],
    'installable': True,
    'auto_install': False,
#    'certificate': 'certificate',
}