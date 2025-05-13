
# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Library Management Test',
    'version': '1.1',
    'category': 'niloy',
    'sequence': -95,
    'summary': 'Library Management System.. This is for my day01 task',
    'website': 'https://www.linkedin.com/in/NureAlamNiloy',
    'depends': [
        'base', 'stock', 'product'
    ],
    'data': [ 
        'security/ir.model.access.csv',
        'views/book.xml',
        'views/library_form.xml',
        'views/menu.xml',
        'views/booklist.xml',
    ],
    'installable': True,
    'application': True,
    # 'license': 'LGPL-4',
}
