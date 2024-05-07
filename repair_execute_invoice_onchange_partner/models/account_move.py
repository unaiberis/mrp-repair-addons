# Copyright 2023 Alfredo de la Fuente - AvanzOSC
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
from odoo import api, models


class AccountMove(models.Model):
    _inherit = "account.move"

    @api.model
    def create(self, vals):
        move = super(AccountMove, self).create(vals)
        if "create_move_from_repair" in self.env.context:
            move._onchange_partner_id()
        return move
