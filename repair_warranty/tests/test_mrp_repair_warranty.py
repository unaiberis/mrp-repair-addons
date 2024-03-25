# Copyright 2019 Daniel Campos - AvanzOSC
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import odoo.tests.common as common


class TestMrpRepairWarranty(common.TransactionCase):
    def setUp(self):
        super().setUp()
        self.mrp_repair_model = self.env["repair.order"]
        self.product = self.browse_ref("product.product_product_3")
        self.location_id = self.ref("stock.stock_location_locations")
        self.customer = self.env["res.partner"].create(
            {
                "name": "Test Customer",
                "is_company": True,
                "company_id": self.env.user.company_id.id,
            }
        )
        vals = {
            "name": "test",
            "product_id": self.product.id,
            "location_id": self.location_id,
            "product_uom": self.product.uom_id.id,
            "partner_id": self.customer.id,
            "invoice_method": "after_repair",
        }
        self.mrp_repair_customer = self.mrp_repair_model.create(vals)

    def test_warranty(self):
        self.assertEqual(self.mrp_repair_customer.invoice_method, "after_repair")
        self.mrp_repair_customer.is_in_warranty = True
        self.mrp_repair_customer.onchange_warranty()
        self.assertEqual(self.mrp_repair_customer.invoice_method, "none")
