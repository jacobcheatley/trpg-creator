from misc import helper
import config


class ResourceInfo:
    def __init__(self, name, folder, ext, default, create=True, subfolder=True, delete=True):
        self.name = name
        self.folder = folder
        self.ext = ext
        self.default = default
        self.create = create
        self.subfolder = subfolder
        self.delete = delete


# <editor-fold desc="Resource Info">
ability = ResourceInfo('ability', 'Abilities', '.abil',
                       {})

buff = ResourceInfo('buff', 'Buffs', '.buff',
                    {})

enemy = ResourceInfo('enemy', 'Enemies', '.enem',
                     {})

function = ResourceInfo('function', 'Functions', '.func',
                        '')

item = ResourceInfo('item', 'Items', '.item',
                    {
                        'name': '',
                        'desc': '',
                        'value': 0,
                        'use': '',
                        'equip': None
                    })

perk = ResourceInfo('perk', 'Perks', '.perk',
                    {})

res_stat = ResourceInfo('resource stat', 'Stats-Resource', '.reso',
                        {
                            'name': '',
                            'desc': ''
                        },
                        subfolder=False)

other_stat = ResourceInfo('other stat', 'Stats-Other', '.othr',
                          {
                              'name': '',
                              'desc': ''
                          },
                          subfolder=False)

health_stat = ResourceInfo('health stat', 'Stats-Health', '.hlth',
                           {
                               'name': 'health',
                               'desc': 'Health'
                           },
                           create=False, delete=False, subfolder=False)

scenario = ResourceInfo('scenario', 'Scenarios', '.scen',
                        {
                            'name': '',
                            'desc': '',
                            'options': []
                        })

shop = ResourceInfo('shop', 'Shops', '.shop',
                    {})

all_info = [
    ability,
    buff,
    enemy,
    function,
    item,
    perk,
    res_stat,
    other_stat,
    health_stat,
    scenario,
    shop
]
# </editor-fold>

folders = list(map(lambda r: r.folder, all_info))

# Yes, this is ugly. But it's the easiest way to convert from available data to other needed data.
ext_to_name = {resource.ext: resource.name for resource in all_info}
folder_to_name = {resource.folder: resource.name for resource in all_info}
folder_to_ext = {resource.folder: resource.ext for resource in all_info}
name_to_default = {resource.name: resource.default for resource in all_info}
folder_to_object = {resource.folder: resource for resource in all_info}
ext_to_object = {resource.ext: resource for resource in all_info}


def create_config_files(directory, campaign_name):
    # /.settings
    settings_dir = directory + '/.settings'
    player_data = {
        'scenario': 'start',
        'stats': {},
        'inventory': {
            'currency': 0,
            'items': {}
        }
    }
    export_data = {
        'name': campaign_name,
        'creator': config.get('default_creator'),
        'about': ''
    }
    helper.save_json_data(settings_dir + '/std/player.json', player_data)
    helper.save_json_data(settings_dir + '/debug/player.json', player_data)
    helper.save_json_data(settings_dir + '/std/globals.json', {})
    helper.save_json_data(settings_dir + '/debug/globals.json', {})
    helper.save_json_data(settings_dir + '/export.json', export_data)
