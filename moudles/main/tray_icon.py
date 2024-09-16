from PyQt5.QtWidgets import QApplication, QSystemTrayIcon, QMenu, QAction
from PyQt5.QtGui import QIcon, QPixmap, QPainter, QColor
from PyQt5.QtCore import Qt
import sys
from pathlib import Path

def create_pixmap_with_background(icon_pixmap, background_color_str):
    # 解析背景颜色字符串
    r, g, b = map(int, background_color_str.split(','))
    background_color = QColor(r, g, b)
    
    # 创建一个与图标相同大小的背景 pixmap
    size = icon_pixmap.size()
    background_pixmap = QPixmap(size)
    background_pixmap.fill(background_color)
    
    # 在背景上绘制图标
    painter = QPainter(background_pixmap)
    painter.drawPixmap(0, 0, icon_pixmap)
    painter.end()
    
    return background_pixmap

def tray_icon(fridge_skin_close, fridge_skin_open, background_color):
    app = QApplication(sys.argv)
    
    # 确保路径是字符串
    if isinstance(fridge_skin_close, Path):
        fridge_skin_close = str(fridge_skin_close)
    if isinstance(fridge_skin_open, Path):
        fridge_skin_open = str(fridge_skin_open)
    
    # 加载图标 pixmap
    close_pixmap = QPixmap(fridge_skin_close)
    open_pixmap = QPixmap(fridge_skin_open)
    
    # 创建具有背景颜色的图标 pixmap
    close_pixmap_with_bg = create_pixmap_with_background(close_pixmap, background_color)
    open_pixmap_with_bg = create_pixmap_with_background(open_pixmap, background_color)
    
    # 创建系统托盘图标
    tray_icon = QSystemTrayIcon(QIcon(close_pixmap_with_bg), app)
    
    # 图标切换逻辑
    icons = [QIcon(close_pixmap_with_bg), QIcon(open_pixmap_with_bg)]
    current_icon_index = 0
    
    def toggle_icon():
        nonlocal current_icon_index
        current_icon_index = (current_icon_index + 1) % len(icons)
        tray_icon.setIcon(icons[current_icon_index])
    
    def handle_icon_activation(reason):
        if reason == QSystemTrayIcon.Trigger:
            toggle_icon()
    
    tray_icon.activated.connect(handle_icon_activation)
    
    # 创建托盘菜单
    menu = QMenu()
    
    # 添加 "Exit" 动作并连接到槽函数
    exit_action = QAction("Exit", app)
    exit_action.triggered.connect(app.quit)
    menu.addAction(exit_action)
    
    tray_icon.setContextMenu(menu)
    tray_icon.show()
    
    sys.exit(app.exec_())

# 示例用法
if __name__ == "__main__":
    tray_icon(
        'path_to_close_icon.png', 
        'path_to_open_icon.png', 
        '255,255,255'  # 背景颜色: 白色
    )
