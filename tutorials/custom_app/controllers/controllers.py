# -*- coding: utf-8 -*-
# from odoo import http


# class CustomApp(http.Controller):
#     @http.route('/custom_app/custom_app', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom_app/custom_app/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom_app.listing', {
#             'root': '/custom_app/custom_app',
#             'objects': http.request.env['custom_app.custom_app'].search([]),
#         })

#     @http.route('/custom_app/custom_app/objects/<model("custom_app.custom_app"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom_app.object', {
#             'object': obj
#         })

