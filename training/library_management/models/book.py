from odoo import models, fields


#Book Model

class bookModel(models.Model):
    _name = "library.book"
    _description = "This model for book"

    book_name = fields.Char(string="Book Name")
    serial_no = fields.Char(string="Serial Number")
    price = fields.Integer(string="Book Price")
    available_copies = fields.Integer(string="Available Copies")