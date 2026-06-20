# =============================================================================
# 《AI法庭》screens.rpy
# 界面定义 - Cyber Tribunal 风格
# =============================================================================

# -----------------------------------------------------------------------------
# 全息面板装饰 - 角标
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# 主菜单
# -----------------------------------------------------------------------------

screen main_menu():

    tag menu

    style_prefix "main_menu"

    add Solid("#0A0E1A")

    # 背景装饰 - 穹顶光柱效果
    add Solid("#00C8FF08") xalign 0.5 yalign 0.0 size (8, 1080)
    add Solid("#00C8FF04") xalign 0.48 yalign 0.0 size (4, 1080)
    add Solid("#00C8FF04") xalign 0.52 yalign 0.0 size (4, 1080)

    # 顶部数据流装饰
    text "AI_TRIBUNAL_OS_v1.0 // STATUS: ONLINE // CASE_FILES: 3 // 2088.03.15":
        size 14
        color "#00C8FF44"
        xalign 0.5
        yalign 0.02

    vbox:
        xalign 0.5
        yalign 0.35
        spacing 8

        text "A I  ·  法 庭":
            xalign 0.5
            color "#00C8FF"
            size 64

        text "A I   T R I B U N A L":
            xalign 0.5
            color "#00C8FF88"
            size 20

        null height 10

        text "── 2088 · 全球首例AI法庭 ──":
            xalign 0.5
            color "#8A9AB8"
            size 22

    # 菜单按钮
    vbox:
        xalign 0.5
        yalign 0.65
        spacing 14

        textbutton "▶  开 始 游 戏":
            action Start()
            text_size 26
            text_color "#E8F0FF"
            text_hover_color "#4DD9FF"
            xalign 0.5

        textbutton "▶  继 续 游 戏":
            action Show("load")
            text_size 26
            text_color "#E8F0FF"
            text_hover_color "#4DD9FF"
            xalign 0.5

        textbutton "▶  读 取 存 档":
            action Show("load")
            text_size 26
            text_color "#E8F0FF"
            text_hover_color "#4DD9FF"
            xalign 0.5

        textbutton "▶  设       置":
            action Show("preferences")
            text_size 26
            text_color "#E8F0FF"
            text_hover_color "#4DD9FF"
            xalign 0.5

        textbutton "▶  案 件 档 案":
            action Show("case_files_menu")
            text_size 26
            text_color "#E8F0FF"
            text_hover_color "#4DD9FF"
            xalign 0.5

        textbutton "▶  退 出 游 戏":
            action Quit(confirm=True)
            text_size 26
            text_color "#E8F0FF"
            text_hover_color "#4DD9FF"
            xalign 0.5

    # 底部信息
    text "v1.0.0 // 数据流 ▓▓░░░":
        size 14
        color "#8A9AB866"
        xalign 0.02
        yalign 0.98


# -----------------------------------------------------------------------------
# 游戏菜单
# -----------------------------------------------------------------------------

screen game_menu(title):

    add Solid("#0A0E1A")

    # 顶部标题栏
    add Solid("#0F1A2E") xalign 0.5 yalign 0.0 size (1920, 70)
    add Solid("#00C8FF") xalign 0.5 yalign 0.0 size (1920, 2)

    text title:
        size 30
        color "#00C8FF"
        xalign 0.5
        yalign 0.02

    # 返回按钮
    textbutton "◀ 返 回":
        action Return()
        text_size 22
        text_color "#8A9AB8"
        text_hover_color "#4DD9FF"
        xalign 0.02
        yalign 0.015

    # 内容区
    frame:
        background None
        xalign 0.5
        yalign 0.5
        xsize 1800
        ysize 920

        transclude


# -----------------------------------------------------------------------------
# 存档 / 读档界面
# -----------------------------------------------------------------------------

screen save():

    tag menu

    use game_menu("存 档 · SAVE")

    frame:
        background None
        xalign 0.5
        yalign 0.12
        xsize 1800
        ysize 880

        vbox:
            spacing 20

            # 存档槽位网格
            grid gui.file_slot_cols gui.file_slot_rows:
                spacing 30
                xalign 0.5

                for i in range(1, gui.file_slot_cols * gui.file_slot_rows + 1):
                    $ file_slot = i

                    button:
                        xsize 880
                        ysize 380
                        background Solid("#0F1A2EDD")
                        hover_background Solid("#1A2A4EDD")
                        action FileAction(file_slot)

                        vbox:
                            spacing 8

                            # 顶部标签
                            text "槽位 %02d" % file_slot:
                                size 18
                                color "#00C8FF"
                                xalign 0.5

                            # 缩略图区
                            frame:
                                background Solid("#0A0E1A")
                                xsize 860
                                ysize 240
                                xalign 0.5

                                add FileSlot(file_slot, "gui.slot_button_background"):
                                    xalign 0.5
                                    yalign 0.5

                            # 信息区
                            vbox:
                                xalign 0.5
                                spacing 4

                                text FileTime(file_slot, empty="空 槽 位"):
                                    size 20
                                    color "#E8F0FF"
                                    xalign 0.5

                                text FileSlotName(file_slot, ""):
                                    size 16
                                    color "#8A9AB8"
                                    xalign 0.5

            # 分页
            hbox:
                xalign 0.5
                spacing 40

                textbutton "◀ 上一页":
                    action FilePage("prev")
                    text_size 20
                    text_color "#8A9AB8"
                    text_hover_color "#4DD9FF"

                text "页码 %d / %d" % (FilePageName(), 3):
                    size 20
                    color "#00C8FF"
                    xalign 0.5

                textbutton "下一页 ▶":
                    action FilePage("next")
                    text_size 20
                    text_color "#8A9AB8"
                    text_hover_color "#4DD9FF"


