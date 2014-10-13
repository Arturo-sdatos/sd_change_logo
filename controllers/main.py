# -*- encoding: utf-8 -*-
##############################################################################
#
#    Sistemas de Datos, Open Source Management Solution
#    Copyright (C) 2004-2014 Arturo Esparragón Goncalves (http://sdatos.com). All Rights Reserved
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

from web import http
from openerp.addons.web.controllers.main import Database, db_list
openerpweb = http

class Database_restrict(Database):
    @openerpweb.jsonrequest
    def create(self, req, fields):

        # check if it is not first installation - restrict!

        dblist = db_list(req)
        if len(dblist) > 0:
            raise Exception('Not allowed')

        return super(Database_restrict, self).create(req, fields)

    @openerpweb.jsonrequest
    def duplicate(self, req, fields):
        raise Exception('Not allowed')

    @openerpweb.jsonrequest
    def drop(self, req, fields):
        raise Exception('Not allowed')

    @openerpweb.httprequest
    def backup(self, req, backup_db, backup_pwd, token):
        raise Exception('Not allowed')

    @openerpweb.httprequest
    def restore(self, req, db_file, restore_pwd, new_db):
        raise Exception('Not allowed')

    @openerpweb.jsonrequest
    def change_password(self, req, fields):
        raise Exception('Not allowed')
    
Database_restrict()