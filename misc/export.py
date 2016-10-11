from misc import helper
import os


def export_to_file(current_dir, file_location, debug=False):
    # Settings
    settings_dir = current_dir + '/.settings/' + ('debug' if debug else 'std')
    # Settings - Player
    player_data = helper.get_json_data(settings_dir + '/player.json')
    player_data['__type__'] = 'player'
    player_data['stats']['__type__'] = 'player_stats'
    player_data['stats']['health']['__type__'] = 'resource_stat'
    for stat_id, stat_info in player_data['stats']['resource'].items():
        stat_info['__type__'] = 'resource_stat'
    for stat_id, stat_info in player_data['stats']['other'].items():
        stat_info['__type__'] = 'other_stat'
    player_data['inventory']['__type__'] = 'inventory'
    # Settings - Globals
    globals_data = helper.get_json_data(settings_dir + '/globals.json')

    # Funcs
    funcs_dir = current_dir + '/Functions'
    funcs_data = {func_id: func_string for func_id, func_string in ids_info(funcs_dir)}

    # Stats
    # Stats- Health
    health_data = helper.get_json_data(current_dir + '/Stats-Health/health.hlth')
    health_data['__type__'] = 'stat_setting'
    # Stats - Other
    other_ids_info = ids_info(current_dir + '/Stats-Other')
    other_data = {}
    for stat_id, stat_info in other_ids_info:
        stat_info['__type__'] = 'stat_setting'
        other_data[stat_id] = stat_info
    # Stats - Resource
    resource_ids_info = ids_info(current_dir + '/Stats-Resource')
    resource_data = {}
    for stat_id, stat_info in resource_ids_info:
        stat_info['__type__'] = 'stat_setting'
        resource_data[stat_id] = stat_info

    # Items
    items_ids_info = ids_info(current_dir + '/Items')
    items_data = {}
    for item_id, item_info in items_ids_info:
        item_info['__type__'] = 'item'
        items_data[item_id] = item_info

    # Scenarios
    scenarios_ids_info = ids_info(current_dir + '/Scenarios')
    scenarios_data = {}
    for scenario_id, scenario_info in scenarios_ids_info:
        scenario_info['__type__'] = 'scenario'
        for option in scenario_info['options']:
            option['__type__'] = 'option'
        scenarios_data[scenario_id] = scenario_info

    helper.save_json_data(file_location, {
        '__type__': 'campaign',
        'player': player_data,
        'globals': globals_data,
        'funcs': funcs_data,
        'stats': {
            '__type__': 'stat_settings',
            'health': health_data,
            'resource': resource_data,
            'other': other_data
        },
        'items': items_data,
        'scenarios': scenarios_data
    })


def ids_info(start_dir):
    for (dirpath, dirnames, filenames) in os.walk(start_dir):
        folder_paths = os.path.split(os.path.relpath(dirpath, start_dir))
        folder_paths = [folder for folder in folder_paths if folder not in ('', '.')]
        prefix = '.'.join(folder_paths)
        for filename in filenames:
            resource_id = os.path.splitext(filename)[0]
            data = helper.get_json_data(dirpath + '/' + filename)
            if prefix:
                yield prefix + '.' + resource_id, data
            else:
                yield resource_id, data
