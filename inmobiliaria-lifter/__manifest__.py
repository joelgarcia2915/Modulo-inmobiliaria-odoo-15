# -*- coding: utf-8 -*-
{
    'name': "inmobiliaria lifter",

    'summary': """
        aplicacion para el manejo de propiedades""",

    'description': """
        Para inmobiliaria que gestione los inmuebles y sus detalles
    """,

    'author': "Joel Garcia",
    'website': "http://linkfly.to/joelgarcia",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',

        'views/inmobiliaria.xml',
        'views/property_type.xml',

        'views/menus.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}