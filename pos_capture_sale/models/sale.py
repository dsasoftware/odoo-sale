# -*- coding: utf-8 -*-
###############################################################################
#
#    Trey, Kilobytes de Soluciones
#    Copyright (C) 2014-Today Trey, Kilobytes de Soluciones <www.trey.es>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################
from openerp import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    pos_order_id = fields.Many2one(
        comodel_name='pos.order',
        string='Pos Order',
        readonly=True,
        help="Pos Order relationated.")

    @api.model
    def _setup_fields(self):
        '''Anadir valores al campo state de pedido de ventas.'''
        res = super(SaleOrder, self)._setup_fields()
        if 'state' in self._fields and \
           ('manage_from_pos', 'Manage from PoS') not in\
           self._fields['state'].selection:
                self._fields['state'].selection.append(
                    ('manage_from_pos', 'Manage from PoS'))
        return res