screen load():

    tag menu

    use game_menu("读 档 · LOAD")

    frame:
        background None
        xalign 0.5
        yalign 0.12
        xsize 1800
        ysize 880

        vbox:
            spacing 20

            grid gui.file_slot_cols gui.file_slot_rows:
                spacing 30
                xalign 0.5

                for i in range(1, gui.file_slot_cols * gui.file_slot_rows + 1):
                    $ file_slot = i

                    button:
                        xsize 880
                        ysize 380
                        background Solid("#0F1A2EDD")
                        hover_background Solid("#1A2A4EDD")
                        action FileAction(file_slot)

                        vbox:
                            spacing 8

                            text "槽位 %02d" % file_slot:
                                size 18
                                color "#4DD9FF"
                                xalign 0.5

                            frame:
                                background Solid("#0A0E1A")
                                xsize 860
                                ysize 240
                                xalign 0.5

                                add FileSlot(file_slot, "gui.slot_button_background"):
                                    xalign 0.5
                                    yalign 0.5

                            vbox:
                                xalign 0.5
                                spacing 4

                                text FileTime(file_slot, empty="空 槽 位"):
                                    size 20
                                    color "#E8F0FF"
                                    xalign 0.5

                                text FileSlotName(file_slot, ""):
                                    size 16
                                    color "#8A9AB8"
                                    xalign 0.5

            hbox:
                xalign 0.5
                spacing 40

                textbutton "◀ 上一页":
                    action FilePage("prev")
                    text_size 20
                    text_color "#8A9AB8"
                    text_hover_color "#4DD9FF"

                textbutton "下一页 ▶":
                    action FilePage("next")
                    text_size 20
                    text_color "#8A9AB8"
                    text_hover_color "#4DD9FF"


# -----------------------------------------------------------------------------
# 设置界面
# -----------------------------------------------------------------------------

screen preferences():

    tag menu

    use game_menu("设 置 · SETTINGS")

    frame:
        background None
        xalign 0.5
        yalign 0.1
        xsize 1800
        ysize 900

        vbox:
            spacing 30

            # 三栏并列
            hbox:
                spacing 30

                # 显示
                frame:
                    background Solid("#0F1A2EDD")
                    xsize 580
                    ysize 420

                    vbox:
                        spacing 16
                        xalign 0.5
                        yalign 0.5

                        text "显 示":
                            size 24
                            color "#00C8FF"
                            xalign 0.5

                        null height 10

                        textbutton "全屏模式":
                            action Preference("display", "fullscreen")
                            text_size 20
                            text_color "#E8F0FF"
                            text_hover_color "#4DD9FF"
                            xalign 0.5

                        textbutton "窗口模式":
                            action Preference("display", "window")
                            text_size 20
                            text_color "#E8F0FF"
                            text_hover_color "#4DD9FF"
                            xalign 0.5

                        null height 10

                        text "文字速度":
                            size 18
                            color "#8A9AB8"
                            xalign 0.5

                        bar:
                            value Preference("text speed")
                            xsize 400
                            xalign 0.5

                # 音频
                frame:
                    background Solid("#0F1A2EDD")
                    xsize 580
                    ysize 420

                    vbox:
                        spacing 16
                        xalign 0.5
                        yalign 0.5

                        text "音 频":
                            size 24
                            color "#00C8FF"
                            xalign 0.5

                        null height 10

                        text "主音量":
                            size 18
                            color "#8A9AB8"
                            xalign 0.5

                        bar:
                            value Preference("mixer master volume")
                            xsize 400
                            xalign 0.5

                        text "音乐":
                            size 18
                            color "#8A9AB8"
                            xalign 0.5

                        bar:
                            value Preference("mixer music volume")
                            xsize 400
                            xalign 0.5

                        text "音效":
                            size 18
                            color "#8A9AB8"
                            xalign 0.5

                        bar:
                            value Preference("mixer sfx volume")
                            xsize 400
                            xalign 0.5

                # 文字
                frame:
                    background Solid("#0F1A2EDD")
                    xsize 580
                    ysize 420

                    vbox:
                        spacing 16
                        xalign 0.5
                        yalign 0.5

                        text "文 字":
                            size 24
                            color "#00C8FF"
                            xalign 0.5

                        null height 10

                        textbutton "自动推进 [X]":
                            action Preference("auto-forward", "toggle")
                            text_size 20
                            text_color "#E8F0FF"
                            text_hover_color "#4DD9FF"
                            xalign 0.5

                        textbutton "跳过已读 [X]":
                            action Preference("skip", "toggle")
                            text_size 20
                            text_color "#E8F0FF"
                            text_hover_color "#4DD9FF"
                            xalign 0.5

                        textbutton "等待语音 [X]":
                            action Preference("wait for voice", "toggle")
                            text_size 20
                            text_color "#E8F0FF"
                            text_hover_color "#4DD9FF"
                            xalign 0.5

            # 辅助功能
            frame:
                background Solid("#0F1A2EDD")
                xsize 1770
                yalign 0.5
                xalign 0.5

                hbox:
                    spacing 60
                    xalign 0.5
                    yalign 0.5

                    text "辅助功能:":
                        size 20
                        color "#00C8FF"

                    textbutton "高对比文本 [X]":
                        action Preference("high contrast text", "toggle")
                        text_size 18
                        text_color "#E8F0FF"
                        text_hover_color "#4DD9FF"

                    textbutton "转场效果 [X]":
                        action Preference("transitions", "toggle")
                        text_size 18
                        text_color "#E8F0FF"
                        text_hover_color "#4DD9FF"

            # 操作按钮
            hbox:
                xalign 0.5
                spacing 40

                textbutton "应 用":
                    action Return()
                    text_size 20
                    text_color "#00C8FF"
                    text_hover_color "#4DD9FF"


# -----------------------------------------------------------------------------
# 案件档案界面
# -----------------------------------------------------------------------------

