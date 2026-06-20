# =============================================================================
# 《AI法庭》gui.rpy
# GUI 配置 - Cyber Tribunal 风格
# =============================================================================

# -----------------------------------------------------------------------------
# 基础尺寸
# -----------------------------------------------------------------------------

define gui.init_width = 1920
define gui.init_height = 1080

# -----------------------------------------------------------------------------
# 颜色定义 - Cyber Tribunal 配色
# -----------------------------------------------------------------------------

define gui.text_color = "#E8F0FF"
define gui.idle_color = "#8A9AB8"
define gui.idle_hover_color = "#4DD9FF"
define gui.insensitive_color = "#3A4A6C"
define gui.muted_color = "#5A6A8C"
define gui.hover_color = "#4DD9FF"
define gui.selected_color = "#00C8FF"
define gui.selected_hover_color = "#4DD9FF"

define gui.text_size = 28
define gui.name_text_size = 30
define gui.interface_text_size = 24
define gui.label_text_size = 36
define gui.notify_text_size = 22
define gui.title_text_size = 48

# -----------------------------------------------------------------------------
# 字体定义
# -----------------------------------------------------------------------------

define gui.text_font = "SourceHanSansLite.ttf"
define gui.name_text_font = "SourceHanSansLite.ttf"
define gui.interface_text_font = "SourceHanSansLite.ttf"
define gui.system_font = "SourceHanSansLite.ttf"

# -----------------------------------------------------------------------------
# 对话框
# -----------------------------------------------------------------------------

define gui.textbox_height = 320
define gui.textbox_yalign = 1.0
define gui.textbox_background = None

define gui.name_xpos = 60
define gui.name_ypos = 20
define gui.name_xalign = 0.0
define gui.namebox_width = 400
define gui.namebox_height = None
define gui.namebox_background = None

define gui.text_xpos = 80
define gui.text_ypos = 90
define gui.text_width = 1760
define gui.text_xalign = 0.0

# -----------------------------------------------------------------------------
# 按钮样式
# -----------------------------------------------------------------------------

define gui.button_width = None
define gui.button_height = None
define gui.button_borders = Borders(8, 8, 8, 8)
define gui.button_text_font = gui.interface_text_font
define gui.button_text_size = gui.interface_text_size
define gui.button_text_idle_color = gui.idle_color
define gui.button_text_hover_color = gui.hover_color
define gui.button_text_selected_color = gui.selected_color
define gui.button_text_insensitive_color = gui.insensitive_color

# -----------------------------------------------------------------------------
# 存档槽位
# -----------------------------------------------------------------------------

define gui.slot_button_width = 440
define gui.slot_button_height = 320
define gui.slot_button_borders = Borders(10, 10, 10, 10)
define gui.slot_button_text_size = 18
define gui.slot_button_text_xalign = 0.5
define gui.slot_button_text_idle_color = gui.idle_color
define gui.slot_button_text_hover_color = gui.hover_color
define gui.slot_button_text_selected_color = gui.selected_color
define gui.slot_button_text_insensitive_color = gui.insensitive_color

define config.thumbnail_width = 384
define config.thumbnail_height = 216

define gui.file_slot_cols = 2
define gui.file_slot_rows = 2

# -----------------------------------------------------------------------------
# 导航按钮
# -----------------------------------------------------------------------------

define gui.navigation_spacing = 12
define gui.navigation_xalign = 0.5

# -----------------------------------------------------------------------------
# 设置滑块
# -----------------------------------------------------------------------------

define gui.slider_size = 36
define gui.slider_borders = Borders(0, 0, 0, 0)
define gui.slider_tile = False

# -----------------------------------------------------------------------------
# 主菜单 / 游戏菜单
# -----------------------------------------------------------------------------

define gui.main_menu_background = None
define gui.game_menu_background = None
define gui.overlay_background = None

# -----------------------------------------------------------------------------
# 对话历史
# -----------------------------------------------------------------------------

define gui.history_height = 140
define gui.history_name_xpos = 80
define gui.history_name_ypos = 0
define gui.history_name_width = 180
define gui.history_name_xalign = 0.5
define gui.history_text_xpos = 280
define gui.history_text_ypos = 10
define gui.history_text_width = 1540
define gui.history_text_xalign = 0.0

# -----------------------------------------------------------------------------
# 确认 / 跳过
# -----------------------------------------------------------------------------

