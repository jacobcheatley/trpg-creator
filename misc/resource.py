class ResourceInfo:
    def __init__(self, name, folder, ext):
        self.name = name
        self.folder = folder
        self.ext = ext

ability = ResourceInfo('ability', 'Abilities', '.abil')
buff = ResourceInfo('buff', 'Buffs', '.buff')
enemy = ResourceInfo('enemy', 'Enemies', '.enem')
function = ResourceInfo('function', 'Functions', '.func')
item = ResourceInfo('item', 'Items', '.item')
info = ResourceInfo('info', '', '.info')
perk = ResourceInfo('perk', 'Perks', '.perk')
scenario = ResourceInfo('scenario', 'Scenarios', '.scen')
shop = ResourceInfo('shop', 'Shops', '.shop')

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
