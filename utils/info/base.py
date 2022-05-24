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
    'db_conn': {
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
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36',
    ],
    'prefs': {'download.default_directory': 'Data/chromedriver'},
}