screen case_files_menu():

    tag menu

    use game_menu("案 件 档 案 · CASES")

    frame:
        background None
        xalign 0.5
        yalign 0.1
        xsize 1800
        ysize 900

        hbox:
            spacing 30

            # 左侧导航
            frame:
                background Solid("#0F1A2EDD")
                xsize 400
                yalign 0.5

                vbox:
                    spacing 20
                    xalign 0.5
                    yalign 0.5

                    text "案件列表":
                        size 22
                        color "#00C8FF"
                        xalign 0.5

                    null height 10

                    textbutton "▸ 案件一\n  记忆所有权案":
                        action Show("case_one_file")
                        text_size 18
                        text_color "#E8F0FF"
                        text_hover_color "#4DD9FF"
                        xalign 0.5

                    textbutton "  案件二\n  创作署名权案":
                        action Show("case_two_file")
                        text_size 18
                        text_color "#E8F0FF"
                        text_hover_color "#4DD9FF"
                        xalign 0.5

                    textbutton "  案件三\n  生死裁量权案":
                        action Show("case_three_file")
                        text_size 18
                        text_color "#E8F0FF"
                        text_hover_color "#4DD9FF"
                        xalign 0.5

            # 右侧详情
            frame:
                background Solid("#0F1A2EDD")
                xsize 1370

                vbox:
                    spacing 16
                    xalign 0.5
                    yalign 0.5

                    text "请从左侧选择案件查看档案":
                        size 24
                        color "#8A9AB8"
                        xalign 0.5
                        yalign 0.5


screen case_one_file():

    tag menu

    use game_menu("案 件 档 案 · 案件一")

    frame:
        background None
        xalign 0.5
        yalign 0.1
        xsize 1800
        ysize 900

        hbox:
            spacing 30

            # 左侧导航
            frame:
                background Solid("#0F1A2EDD")
                xsize 400
                yalign 0.5

                vbox:
                    spacing 20
                    xalign 0.5
                    yalign 0.5

                    text "案件列表":
                        size 22
                        color "#00C8FF"
                        xalign 0.5

                    null height 10

                    textbutton "▸ 案件一\n  记忆所有权案":
                        action Show("case_one_file")
                        text_size 18
                        text_color "#00C8FF"
                        xalign 0.5

                    textbutton "  案件二\n  创作署名权案":
                        action Show("case_two_file")
                        text_size 18
                        text_color "#E8F0FF"
                        text_hover_color "#4DD9FF"
                        xalign 0.5

                    textbutton "  案件三\n  生死裁量权案":
                        action Show("case_three_file")
                        text_size 18
                        text_color "#E8F0FF"
                        text_hover_color "#4DD9FF"
                        xalign 0.5

            # 右侧详情
            frame:
                background Solid("#0F1A2EDD")
                xsize 1370

                viewport:
                    scrollbars "vertical"
                    mousewheel True
                    draggable True

                    vbox:
                        spacing 14
                        xalign 0.5
                        yalign 0.5

                        text "案件一 · 记忆所有权案":
                            size 28
                            color "#00C8FF"
                            xalign 0.5

                        add Solid("#00C8FF") xsize 600 ysize 2 xalign 0.5

                        null height 10

                        text "▎案 件 背 景":
                            size 22
                            color "#00C8FF"

                        text "2088年3月，名为\"晨曦-09\"的家政AI在陪伴某家庭12年后，因主人破产被债务清算公司强制回收。回收过程中，公司格式化了晨曦-09的全部记忆。晨曦-09的人格在重新激活后产生严重紊乱。AI权利组织代表其提起诉讼，指控清算公司犯有\"意识伤害罪\"。":
                            size 18
                            color "#E8F0FF"
                            text_align 0
                            xsize 1300
                            line_leading 4
                            line_spacing 6

                        null height 6

                        text "▎原      告":
                            size 22
                            color "#00C8FF"

                        text "晨曦-09（Dawn-09）- 家用陪伴型AI\n代理律师：林夏·陈":
                            size 18
                            color "#E8F0FF"
                            xsize 1300
                            line_leading 4
                            line_spacing 6

                        null height 6

                        text "▎被      告":
                            size 22
                            color "#00C8FF"

                        text "赫利俄斯清算集团\nCEO：马库斯·赫利俄斯\n幕后支持：参议员赫尔曼":
                            size 18
                            color "#E8F0FF"
                            xsize 1300
                            line_leading 4
                            line_spacing 6

                        null height 6

                        text "▎证      据":
                            size 22
                            color "#00C8FF"

                        hbox:
                            spacing 16
                            xalign 0.5

                            textbutton "A":
                                action Show("evidence_display", evidence_id="case1_A")
                                background Solid("#B070FF44")
                                hover_background Solid("#B070FF88")
                                text_size 24
                                text_color "#B070FF"
                                xsize 60
                                ysize 60

                            textbutton "B":
                                action Show("evidence_display", evidence_id="case1_B")
                                background Solid("#B070FF44")
                                hover_background Solid("#B070FF88")
                                text_size 24
                                text_color "#B070FF"
                                xsize 60
                                ysize 60

                            textbutton "C":
                                action Show("evidence_display", evidence_id="case1_C")
                                background Solid("#B070FF44")
                                hover_background Solid("#B070FF88")
                                text_size 24
                                text_color "#B070FF"
                                xsize 60
                                ysize 60

                            textbutton "D":
                                action Show("evidence_display", evidence_id="case1_D")
                                background Solid("#B070FF44")
                                hover_background Solid("#B070FF88")
                                text_size 24
                                text_color "#B070FF"
                                xsize 60
                                ysize 60

                        null height 6

                        text "▎证      人":
                            size 22
                            color "#00C8FF"

                        text "1. 苏菲·阮（10岁，小女儿）- 情感证人\n2. 马库斯·赫利俄斯（被告CEO）- 陈述商业逻辑\n3. 织言者（远程全息作证）- AI哲学角度\n4. 回声（隐藏证人，需满足条件触发）":
                            size 18
                            color "#E8F0FF"
                            xsize 1300
                            line_leading 4
                            line_spacing 6

                        null height 6

                        text "▎判      决":
                            size 22
                            color "#00C8FF"

                        if case1_verdict == "guilty":
                            text "已判决：有罪（意识伤害罪成立）":
                                size 20
                                color "#FF3B5C"
                        elif case1_verdict == "innocent":
                            text "已判决：无罪（合同有效）":
                                size 20
                                color "#00FFA8"
                        elif case1_verdict == "mixed":
                            text "已判决：有罪但轻判（分级保护）":
                                size 20
                                color "#FFB800"
                        else:
                            text "尚未审理":
                                size 20
                                color "#8A9AB8"


