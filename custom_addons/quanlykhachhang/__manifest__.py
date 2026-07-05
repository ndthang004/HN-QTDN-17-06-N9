{
    'name': 'Quan Ly Khach Hang',
    'version': '15.0.1.0',
    'category': 'Management',
    'summary': 'Quan ly khach hang va so hoa ho so',

    'depends': [
        'base',
        'hr'
    ],

    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/khachhang_views.xml',
        'views/vanban_views.xml',
    ],

    'installable': True,
    'application': True,
}