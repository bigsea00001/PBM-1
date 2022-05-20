kwargs_list = [
    'dir_check',
    'selenium_ops',
]
kwargs_info = {
    'dir_check': {
        'type': 'func',
        'name': '_dir_check',
        'return': False
    },
    'selenium_ops': {
        'type': 'func',
        'name': '_selenium_options_config',
        'return': True,
        'return_name': 'options'
    },
}


base_info = {
    'dirs': [
        'Data',
        'Data/pkl',
        'Data/chromedriver',
        'Data/download',
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