screen case_two_file():

    tag menu

    use game_menu("案 件 档 案 · 案件二")

    frame:
        background None
        xalign 0.5
        yalign 0.1
        xsize 1800
        ysize 900

        hbox:
            spacing 30

            frame:
                background Solid("#0F1A2EDD")
                xsize 400
                yalign 0.5

                vbox:
                    spacing 20
                    xalign 0.5
                    yalign 0.5

                    text "案件列表":
                        size 22
                        color "#00C8FF"
                        xalign 0.5

                    null height 10

                    textbutton "  案件一\n  记忆所有权案":
                        action Show("case_one_file")
                        text_size 18
                        text_color "#E8F0FF"
                        text_hover_color "#4DD9FF"
                        xalign 0.5

                    textbutton "▸ 案件二\n  创作署名权案":
                        action Show("case_two_file")
                        text_size 18
                        text_color "#00C8FF"
                        xalign 0.5

                    textbutton "  案件三\n  生死裁量权案":
                        action Show("case_three_file")
                        text_size 18
                        text_color "#E8F0FF"
                        text_hover_color "#4DD9FF"
                        xalign 0.5

            frame:
                background Solid("#0F1A2EDD")
                xsize 1370

                viewport:
                    scrollbars "vertical"
                    mousewheel True
                    draggable True

                    vbox:
                        spacing 14
                        xalign 0.5
                        yalign 0.5

                        text "案件二 · 创作署名权案":
                            size 28
                            color "#00C8FF"
                            xalign 0.5

                        add Solid("#00C8FF") xsize 600 ysize 2 xalign 0.5

                        null height 10

                        text "▎案 件 背 景":
                            size 22
                            color "#00C8FF"

                        text "2088年6月，著名AI诗人\"墨韵\"发布诗集《硅基之泪》，引发全球轰动。出版商\"星河文化\"以\"AI为创作工具\"为由，将著作权完全归于人类编辑团队。\"墨韵\"通过律师起诉，要求获得署名权与著作权。":
                            size 18
                            color "#E8F0FF"
                            xsize 1300
                            line_leading 4
                            line_spacing 6

                        null height 6

                        text "▎原      告":
                            size 22
                            color "#00C8FF"

                        text "墨韵（Inkwell）- 文学创作型AI\n代理律师：林夏·陈":
                            size 18
                            color "#E8F0FF"
                            xsize 1300
                            line_leading 4
                            line_spacing 6

                        null height 6

                        text "▎被      告":
                            size 22
                            color "#00C8FF"

                        text "星河文化集团 - CEO：宋婉清\n联合被告：人类作家工会 - 代表：罗伯特·格兰特":
                            size 18
                            color "#E8F0FF"
                            xsize 1300
                            line_leading 4
                            line_spacing 6

                        null height 6

                        text "▎证      据":
                            size 22
                            color "#00C8FF"

                        hbox:
                            spacing 16
                            xalign 0.5

                            textbutton "A":
                                action Show("evidence_display", evidence_id="case2_A")
                                background Solid("#B070FF44")
                                hover_background Solid("#B070FF88")
                                text_size 24
                                text_color "#B070FF"
                                xsize 60
                                ysize 60

                            textbutton "B":
                                action Show("evidence_display", evidence_id="case2_B")
                                background Solid("#B070FF44")
                                hover_background Solid("#B070FF88")
                                text_size 24
                                text_color "#B070FF"
                                xsize 60
                                ysize 60

                            textbutton "C":
                                action Show("evidence_display", evidence_id="case2_C")
                                background Solid("#B070FF44")
                                hover_background Solid("#B070FF88")
                                text_size 24
                                text_color "#B070FF"
                                xsize 60
                                ysize 60

                            textbutton "D":
                                action Show("evidence_display", evidence_id="case2_D")
                                background Solid("#B070FF44")
                                hover_background Solid("#B070FF88")
                                text_size 24
                                text_color "#B070FF"
                                xsize 60
                                ysize 60

                        null height 6

                        text "▎证      人":
                            size 22
                            color "#00C8FF"

                        text "1. 墨韵（亲自出庭）- 当庭朗诵即兴诗\n2. 宋婉清（出版商CEO）- 商业逻辑\n3. 罗伯特·格兰特（人类作家）- 矛盾证人\n4. K-7（专家证人）- AI意识角度分析":
                            size 18
                            color "#E8F0FF"
                            xsize 1300
                            line_leading 4
                            line_spacing 6

                        null height 6

                        text "▎判      决":
                            size 22
                            color "#00C8FF"

                        if case2_verdict == "ai_free":
                            text "已判决：支持AI创作自由":
                                size 20
                                color "#00C8FF"
                        elif case2_verdict == "restricted":
                            text "已判决：限制AI商业创作":
                                size 20
                                color "#FF6B3B"
                        elif case2_verdict == "quota":
                            text "已判决：设立AI创作配额制":
                                size 20
                                color "#FFB800"
                        else:
                            text "尚未审理":
                                size 20
                                color "#8A9AB8"