define gui.confirm_frame_borders = Borders(40, 40, 40, 40)
define gui.skip_ypos = 10
define gui.notify_ypos = 120

# =============================================================================
# GUI 初始化
# =============================================================================

init python:

    # 主色
    HOLO_BLUE = "#00C8FF"
    ICE_BLUE = "#4DD9FF"
    DEEP_BLACK = "#0A0E1A"
    COURT_BLUE = "#0F1A2E"
    STEEL_GRAY = "#2A3A5C"
    COLD_WHITE = "#E8F0FF"
    DIM_GRAY = "#8A9AB8"
    WARN_RED = "#FF3B5C"
    ACCEPT_GREEN = "#00FFA8"
    BALANCE_GOLD = "#FFB800"
    EVIDENCE_PURPLE = "#B070FF"
    INTEGRATION_COLOR = "#00C8FF"
    SEPARATION_COLOR = "#FF6B3B"
    PRAGMATIC_COLOR = "#FFB800"

    # GUI 变量
    gui.textbox_background = Solid("#0A0E1ACC")
    gui.namebox_background = Solid("#0F1A2EAA")
    gui.text_color = COLD_WHITE
    gui.name_text_color = HOLO_BLUE
    gui.idle_color = DIM_GRAY
    gui.hover_color = ICE_BLUE
    gui.selected_color = HOLO_BLUE
    gui.insensitive_color = "#3A4A6C"

    # 滑块
    gui.slider_idle_background = Solid("#2A3A5C")
    gui.slider_hover_background = Solid("#3A5A8C")
    gui.slider_selected_background = Solid(HOLO_BLUE)
    gui.slider_thumb = Solid(ICE_BLUE)
    gui.slider_thumb_shadow = Solid("#000000AA")

    # 滑块（设置用）
    gui.muted_color = "#5A6A8C"
    gui.hover_muted_color = ICE_BLUE
    gui.selected_hover_color = ICE_BLUE

    # 存档槽位背景
    gui.slot_button_background = Solid("#0F1A2EDD")
    gui.slot_button_hover_background = Solid("#1A2A4EDD")
    gui.slot_button_selected_background = Solid("#0A3A5EDD")
    gui.slot_button_insensitive_background = Solid("#1A1A2A55")

    # 导航按钮
    gui.navigation_button_background = None
    gui.navigation_button_hover_background = Solid("#00C8FF22")

    # 主菜单按钮
    gui.main_menu_text_align = 0.5
    gui.main_menu_text_xalign = 0.5

    # 检查按钮（设置中的开关）
    gui.check_button_background = None
    gui.check_button_foreground = None

    # 确认框
    gui.confirm_frame_background = Frame(Solid("#0A0E1AEE"), 10, 10)
    gui.confirm_button_background = Solid("#0F1A2EDD")
    gui.confirm_button_hover_background = Solid("#1A2A4EDD")

    # 跳过指示器
    gui.skip_indicator_background = Solid("#0A0E1ACC")
    gui.skip_indicator_text_color = HOLO_BLUE

    # 通知
    gui.notify_frame_background = Solid("#0A0E1ACC")
    gui.notify_text_color = HOLO_BLUE

    # 名称框
    gui.namebox_borders = None
    gui.name_xpos = 80
    gui.name_ypos = 30
    gui.name_xalign = 0.0
    gui.namebox_width = 400
    gui.namebox_height = None

    # 文本框
    gui.text_xpos = 100
    gui.text_ypos = 100
    gui.text_width = 1720
    gui.text_xalign = 0.0

    # 对话框高度
    gui.textbox_height = 340

# =============================================================================
# 自定义图像 - 纯色背景（无外部资源依赖）
# =============================================================================

image bg_black = Solid(DEEP_BLACK)
image bg_court_blue = Solid(COURT_BLUE)
image bg_deep = Solid(DEEP_BLACK)
image bg_gravestone = Solid("#0F0F1A")
image bg_courtroom = Solid("#0F1A2E")
image bg_judge_desk = Solid("#16213E")
image bg_hologram = Solid("#0A1A3A")
image bg_war = Solid("#2A1A1A")
image bg_iron = Solid("#1A1A1A")
image bg_gray = Solid("#2A2A3A")
image bg_end_a = Solid("#2A1A1A")
image bg_end_b = Solid("#1A1A1A")
image bg_end_c = Solid("#2A2A3A")
