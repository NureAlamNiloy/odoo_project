# -*- coding: utf-8 -*-

from odoo import models, fields


# class portal_purchase_form(models.Model):
#     _name = 'portal_purchase_form.portal_purchase_form'
#     _description = 'portal_purchase_form.portal_purchase_form'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

class InheritPurchase(models.Model):
    _inherit = 'purchase.order'

    employee_id = fields.Many2one('hr.employee', string="Employee")



class InheritEmployee(models.Model):
    _inherit = 'hr.employee'

    niloy = fields.Char(string="Job ID")