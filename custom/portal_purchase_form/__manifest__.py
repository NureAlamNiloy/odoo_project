# -*- coding: utf-8 -*-
{
    'name': "Portal Purchase Form",

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
        'views/purchase_field.xml',
        'views/inharit_portal_link.xml',
        'views/purchase_form.xml',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
'application':True,
}

