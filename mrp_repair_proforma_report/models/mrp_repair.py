# (c) 2015 Esther Martín - AvanzOSC
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import fields, models


class MrpRepair(models.Model):
    _inherit = 'mrp.repair'

    proforma = fields.Boolean(string='Proforma')
