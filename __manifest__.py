{
    'name': 'Cash on Delivery (COD)',
    'version': '1.0',
    'summary': 'Enable Cash on Delivery Payment Method',
    'description': 'Provide Cash on Delivery payment option for customers in Odoo 17',
    'category': 'Accounting',
    'author': 'Your Name',
    'depends': ['payment', 'sale'],
    'data': [
        'data/cod_payment_data.xml',
        'views/cod_payment_views.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
