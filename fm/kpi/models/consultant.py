from odoo import fields, models

class consultantEmployee(models.Model):
    _inherit = "sale.order"

    consultant = fields.Many2one("hr.employee", string="Consultant")