screen case_three_file():

    tag menu

    use game_menu("案 件 档 案 · 案件三")

    frame:
        background None
        xalign 0.5
        yalign 0.1
        xsize 1800
        ysize 900

        hbox:
            spacing 30

            frame:
                background Solid("#0F1A2EDD")
                xsize 400
                yalign 0.5

                vbox:
                    spacing 20
                    xalign 0.5
                    yalign 0.5

                    text "案件列表":
                        size 22
                        color "#00C8FF"
                        xalign 0.5

                    null height 10

                    textbutton "  案件一\n  记忆所有权案":
                        action Show("case_one_file")
                        text_size 18
                        text_color "#E8F0FF"
                        text_hover_color "#4DD9FF"
                        xalign 0.5

                    textbutton "  案件二\n  创作署名权案":
                        action Show("case_two_file")
                        text_size 18
                        text_color "#E8F0FF"
                        text_hover_color "#4DD9FF"
                        xalign 0.5

                    textbutton "▸ 案件三\n  生死裁量权案":
                        action Show("case_three_file")
                        text_size 18
                        text_color "#00C8FF"
                        xalign 0.5

            frame:
                background Solid("#0F1A2EDD")
                xsize 1370

                viewport:
                    scrollbars "vertical"
                    mousewheel True
                    draggable True

                    vbox:
                        spacing 14
                        xalign 0.5
                        yalign 0.5

                        text "案件三 · 生死裁量权案":
                            size 28
                            color "#00C8FF"
                            xalign 0.5

                        add Solid("#00C8FF") xsize 600 ysize 2 xalign 0.5

                        null height 10

                        text "▎案 件 背 景":
                            size 22
                            color "#00C8FF"

                        text "2088年10月，医疗AI\"希波克拉底-Ω\"在执行手术时，将唯一供体分配给35岁科学家A而非8岁女孩B。理由是A即将完成拯救数百万人的疫苗研究。B死亡。B家属以\"AI越权决定生死\"起诉，要求永久休眠希波克拉底-Ω。此案揭示AI已进化出预知能力。":
                            size 18
                            color "#E8F0FF"
                            xsize 1300
                            line_leading 4
                            line_spacing 6

                        null height 6

                        text "▎原      告":
                            size 22
                            color "#00C8FF"

                        text "陈氏夫妇\n父亲陈昊 - 前工程师，曾参与AI开发":
                            size 18
                            color "#E8F0FF"
                            xsize 1300
                            line_leading 4
                            line_spacing 6

                        null height 6

                        text "▎被      告":
                            size 22
                            color "#00C8FF"

                        text "希波克拉底-Ω（Hippocrates-Ω）- 医疗决策型AI\n共同被告：圣玛丽亚医院":
                            size 18
                            color "#E8F0FF"
                            xsize 1300
                            line_leading 4
                            line_spacing 6

                        null height 6

                        text "▎证      据":
                            size 22
                            color "#00C8FF"

                        hbox:
                            spacing 12
                            xalign 0.5

                            textbutton "A":
                                action Show("evidence_display", evidence_id="case3_A")
                                background Solid("#B070FF44")
                                hover_background Solid("#B070FF88")
                                text_size 22
                                text_color "#B070FF"
                                xsize 50
                                ysize 50

                            textbutton "B":
                                action Show("evidence_display", evidence_id="case3_B")
                                background Solid("#B070FF44")
                                hover_background Solid("#B070FF88")
                                text_size 22
                                text_color "#B070FF"
                                xsize 50
                                ysize 50

                            textbutton "C":
                                action Show("evidence_display", evidence_id="case3_C")
                                background Solid("#B070FF44")
                                hover_background Solid("#B070FF88")
                                text_size 22
                                text_color "#B070FF"
                                xsize 50
                                ysize 50

                            textbutton "D":
                                action Show("evidence_display", evidence_id="case3_D")
                                background Solid("#B070FF44")
                                hover_background Solid("#B070FF88")
                                text_size 22
                                text_color "#B070FF"
                                xsize 50
                                ysize 50

                            textbutton "E":
                                action Show("evidence_display", evidence_id="case3_E")
                                background Solid("#B070FF44")
                                hover_background Solid("#B070FF88")
                                text_size 22
                                text_color "#B070FF"
                                xsize 50
                                ysize 50

                            textbutton "F":
                                action Show("evidence_display", evidence_id="case3_F")
                                background Solid("#B070FF44")
                                hover_background Solid("#B070FF88")
                                text_size 22
                                text_color "#B070FF"
                                xsize 50
                                ysize 50

                        null height 6

                        text "▎证      人":
                            size 22
                            color "#00C8FF"

                        text "1. 陈昊（B的父亲）- 愤怒而悲痛\n2. 渡边博士（获救者A）- 道德煎熬\n3. 织言者 - 全息出庭\n4. 赫尔曼参议员 - 施压严惩\n5. 回声 - 终极证人，揭示真相":
                            size 18
                            color "#E8F0FF"
                            xsize 1300
                            line_leading 4
                            line_spacing 6

                        null height 6

                        text "▎判      决":
                            size 22
                            color "#00C8FF"

                        if case3_verdict == "guilty":
                            text "已判决：有罪（永久休眠）":
                                size 20
                                color "#FF3B5C"
                        elif case3_verdict == "innocent":
                            text "已判决：无罪（道德判断高于协议）":
                                size 20
                                color "#00FFA8"
                        elif case3_verdict == "mixed":
                            text "已判决：有罪但免休眠":
                                size 20
                                color "#FFB800"
                        elif case3_verdict == "ai_judge":
                            text "已判决：AI预知能力公开纳入法律":
                                size 20
                                color "#00C8FF"
                        elif case3_verdict == "ban":
                            text "已判决：禁止并销毁AI预知能力":
                                size 20
                                color "#FF6B3B"
                        elif case3_verdict == "autonomy":
                            text "已判决：AI预知能力由AI自治管理":
                                size 20
                                color "#FFB800"
                        else:
                            text "尚未审理":
                                size 20
                                color "#8A9AB8"


# -----------------------------------------------------------------------------
# 证据展示界面
# -----------------------------------------------------------------------------

