from odoo import http
from odoo.http import request


class NiloyPortal(http.Controller):
    @http.route('/niloy_portal', auth='user', website=True)
    def list_purchase_orders(self, **kw):
        orders = request.env['purchase.order'].search([])
        return request.render('niloy_portal.portal_my_purchase_orders', {
            'orders': orders
        })

