from itertools import product
from pickle import FALSE

from odoo import http
from odoo.http import request
from odoo import fields
from odoo.http import request

class PortalPurchaseForm(http.Controller):
    @http.route('/portal_purchase_form', auth='public', website=True)
    def index(self, **kw):
        user_id = request.env.user  # user dorsiii
        employee_id = request.env['hr.employee'].sudo().search([('user_id', '=', user_id.id)], limit=1)
        # product = request.env['product.template'].sudo().search([('name', '=', product)], limit=1)


        return request.render('portal_purchase_form.purchase_portal_from', {
            "employee_id":employee_id,

        })



    @http.route('/purchase_form/submit', auth="public", website=True, methods=['GET', 'POST'], csrf=False)
    def purchase_form_submit(self, **post):
        product = post.get("product2")
        vendorName = post.get("vendor_name2")
        vendorreference = post.get("vendor_ref")
        quentity = int(post.get("quentity") or 0)
        unit_price = float(post.get("unit_price") or 0.0)

        # Find or create vendor
        vendor = request.env['res.partner'].sudo().search([('name', '=', vendorName)], limit=1)
        if not vendor:
            vendor = request.env['res.partner'].sudo().create({"name": vendorName})

        # Find product
        product2 = request.env['product.product'].sudo().search([('name', '=', product)], limit=1)
        if not product2:
            return "Product not found"

        # Create purchase order with order line
        create_purchase_order = request.env['purchase.order'].sudo().create({
            "partner_id": vendor.id,
            "partner_ref": vendorreference,
            "order_line": [(0, 0, {
                "product_id": product2.id,
                "name": product2.name,
                "product_qty": quentity,
                "price_unit": unit_price,
                "date_planned": fields.Date.today(),
            })]
        })

        return "Purchase order created successfully"



