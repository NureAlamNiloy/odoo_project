from odoo import models, fields, api
from datetime import date
from odoo.exceptions import ValidationError

# Book model
class BookModelForm(models.Model):
    _name = "book.form"
    _description = "This is ongoing task"
    _rec_name = 'book_name'

    book_name = fields.Char(string="Book Name")
    serial_number = fields.Char(string="Serial Number")
    total_page = fields.Integer(string="Total Pages")
    published_date = fields.Date(string="Published Date")
    book_age = fields.Integer(string="Age of book", compute="total_age", store=True)
    book_image = fields.Image(string="Book Cover")

    # teacher_id = fields.Many2one('related.model', string="label")
    author_ids =fields.Many2one('library.form', string="Author")  
    
    @api.depends('published_date') #Which field we depend for our operation 
    def total_age(self):
        if self.published_date:
            self.book_age = date.today().year - self.published_date.year 
        else:
            self.book_age = 0
    
    @api.onchange('book_name')
    def auto_serial_number(self):
        if self.book_name:
            self.serial_number = f"{self.book_name[:2]}/{date.today().day}/{date.today().month}/{date.today().year}"


    @api.constrains('total_page', 'published_date')
    def validation(self):
        if self.total_page <10:
            raise ValidationError("Total pages must be at least 10.")


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
    
    @api.model
    def update_book_age(self):
        books = self.search([])
        for book in books:
            if book.published_date:
                book.book_age = date.today().year - book.published_date.year


    

class inheritInventory(models.Model):
    _inherit = 'product.template'

    book_list = fields.Many2one("book.form", string="Books")

