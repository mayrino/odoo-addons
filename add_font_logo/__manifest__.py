# -*- coding: utf-8 -*-
{
    'name': "Add_font_logo",

    'summary': """
        add fontebled logo
     """,

    'description': """
       add a company  font logo  
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
        'layout/font_logo_layout.xml',
        
    ],
 
    "application": False,
    "installable": True,
}