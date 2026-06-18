// =============================================================================
// 《AI法庭》options.rpy
// 项目配置文件
// =============================================================================

define config.name = _("AI法庭")

define gui.show_name = True

define config.version = "1.0.0"

define gui.about = _("2088年，全球首个AI法庭开庭。\n你是首席法官，你的判决定义未来。")

define build.name = "AI_Tribunal"

define config.has_sound = True
define config.has_music = True
define config.has_voice = True

define config.main_menu_music = None
define config.game_menu_music = None

define config.window_icon = None

define config.save_directory = "AI_Tribunal-1.0"

define config.skip_indicator = True
define config.has_autosave = True
define config.autosave_slots = 10
define config.autosave_on_choice = True
define config.autosave_on_quit = True

define config.default_language = None

init python:
    if len(config.translations) == 0:
        config.translations = {}

define config.window_title_format = "AI法庭 - AI Tribunal"

define config.screen_width = 1920
define config.screen_height = 1080

define config.rollback_enabled = True
define config.rollback_length = 256
define config.hard_rollback_limit = 100