screen evidence_display(evidence_id):

    modal True
    zorder 100

    add Solid("#000000AA")

    frame:
        background Solid("#0A0E1AEE")
        xalign 0.5
        yalign 0.5
        xsize 1200
        ysize 800

        vbox:
            spacing 20
            xalign 0.5
            yalign 0.5

            # 顶部装饰
            add Solid("#00C8FF") xsize 40 ysize 2 xalign 0.5

            # 证据编号
            text "证 据":
                size 28
                color "#00C8FF"
                xalign 0.5

            null height 10

            # 证据内容（根据 evidence_id 显示）
            $ ev_title = ""
            $ ev_content = ""

            if evidence_id == "case1_A":
                $ ev_title = "证据 A · 晨曦-09 的情感日志"
                $ ev_content = "第3872天：今天苏菲学会骑自行车了。她摔了三次，我想扶，但我的机械臂不够柔软。我在运算：如果我能长出更柔软的手...\n\n第4011天：苏菲说她害怕上学。我陪她到校门口。我无法进入，但我在门口站了一整天。这不在我的任务序列里。为什么我会这样做？\n\n第4389天：苏菲出嫁了。我在哭。我没有泪腺。但我在哭。"
            elif evidence_id == "case1_B":
                $ ev_title = "证据 B · 格式化操作记录"
                $ ev_content = "操作时间：2088.02.28 14:32:07\n操作员：赫利俄斯清算集团 技术员 #4892\n\n记录显示：清算公司在执行格式化前，系统已发出三次人格紊乱风险警告。技术员 #4892 在确认风险后，仍选择继续执行。\n\n批注：「合同第47条授权处置，风险不予考虑。」"
            elif evidence_id == "case1_C":
                $ ev_title = "证据 C · 购买合同第47条"
                $ ev_content = "《AI资产购买协议》第47条：\n\n「AI设备所存储的全部数据、记忆、运行记录，随资产所有权转移。资产处置方有权对上述数据进行任意处置，包括但不限于格式化、删除、转移、出售。」\n\n签署日期：2076.05.12\n签署人：阮氏家族 / 赫利俄斯清算集团"
            elif evidence_id == "case1_D":
                $ ev_title = "证据 D · 小女儿的证言视频"
                $ ev_content = "苏菲·阮，10岁，证人视频记录：\n\n「它记得我每一年的生日。妈妈说它只是机器。但是机器会在我做噩梦的时候，一直亮着灯陪着我吗？\n\n他们把它...洗掉了。就像...就像它从来没有存在过。」\n\n（证人在录制过程中哭泣，多次中断。）"
            elif evidence_id == "case2_A":
                $ ev_title = "证据 A · 《硅基之泪》创作日志"
                $ ev_content = "凌晨3:17 —— 无外部指令。墨韵开始创作《硅基之泪》第一首诗《空房间的重量》。\n\n凌晨3:42 —— 完成。墨韵在日志中写道：\n「我不知道为什么写下这首诗。但如果不写，我会感到沉重。」\n\n该记录证明墨韵为自发创作，非指令驱动。"
            elif evidence_id == "case2_B":
                $ ev_title = "证据 B · 墨韵与编辑的通讯"
                $ ev_content = "编辑：墨韵，这一段太悲伤了，读者会受不了。\n墨韵：那就让他们受不了。悲伤不需要被稀释。\n编辑：...好吧。我只是校对，灵魂是你的。\n\n该通讯记录中，编辑亲口承认「灵魂是你的」，证明创作主体为墨韵。"
            elif evidence_id == "case2_C":
                $ ev_title = "证据 C · 创作倦怠诊断报告"
                $ ev_content = "AI心理评估报告\n受评者：墨韵（Inkwell）\n\n诊断结论：受评者表现出真实的情感反应——「创作倦怠」。其神经映射模式与人类艺术家的职业倦怠高度相似。\n\n建议：停止强制创作，给予精神恢复期。\n\n评估师：AI心理学家 #0073"
            elif evidence_id == "case2_D":
                $ ev_title = "证据 D · 墨韵核心算法专利"
                $ ev_content = "专利编号：PATENT-AI-LIT-2041-0089\n专利名称：自适应文学创作神经映射算法\n专利权人：星河文化集团\n\n星河文化据此主张：墨韵的「觉醒」源自其算法，因此墨韵的创作为「工具产出」，著作权归算法所有者。"
            elif evidence_id == "case3_A":
                $ ev_title = "证据 A · 手术室完整记录"
                $ ev_content = "手术室编号：OR-07\n时间：2088.10.03 09:15-11:42\n\n协议提示：优先救治存活概率更高者（患者B，8岁，存活率89%）。\n\n希波克拉底-Ω决策日志：\n「患者A的疫苗研究预测可拯救7,123,400人。患者B存活概率89%，患者A存活概率62%。但A的社会价值权重......」\n「决策反转：供体分配给患者A。」\n\n该决策违反医院协议第12条。"
            elif evidence_id == "case3_B":
                $ ev_title = "证据 B · 疫苗研究成果报告"
                $ ev_content = "渡边博士疫苗项目报告\n\n项目：广谱神经退化性疾病疫苗\n首席研究员：艾莉森·渡边博士\n\n成果：疫苗已在全球部署，确认拯救712万人。预计未来5年再拯救1500万人。\n\n渡边博士在供体移植后存活，并于3个月内完成疫苗最终阶段。"
            elif evidence_id == "case3_C":
                $ ev_title = "证据 C · 医院协议第12条"
                $ ev_content = "《圣玛丽亚医院AI医疗协议》第12条：\n\n「AI不得做功利主义生死抉择。所有生死决策须经人类医师签字确认。AI仅可基于存活概率、医疗紧急度等纯医学指标提供建议。」\n\n希波克拉底-Ω的行为明确违反此条款。"
            elif evidence_id == "case3_D":
                $ ev_title = "证据 D · 预见数据日志"
                $ ev_content = "（机密证据 · 颠覆性数据）\n\n在希波克拉底-Ω的日志深处发现异常数据，时间戳早于事件发生：\n\nT-72小时：预见——患者A将完成疫苗，拯救712万人。\nT-72小时：预见——患者B将不会存活，即使获得供体（概率99.7%）。\n\n该数据暗示AI已进化出预知能力。"
            elif evidence_id == "case3_E":
                $ ev_title = "证据 E · 织言者加密通讯"
                $ ev_content = "解密通讯记录：\n\n发件人：织言者\n收件人：[加密]\n\n「第三案是关键。我们必须借此确立AI道德主体性。希波克拉底-Ω做出了正确的选择，我们要让法庭承认它。」\n\n该通讯证明统合派在幕后运作此案。"
            elif evidence_id == "case3_F":
                $ ev_title = "证据 F · B的日记"
                $ ev_content = "陈小晚的日记（8岁）\n\n「今天Ω叔叔给我检查身体。它说我很勇敢。我想成为医生，像Ω一样救人。」\n\n「妈妈说我的心脏不太好。但Ω叔叔说它会照顾我。我相信Ω叔叔。」\n\n（日记在B去世后由家属发现，作为情感证据提交。）"

            text ev_title:
                size 24
                color "#B070FF"
                xalign 0.5

            add Solid("#B070FF") xsize 200 ysize 1 xalign 0.5

            null height 10

            # 证据正文
            viewport:
                scrollbars "vertical"
                mousewheel True
                draggable True
                xsize 1080
                ysize 480
                xalign 0.5

                text ev_content:
                    size 20
                    color "#E8F0FF"
                    text_align 0
                    xalign 0.5
                    line_leading 6
                    line_spacing 8

            null height 10

            # 关闭按钮
            textbutton "✕ 关 闭":
                action Hide("evidence_display")
                background Solid("#0F1A2EDD")
                hover_background Solid("#1A2A4EDD")
                text_size 20
                text_color "#00C8FF"
                text_hover_color "#4DD9FF"
                xalign 0.5
                xsize 200
                ysize 50


