from odoo import fields, models

class ConsultantGroupByFilter(models.Model):
    _inherit = "sale.report"

    consultant = fields.Many2one("hr.employee", string="Consultant", readonly=True)

    def _select(self):
        res = super()._select()
        res += ", s.consultant as consultant"
        return res

    def _group_by(self):
        res = super()._group_by()
        res += ", s.consultant"
        return res