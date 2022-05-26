from utils import info, DB_model

parameters = list(info.base.kwargs_info.keys())

def type_hinting_by_exec(argus):
    for idx_argu, argu in enumerate(argus):
        if argu == 'add_db':
            exec(f'argus[{idx_argu}]: DB_model')

        exec(f'argus[{idx_argu}]: int = 1')
        print(f'{argu}: {type(argus[idx_argu])}')

type_hinting_by_exec(parameters)
