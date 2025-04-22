from odoo import models, fields

# Library Form model
class LibraryFrom(models.Model):
    _name = "library.form"
    _description = "This is a library management system"

    name = fields.Char(string="Book Name", help="Enter the bookname here")
    description = fields.Text(string="Book Description", help="Enter the bookname description here")
    notes = fields.Html(string="Notes", help="Add additional Notes if you want")

    # # ==== Numeric ====
    pages = fields.Integer(string="Page Number")
    price = fields.Float(string="Book Price")

    # # ==== Date/Time ====
    # published_date = fields.Date(string="Published Date")
    # return_datetime = fields.Datetime(string="Return Dedline")
    # duration = fields.Float(string="Duration in Days", help="Custom time float")

    # # ==== Binary ====
    # book_file =fields.Binary(string="Digital Book File")
    # cover_image = fields.Image(string="Cover Image")

    # # ==== Relational Fields ====
    # author_id = fields.Many2one('res.partner', string="Author")
    # category_ids = fields.Many2many('library.category', string="Categories")
    # publisher_id = fields.Many2one('res.partner', string="Publisher")


    # ==== Selection ====
    # condition = fields.Selection([
    #     ('new', 'New'),
    #     ('used', 'Used'),
    #     ('damaged', 'Damaged'),
    # ], string="Book Condition")

    # # ==== Misc ====
    # sequence = fields.Integer(string="Sequence for sorting")



# Book model
class BookModelForm(models.Model):
    _name = "book.form"
    _description = "This is ongoing task"

    book_name = fields.Char(string="Book Name")
    serial_number = fields.Char(string="Serial Number")


