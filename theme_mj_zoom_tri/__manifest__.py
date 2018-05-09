# -*- coding: utf-8 -*-
{
    'name': "theme_mj_zoom_tri",

    'summary': """
        A widget be used to MJ home site for new arreved items
     """,

    'description': """
        Customised a widget be used to MJ home page,also can be used anywhere if you want , likes 
        others widget what uesd be in odoo system .
    """,

    'author': "Samon Xie",
    'website': "http://www.mayrino.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Hidden',
    'version': '0.1',
     "contributors": [
        "Samon Xie <reyesxie@foxmail.com>",
    ],
    # any module necessary for this one to work correctly
    'depends': ['base','website'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/snippet.xml',
        'views/assets.xml',
        'views/options.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    "application": False,
    "installable": True,
}