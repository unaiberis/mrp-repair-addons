# Copyright 2023 Alfredo de la Fuente - AvanzOSC
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
from odoo import models


class RepairOrder(models.Model):
    _inherit = "repair.order"

    def action_move_create(self, group=False):
        return super(
            RepairOrder, self.with_context(create_move_from_repair=True)
        ).action_move_create(group=group)
