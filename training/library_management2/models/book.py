from odoo import models, fields

# Book model
class BookModelForm(models.Model):
    _name = "book.form"
    _description = "This is ongoing task"

    book_name = fields.Char(string="Book Name")
    serial_number = fields.Char(string="Serial Number")

    # teacher_id = fields.Many2one('related.model', string="label")
    author_ids =fields.Many2one('library.form', string="Book")
    