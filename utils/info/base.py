kwargs_schema = {
    'dir_check': str,
    'selenium_ops': str,
}

kwargs_list = [
    'dir_check',
    'selenium_ops',
]

kwargs_info = {
    'dir_check': {
        'type': 'func',
        'func': '_dir_check',
        '_return': None,
    },
    'selenium_ops': {
        'type': 'func',
        'func': '_selenium_options_config',
        '_return': 'options',
    },
    'add_db': {
        'type': 'func',
        'func': '_add_db_model',
        '_return': None
    },
    'db_conn':{
        'type': 'func',
        'func': '_get_conn',
        '_return': 'conn'
    },
}

base_info = {
    'dirs': [
        'Data',
        'Data/log',
        'Data/pkl',
        'Data/model/',
        'Data/etc_info',
        'Data/download',
        'Data/chromedriver',
        'Data/model/database',
    ],
}

selenium_info = {
    'options': [
        'ignore-certificate-errors',
        'dns-prefetch-disable',
        'disable-extensions',
        'headless',
    ],
    'prefs': {'download.default_directory': 'Data/chromedriver'},
}
