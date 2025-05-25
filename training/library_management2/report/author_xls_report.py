from odoo import models
# from xlsxwriter.workbook import Workbook

class AuthorReportXlsx(models.AbstractModel):
    _name="report.library_management2.author_xlsx_report"
    _inherit = "report.report_xlsx.abstract"

    def generate_xlsx(self, workbook, data, authors):
        format_header = workbook.add_format({
            'font_size': 12, 'bold': True, 'align': 'center', 'border': 1
        })

        format_cell = workbook.add_format({
            'font_size': 10, 'align': 'center', 'border': 1
        })

        sheet = workbook.add_worksheet('Author')
        sheet.set_column('A:E', 30)

        headers = ["Author Name", "Email", "Phone"]

        for col, header in enumerate(headers):
            sheet.write(0, col, header, format_header)
        
        row = 1

        for author in authors:
            sheet.write(row, 0, author.name or '', format_cell)
            sheet.write(row, 1, author.description or '', format_cell)
            sheet.write(row, 2, author.notes or '', format_cell)
            row+=1