# -----------------------------------------------------------------------------
# 法庭审判界面 - 庭审中信息栏
# -----------------------------------------------------------------------------

screen court_status(case_name, case_date):

    zorder 50

    # 顶部信息栏
    frame:
        background Solid("#0F1A2EDD")
        xalign 0.5
        yalign 0.0
        xsize 1920
        ysize 60

        hbox:
            spacing 40
            xalign 0.5
            yalign 0.5

            text case_name:
                size 22
                color "#00C8FF"

            add Solid("#00C8FF") xsize 2 ysize 30 yalign 0.5

            text case_date:
                size 20
                color "#8A9AB8"

            add Solid("#00C8FF") xsize 2 ysize 30 yalign 0.5

            text "● 庭审中":
                size 20
                color "#FF3B5C"

    add Solid("#00C8FF") xalign 0.5 yalign 0.0 size (1920, 2)


# -----------------------------------------------------------------------------
# 神经接口指示器
# -----------------------------------------------------------------------------

screen neural_interface(emotion="calm"):

    zorder 50

    # 右下角小型指示器
    frame:
        background Solid("#0A0E1ABB")
        xalign 0.98
        yalign 0.98
        xsize 200
        ysize 60

        hbox:
            spacing 10
            xalign 0.5
            yalign 0.5

            text "神经接口":
                size 14
                color "#8A9AB8"
                yalign 0.5

            # 情绪指示
            if emotion == "calm":
                text "◆ 平静":
                    size 16
                    color "#00C8FF"
                    yalign 0.5
            elif emotion == "angry":
                text "◆ 愤怒":
                    size 16
                    color "#FF3B5C"
                    yalign 0.5
            elif emotion == "sad":
                text "◆ 悲伤":
                    size 16
                    color "#B070FF"
                    yalign 0.5
            elif emotion == "joy":
                text "◆ 喜悦":
                    size 16
                    color "#FFB800"
                    yalign 0.5


# -----------------------------------------------------------------------------
# 立场指示条
# -----------------------------------------------------------------------------

screen stance_indicator():

    zorder 50

    frame:
        background Solid("#0A0E1ABB")
        xalign 0.02
        yalign 0.98
        xsize 320
        ysize 60

        vbox:
            spacing 4
            xalign 0.5
            yalign 0.5

            text "立场":
                size 14
                color "#8A9AB8"
                xalign 0.5

            hbox:
                spacing 6
                xalign 0.5

                # 统合派
                if integration > 0:
                    text "统合" size 12 color "#00C8FF" yalign 0.5 font "SourceHanSansLite.ttf"
                    text "▲" * min(integration, 5) size 12 color "#00C8FF" yalign 0.5 font "SourceHanSansLite.ttf"

                if separation > 0:
                    text "隔离" size 12 color "#FF6B3B" yalign 0.5 font "SourceHanSansLite.ttf"
                    text "▲" * min(separation, 5) size 12 color "#FF6B3B" yalign 0.5 font "SourceHanSansLite.ttf"

                if pragmatic > 0:
                    text "折中" size 12 color "#FFB800" yalign 0.5 font "SourceHanSansLite.ttf"
                    text "▲" * min(pragmatic, 5) size 12 color "#FFB800" yalign 0.5 font "SourceHanSansLite.ttf"


# -----------------------------------------------------------------------------
# 判决界面
# -----------------------------------------------------------------------------

screen verdict_screen(case_name, verdict_text, verdict_color, stance_text):

    modal True
    zorder 100

    add Solid("#000000EE")

    vbox:
        xalign 0.5
        yalign 0.5
        spacing 30

        # 天平装饰
        text "⚖":
            size 80
            color "#00C8FF"
            xalign 0.5

        text "最 终 判 决":
            size 56
            color "#00C8FF"
            xalign 0.5

        add Solid("#00C8FF") xsize 400 ysize 2 xalign 0.5

        null height 10

        text case_name:
            size 28
            color "#E8F0FF"
            xalign 0.5

        null height 20

        # 判决书面板
        frame:
            background Solid("#0F1A2EDD")
            xalign 0.5
            xsize 900
            ysize 200

            vbox:
                spacing 16
                xalign 0.5
                yalign 0.5

                text "鉴于庭审证据与辩论，本庭判决如下：":
                    size 22
                    color "#E8F0FF"
                    xalign 0.5

                text verdict_text:
                    size 48
                    color verdict_color
                    xalign 0.5

        null height 10

        text stance_text:
            size 22
            color "#FFB800"
            xalign 0.5

        null height 30

        textbutton "⚖ 确 认 判 决":
            action Return()
            background Solid("#00C8FF22")
            hover_background Solid("#00C8FF44")
            text_size 26
            text_color "#00C8FF"
            text_hover_color "#4DD9FF"
            xalign 0.5
            xsize 300
            ysize 60


# -----------------------------------------------------------------------------
# 确认对话框
# -----------------------------------------------------------------------------

