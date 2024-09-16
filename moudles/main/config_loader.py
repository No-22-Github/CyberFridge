import os
import toml
from pathlib import Path

# 读取配置文件
config = toml.load('config.toml')

# 从配置中获取相关信息
main = config['Main']
fridge = config['Fridge']

theme_dir = Path(main['theme_dir'])
skin = Path(fridge['skin'])
plugins_dir = Path(main['plugins_dir'])

# 冰箱的图标
fridge_icon = ["fridge_open.svg", "fridge_close.svg"]

# 背景颜色
background_color = str(fridge['background_color'])

def checker():
    print(f"CyberFridge_Version: {main['version']}")
    print(f"Chara_Version: {main['chara_version']}")
    print("--------------------")
    print(f"Themes: {skin}")    
    try:
        if theme_dir.is_dir():
            # 遍历目录中的所有条目
            for item in theme_dir.iterdir():
                if item.is_dir():
                    print(item.name)
        else:
            print(f"Error: {theme_dir} is not a directory.")
    except Exception as e:
        print(f"An error occurred: {e}")
    print("--------------------")
    print("Plugins:")
    
    try:
        if plugins_dir.is_dir():
            # 遍历目录中的所有条目
            for item in plugins_dir.iterdir():
                if item.is_dir():
                    print(item.name)
        else:
            print(f"Error: {plugins_dir} is not a directory.")
    except Exception as e:
        print(f"An error occurred: {e}")
    print("--------------------")
    print(f"背景颜色: {background_color}")

def path_mapper():
    fridge_skin_dir = theme_dir / skin
    icon_in_directory = os.listdir(fridge_skin_dir)
    missing_icons = [file for file in fridge_icon if file not in icon_in_directory]
    if not missing_icons:
        print("所有必需的图标都存在")
        fridge_skin_close = fridge_skin_dir / 'fridge_close.svg'
        fridge_skin_open = fridge_skin_dir / 'fridge_open.svg'
    else:
        print("以下图标未找到:")
        for file in missing_icons:
            print(f"- {file}")
    return fridge_skin_close, fridge_skin_open, background_color       
