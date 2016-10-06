class ResourceInfo:
    def __init__(self, name, folder, ext, default):
        self.name = name
        self.folder = folder
        self.ext = ext
        self.default = default

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

info = ResourceInfo('info', '', '.info',
                    {})

perk = ResourceInfo('perk', 'Perks', '.perk',
                    {})

scenario = ResourceInfo('scenario', 'Scenar,ios', '.scen',
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
    info,
    perk,
    scenario,
    shop
]

folders = map(lambda r: r.folder, all_info)

ext_to_name = {resource.ext: resource.name for resource in all_info}
folder_to_name = {resource.folder: resource.name for resource in all_info}
folder_to_ext = {resource.folder: resource.ext for resource in all_info}
name_to_default = {resource.name: resource.default for resource in all_info}
