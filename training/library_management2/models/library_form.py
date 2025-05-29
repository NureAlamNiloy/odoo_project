from odoo import models, fields

# Library Form model
class LibraryFrom(models.Model):
    _name = "library.form"
    _description = "This is a library management system"

    name = fields.Char(string="Author Name", help="Enter the bookname here")
    author_mail = fields.Char(string="Author mail", help="Enter the bookname description here")
    author_mobile = fields.Char(string="Mobile", help="Add additional Notes if you want")
    author_gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], string="Gender")
    author_nationality = fields.Char(string="Author Nationality")

    # student_ids = fields.One2many('related.model', 'inverse_field_name', string="Label")
    book_ids = fields.One2many('book.form', 'author_ids', string="Book")

