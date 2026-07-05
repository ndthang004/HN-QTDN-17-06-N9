# -*- coding: utf-8 -*-
{
    'name': 'Quản lý văn bản',
    'version': '15.0.1.0',
    'summary': 'Quản lý văn bản doanh nghiệp',
    'description': 'Module quản lý văn bản đến, hợp đồng, báo giá và tài liệu pháp lý',

    'author': 'FIT-DNU',
    'website': '',

    'category': 'Management',
    'depends': ['base'],

    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],

    'installable': True,
    'application': True,
    'auto_install': False,
}
