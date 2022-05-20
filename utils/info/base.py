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
    'create_db':{
        'type': 'DB_model',
        'func': '_create_db_model',
        '_return': None
    },
}

base_info = {
    'dirs': [
        'Data',
        'Data/pkl',
        'Data/model/',
        'Data/download',
        'Data/chromedriver',
        'log',
    ],
}

selenium_info = {
    'options': [
        'ignore-certificate-errors',
        'dns-prefetch-disable',
        'disable-extensions',
        'headless',
    ],
    'prefs': {'download.default_directory': 'Data/chrome_driver'},
}
