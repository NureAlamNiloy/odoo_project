
{
    'name': 'KPI Calclution',
    'version': '1.1',
    'category': 'niloy',
    'sequence': -99,
    # 'sequence': -100,
    'website': 'https://www.linkedin.com/in/NureAlamNiloy',
    'depends': [
        'base', 'stock', 'sale_management', 'account', 'hr',
    ],
    'data': [ 
        'views/consultant.xml',
        'views/consultant_groupby.xml',
    ],
    'installable': True,
    'application': True,
    # 'license': 'LGPL-4',
}
