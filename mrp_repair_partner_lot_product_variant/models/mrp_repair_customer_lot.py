# Copyright 2019 Alfredo de la Fuente - AvanzOSC
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
from odoo import models, fields


class MrpRepairCustomerLot(models.Model):
    _inherit = 'mrp.repair.customer.lot'

    product_id = fields.Many2one(
        comodel_name='product.product', string='Product variant',
        related='product_code.product_id', store=True)
    default_code = fields.Char(
        string='Internal reference', related='product_id.default_code',
        store=True)
