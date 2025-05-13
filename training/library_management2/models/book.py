from odoo import models, fields

# Book model
class BookModelForm(models.Model):
    _name = "book.form"
    _description = "This is ongoing task"
    _rec_name = 'book_name'

    book_name = fields.Char(string="Book Name")
    serial_number = fields.Char(string="Serial Number")

    # teacher_id = fields.Many2one('related.model', string="label")
    author_ids =fields.Many2one('library.form', string="Author")  
    
    def orm_search(self):
        book_search = self.env["book.form"].search([])
        print("Search ORM output ", book_search)
        for name in book_search:
            print(f"book name {name.book_name} Author > {name.author_ids.name}")
    
    def orm_browse(self):
        book_browse = self.env["book.form"].browse(1)
        print("browse ORM output ", book_browse)
        for name in book_browse:
            print(f"book name {name.book_name} Author > {name.author_ids.name}")



class inheritInventory(models.Model):
    _inherit = 'product.template'

    book_list = fields.Many2one("book.form", string="Books")

