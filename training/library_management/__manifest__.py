
# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Library Management System',
    'version': '1.1',
    'category': 'niloy',
    'sequence': -100,
    'summary': 'Library Management System.. This is for my day01 task',
    'website': 'https://www.linkedin.com/in/NureAlamNiloy',
    'depends': [
        'base', 
    ],
    'data': [ 
        'views/author.xml',
        'views/book.xml',
        'views/menu.xml',
        'views/member.xml',
    ],
    'installable': True,
    'application': True,
}

