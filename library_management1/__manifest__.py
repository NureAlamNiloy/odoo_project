# -*- coding: utf-8 -*-
{
    'name': "library_management1",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
        Long description of module's purpose
    """,

    'author': "Niloy",
    'website': "https://www.linkedin.com/in/nurealamniloy/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Niloy',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','web','website','portal','sale', 'sale_management', 'product' ,'contacts','hr', 'purchase',],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
}

