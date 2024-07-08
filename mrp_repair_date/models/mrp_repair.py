# (c) 2015 Alfredo de la Fuente - AvanzOSC
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
from odoo import fields, models


class MrpRepair(models.Model):
    _inherit = "repair.order"

    scheduled_departure_date = fields.Date(copy=False)
    start_date = fields.Date(readonly=True, copy=False)
    end_date = fields.Date(readonly=True, copy=False)

    def action_repair_start(self):
        result = super().action_repair_start()
        self.write({"start_date": fields.Date.context_today(self)})
        return result

    def action_repair_end(self):
        result = super().action_repair_end()
        self.write({"end_date": fields.Date.context_today(self)})
        return result

    def action_cancel_draft(self):
        result = super().action_cancel_draft()
        self.write({"start_date": False, "end_date": False})
        return result
