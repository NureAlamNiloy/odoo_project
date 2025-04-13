from odoo import api, fields, models


class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _description = "Test hospital model"

    name = fields.Char(string='Name')
    age = fields.Integer(String="Age")
    gender = fields.Selection([('male', 'Male'), ('female','Female')], string="Gender")