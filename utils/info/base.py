base_info = {
    'selenium': {
        'ops': {
            'headless',
            'ignore-certificate-errors',
            'dns-prefetch-disable',
            'disable-extensions',
        },
        'prefs': {'download.default_directory' : 'Data/chrome_driver'},
    },
    'directories': [
        'Data',
        'Data/pkl',
        'Data/chromedriver',
        'Data/download',
    ],
    'functions': [
        'a_function',
        'b_function',
        'c_function',
    ],
}