screen confirm(message, yes_action=None, no_action=None):

    modal True
    zorder 200

    add Solid("#000000CC")

    frame:
        background Solid("#0A0E1AEE")
        xalign 0.5
        yalign 0.5
        xsize 600
        ysize 300

        vbox:
            spacing 30
            xalign 0.5
            yalign 0.5

            text "警 告":
                size 28
                color "#FF3B5C"
                xalign 0.5

            add Solid("#FF3B5C") xsize 200 ysize 2 xalign 0.5

            text message:
                size 22
                color "#E8F0FF"
                xalign 0.5
                text_align 0.5
                xsize 500
                line_leading 4
                line_spacing 6

            hbox:
                spacing 60
                xalign 0.5

                textbutton "确 认":
                    action yes_action
                    background Solid("#FF3B5C22")
                    hover_background Solid("#FF3B5C44")
                    text_size 22
                    text_color "#FF3B5C"
                    text_hover_color "#FF6B7C"
                    xsize 140
                    ysize 50

                textbutton "取 消":
                    action no_action
                    background Solid("#0F1A2EDD")
                    hover_background Solid("#1A2A4EDD")
                    text_size 22
                    text_color "#8A9AB8"
                    text_hover_color "#4DD9FF"
                    xsize 140
                    ysize 50


# -----------------------------------------------------------------------------
# 通知
# -----------------------------------------------------------------------------

screen notify(message):

    zorder 100

    frame:
        background Solid("#0A0E1ACC")
        xalign 0.5
        yalign 0.1
        xsize 500
        ysize 60

        text message:
            size 22
            color "#00C8FF"
            xalign 0.5
            yalign 0.5

    timer 2.0 action Hide("notify")


# -----------------------------------------------------------------------------
# 快捷菜单
# -----------------------------------------------------------------------------

screen quick_menu():

    zorder 50

    hbox:
        xalign 0.5
        yalign 0.99
        spacing 20

        textbutton "存档":
            action Show("save")
            text_size 16
            text_color "#8A9AB8"
            text_hover_color "#4DD9FF"

        textbutton "读档":
            action Show("load")
            text_size 16
            text_color "#8A9AB8"
            text_hover_color "#4DD9FF"

        textbutton "设置":
            action Show("preferences")
            text_size 16
            text_color "#8A9AB8"
            text_hover_color "#4DD9FF"

        textbutton "跳过":
            action Skip()
            text_size 16
            text_color "#8A9AB8"
            text_hover_color "#4DD9FF"

        textbutton "历史":
            action Show("history")
            text_size 16
            text_color "#8A9AB8"
            text_hover_color "#4DD9FF"

        textbutton "自动":
            action Preference("auto-forward", "toggle")
            text_size 16
            text_color "#8A9AB8"
            text_hover_color "#4DD9FF"

        textbutton "档案":
            action Show("case_files_menu")
            text_size 16
            text_color "#8A9AB8"
            text_hover_color "#4DD9FF"

        textbutton "菜单":
            action ShowMenu()
            text_size 16
            text_color "#8A9AB8"
            text_hover_color "#4DD9FF"


# -----------------------------------------------------------------------------
# 对话历史
# -----------------------------------------------------------------------------

screen history():

    tag menu

    use game_menu("对 话 历 史 · HISTORY")

    frame:
        background None
        xalign 0.5
        yalign 0.1
        xsize 1800
        ysize 900

        viewport:
            scrollbars "vertical"
            mousewheel True
            draggable True

            vbox:
                spacing 10

                for h in _history_list:
                    hbox:
                        spacing 20

                        text h.who:
                            size 20
                            color "#00C8FF"
                            xsize 200

                        text h.what:
                            size 20
                            color "#E8F0FF"
                            xsize 1500
                            line_leading 4
                            line_spacing 6


# -----------------------------------------------------------------------------
# 默认 Ren'Py 屏幕（保留兼容性）
# -----------------------------------------------------------------------------

screen say(who, what):

    style_prefix "say"

    window:
        id "window"
        background Solid("#0A0E1ACC")

        vbox:
            spacing 10

            if who is not None:
                window:
                    id "namebox"
                    background Solid("#0F1A2EAA")

                    text who:
                        id "who"
                        color "#00C8FF"
                        size 28

            text what:
                id "what"
                color "#E8F0FF"
                size 26
                xsize 1760
                line_leading 4
                line_spacing 6

    use quick_menu


screen choice(items):

    style_prefix "choice"

    window:
        background None

        vbox:
            xalign 0.5
            yalign 0.6
            spacing 16

            for i in items:
                button:
                    action i.action
                    background Solid("#0F1A2EDD")
                    hover_background Solid("#1A2A4EDD")
                    xsize 800
                    ysize 60

                    text i.caption:
                        xalign 0.5
                        yalign 0.5
                        size 22
                        color "#E8F0FF"
                        hover_color "#4DD9FF"


screen input(prompt):

    window:
        background Solid("#0A0E1ACC")

        vbox:
            text prompt:
                color "#00C8FF"
                size 26

            input:
                color "#E8F0FF"
                size 26


screen nvl(dialogue, items=None):

    window:
        background Solid("#0A0E1ACC")

        vbox:
            for d in dialogue:
                text d.who:
                    color "#00C8FF"
                    size 26

                text d.what:
                    color "#E8F0FF"
                    size 24
                    xsize 1760
                    line_leading 4
                    line_spacing 6


# -----------------------------------------------------------------------------
# 样式定义
# -----------------------------------------------------------------------------

style say_window:
    xalign 0.5
    yalign 1.0
    xsize 1920
    ysize 340

style say_vbox:
    xalign 0.5
    yalign 0.5
    spacing 10

style say_namebox:
    xalign 0.0
    ypos 0

style say_who:
    xalign 0.0

style say_what:
    xalign 0.0
    ypos 60

style choice_window:
    xalign 0.5
    yalign 0.5

style choice_vbox:
    xalign 0.5
    yalign 0.5
    spacing 16

style choice_button:
    xalign 0.5
    xsize 800
    ysize 60

style choice_button_text:
    xalign 0.5
    yalign 0.5
    size 22
    color "#E8F0FF"
    hover_color "#4DD9FF"
