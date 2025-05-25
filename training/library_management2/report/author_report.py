from odoo import models, api

class LibraryAuthorReport(models.AbstractModel):
    _name ="report.library_management2.author_report_template"
    _description = 'Author books list report'


    @api.model
    def get_report_values(self, docids, data=None):
        authors = self.env['library.form'].browse(docids)
        result = []

        for author in authors:
            result.append({
                'author': author,
                'books': author.book_ids,
            })

            return {
                'doc_ids': docids,
                'doc_model': 'library.form',
                'author_data': result,
            }