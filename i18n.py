"""Runtime i18n for VueOSD — English / Simplified Chinese.

All UI strings are keyed by their original English text.  ``tr()`` returns the
active translation at widget creation time; ``apply_language()`` re-translates
already visible widgets/actions in place when the user switches language.
"""
import json
from pathlib import Path

_LANG_FILE = Path(__file__).with_name('language.json')
_CURRENT = 'en'

ZH = {
    '  Layout locked': '  布局已锁定',
    '  Map hidden': '  地图已隐藏',
    '  Render Video': '  渲染视频',
    '(no label)': '（无标签）',
    '+  Add Font': '+  添加字体',
    '0 regions': '0 个区域',
    '0:00 / 0:00': '0:00 / 0:00',
    'Adjust per-channel gain (1.0 = neutral)': '调整各通道增益（1.0 = 原始值）',
    'Analog dial': '模拟表盘',
    'Ask again next launch.': '下次启动时再次询问。',
    'Aspect ratio:': '宽高比：',
    'Cached: scaled-down preview frames, snappy seeking.\nOriginal: native source resolution — pixel-accurate but\nnoticeably slower to scrub on large videos.': '缓存模式：使用缩小后的预览帧，拖动进度流畅。\n原始模式：使用源视频原生分辨率——像素级精确，但\n在大视频上拖动会明显变慢。',
    'Cancel': '取消',
    'Choose output location.': '选择输出位置。',
    'Chroma key export (magenta)': '色键导出（洋红）',
    'Circular gauge': '圆形仪表',
    'Clear': '清除',
    'Click a swatch or type a hex value  •  Changes preview live': '点击色块或输入十六进制色值  •  预览实时更新',
    'Close': '关闭',
    'Codec:': '编码器：',
    'Color Correction': '色彩校正',
    'Copy this report and share it so the firmware symbol table can be corrected:': '复制此报告并分享，以便修正固件符号表：',
    'Copy to clipboard': '复制到剪贴板',
    'Custom': '自定义',
    'Custom Widgets': '自定义组件',
    'Detected BetaFPV P1 — extracting embedded OSD…': '检测到 BetaFPV P1——正在提取内嵌 OSD…',
    'Detecting…': '检测中…',
    'Digital FPV OSD Tool': '数字 FPV OSD 工具',
    'Digital readout': '数字读数',
    "Don't ask about this version again.": '此版本不再询问。',
    'Done!': '完成！',
    'Dot': '圆点',
    'Downloading fonts': '正在下载字体',
    'Drag on the preview to blank OSD cells. Regions follow the OSD when you change scale or offset.': '在预览上拖动可将 OSD 单元格设为空白。改变缩放或偏移时，遮罩区域会随 OSD 一起移动。',
    'Drag to set output bitrate (logarithmic scale, 1–100 Mbit/s).\nUse the arrows on the right for ±1 Mbit/s fine steps.\nAuto-set to source average bitrate on video load.': '拖动可设置输出码率（对数刻度，1–100 Mbit/s）。\n使用右侧箭头以 ±1 Mbit/s 微调。\n加载视频时自动设为源视频的平均码率。',
    'Draw a map under the GPS track. Downloads map tiles on first use (cached for offline reuse); falls back to a plain background when offline.': '在 GPS 轨迹下方绘制地图。首次使用时会下载地图瓦片（缓存后可离线使用）；离线时回退为纯色背景。',
    'Drop  .mp4 · .ts · .osd · .srt  here': '将 .mp4 · .ts · .osd · .srt 文件拖到此处',
    'Enable color correction': '启用色彩校正',
    'Enable region masking': '启用区域遮罩',
    'Error': '错误',
    'Export only the OSD glyphs and SRT bar onto a solid magenta\nbackground as a standard H.264 .mp4. Pull the magenta key in\nDaVinci Resolve, Premiere Pro, or Final Cut Pro to layer the\nOSD onto GoPro/action-cam footage.\n\nMagenta is used because no FPV OSD glyphs ever contain it,\nso the keyer can\'t eat any OSD content.': '仅将 OSD 字符和 SRT 信息栏导出为纯洋红背景的\n标准 H.264 .mp4。在 DaVinci Resolve、Premiere Pro 或\nFinal Cut Pro 中抠除洋红色，即可将 OSD 叠加到\nGoPro / 运动相机画面上。\n\n选择洋红是因为 FPV OSD 字符中不会使用它，\n因此抠像不会误伤任何 OSD 内容。',
    'FFmpeg Missing': '缺少 FFmpeg',
    'FFmpeg install failed': 'FFmpeg 安装失败',
    'FFmpeg installed — restart app to detect it': 'FFmpeg 已安装——请重启程序以检测',
    'Installing FFmpeg via winget…': '正在通过 winget 安装 FFmpeg…',
    "FFmpeg not found.\n\nRun 'VueOSD.bat' to install it automatically,\nor install manually from https://www.gyan.dev/ffmpeg/builds/": '未找到 FFmpeg。\n\n运行 “VueOSD.bat” 自动安装，\n或从 https://www.gyan.dev/ffmpeg/builds/ 手动安装。',
    "Fetch the bundled font pack (BTFL / INAV / ArduPilot) from the project's GitHub releases and install it into the fonts/ folder.": '从项目的 GitHub Releases 获取内置字体包（BTFL / INAV / ArduPilot），并安装到 fonts/ 目录。',
    'File Already Exists': '文件已存在',
    'Fine-tune Position & Scale': '微调位置与缩放',
    'Files': '文件',
    'Font download failed': '字体下载失败',
    'Fonts installed': '字体已安装',
    'OSD Font': 'OSD 字体',
    'Go to end (End)': '跳到结尾（End）',
    'Go to start (Home)': '跳到开头（Home）',
    'HD tiles': '高清字体',
    'Hide OSD Regions': '隐藏 OSD 区域',
    'Hide the MSP OSD glyph grid. Widgets and the SRT bar are unaffected.': '隐藏 MSP OSD 字符网格。自定义组件和 SRT 信息栏不受影响。',
    'Icons by <a href="https://www.flaticon.com/free-icons/wifi-connection" style="color:#2a2a3a;text-decoration:none;">Smashicons – Flaticon</a>  &middot;  Color correction based on <a href="https://github.com/sickgreg/VfxEnc" style="color:#2a2a3a;text-decoration:none;">VfxEnc</a> by sickgreg': '图标来自 <a href="https://www.flaticon.com/free-icons/wifi-connection" style="color:#2a2a3a;text-decoration:none;">Smashicons – Flaticon</a>  &middot;  色彩校正基于 sickgreg 的 <a href="https://github.com/sickgreg/VfxEnc" style="color:#2a2a3a;text-decoration:none;">VfxEnc</a>',
    'In: 0:00': '入点：0:00',
    'Install FFmpeg': '安装 FFmpeg',
    'Install FFmpeg with your package manager:\n\n  Ubuntu/Debian:  sudo apt install ffmpeg\n  Fedora:         sudo dnf install ffmpeg\n  Arch:           sudo pacman -S ffmpeg\n  macOS:          brew install ffmpeg\n\nThen restart the app.': '使用包管理器安装 FFmpeg：\n\n  Ubuntu/Debian:  sudo apt install ffmpeg\n  Fedora:         sudo dnf install ffmpeg\n  Arch:           sudo pacman -S ffmpeg\n  macOS:          brew install ffmpeg\n\n然后重启本程序。',
    'Install Failed': '安装失败',
    'Linear bar': '线性条',
    'Link Status Bar': '链路状态栏',
    'Load an .osd file first — the diagnostic reads the current OSD frame.': '请先加载 .osd 文件——诊断功能会读取当前 OSD 帧。',
    'Loading OSD parser…': '正在加载 OSD 解析器…',
    'Loading font engine…': '正在加载字体引擎…',
    'Loading video pipeline…': '正在加载视频管线…',
    'GPS Map': 'GPS 地图',
    'Building interface…': '正在构建界面…',
    'Checking FFmpeg…': '正在检查 FFmpeg…',
    'Mbit/s:': '兆位/秒：',
    'Missing': '缺失',
    'No GPU encoder found': '未找到 GPU 编码器',
    'No GPU encoder found (NVENC/AMF/QSV/VAAPI)': '未找到 GPU 编码器（NVENC/AMF/QSV/VAAPI）',
    'No OSD frame at the current playhead. Scrub to a moment where the OSD is visible and try again.': '当前播放位置没有 OSD 帧。请拖动到能看到 OSD 的时刻再试。',
    'No file selected': '未选择文件',
    'No font loaded': '未加载字体',
    'None (track only)': '无（仅显示轨迹）',
    'Opacity': '不透明度',
    'OSD auto-fitted to video height, centred.': 'OSD 已按视频高度自动适配并居中。',
    'OSD diagnostic': 'OSD 诊断',
    'OSD glyph diagnostic': 'OSD 字符诊断',
    'OSD offset:': 'OSD 偏移：',
    'Open theme colour editor': '打开主题颜色编辑器',
    'Out: —': '出点：—',
    'Output & Encoding': '输出与编码',
    'Overwrite': '覆盖',
    'Pad the video into a wider or taller canvas with black bars.\nUse this to put a 4:3 source into a 16:9 frame and place OSD\nelements inside the side bars (drag them out with the X offset).': '用黑边将视频填充到更宽或更高的画布。\n可用于把 4:3 源视频放入 16:9 画面，并将 OSD\n元素放在两侧黑边内（用 X 偏移拖出）。',
    'Plane': '飞机',
    'Play / Pause (Space)': '播放 / 暂停（空格）',
    'Preset:': '预设：',
    'Preview': '预览',
    'P1 OSD: no frames found': 'P1 OSD：未找到帧',
    'Quadcopter': '四轴飞行器',
    'R / G / B:  1.00 / 1.00 / 1.00': 'R / G / B：1.00 / 1.00 / 1.00',
    'RGB Multipliers': 'RGB 倍率',
    'Red': '红',
    'Green': '绿',
    'Blue': '蓝',
    "Radio signal, bitrate, GPS, altitude from .srt.\n'No MAVLink telemetry' lines are hidden.": '从 .srt 读取信号、码率、GPS、高度。\n“No MAVLink telemetry” 行会被隐藏。',
    'Ready': '就绪',
    'Reading video info…': '正在读取视频信息…',
    'Refresh Preview': '刷新预览',
    'Release notes:': '版本说明：',
    'Remind me later': '稍后提醒',
    'Reset': '重置',
    'Reset (1.0)': '重置（1.0）',
    'Reset OSD offset to 0': '将 OSD 偏移重置为 0',
    'Reset all color correction to defaults': '将所有色彩校正恢复为默认值',
    'Reset trim to full video': '将裁剪区间重置为完整视频',
    'Ring gauge': '环形仪表',
    'Satellite (Esri)': '卫星图（Esri）',
    'Save as:': '另存为：',
    'Save as:  ⚠ that file also exists — pick a different name': '另存为：⚠ 该文件已存在——请选择其他名称',
    'Save with this name': '使用此名称保存',
    'Save…': '保存…',
    'Scale': '缩放',
    'Scale the output video to a higher resolution using Lanczos.\nUseful when source is 1080p and you want a sharper result on a high-res display.': '使用 Lanczos 算法将输出视频放大到更高分辨率。\n适用于源视频为 1080p、希望在高清屏幕上获得更清晰效果的场景。',
    'Scan the current OSD frame for digit runs and report the icon glyph IDs adjacent to them. Use this when an OSD-sourced widget shows nothing.': '扫描当前 OSD 帧中的数字串，并报告其旁边的图标字符 ID。当某个基于 OSD 的组件无内容显示时可使用此功能。',
    'Select a video file.': '请选择视频文件。',
    'Semicircle gauge': '半圆仪表',
    "Shape drawn at the craft's current position. Plane rotates to match heading.": '在飞行器当前位置绘制的图形。飞机图标会随航向旋转。',
    'Shift OSD timestamps relative to video.\n+500 ms → OSD shows data 500 ms later (compensates OSD lagging behind).\n−500 ms → OSD shows data 500 ms earlier.\nOnboard video + ground-recorded .osd/.srt: set this to how long the\nground recording had been running when the onboard recording started\n(often tens of seconds).': '相对视频平移 OSD 时间戳。\n+500 毫秒 → OSD 数据延后 500 毫秒显示（补偿 OSD 滞后）。\n−500 毫秒 → OSD 数据提前 500 毫秒显示。\n机载视频 + 地面录制的 .osd/.srt：请将此值设为机载录制开始时\n地面录制已运行的时长（通常为数十秒）。',
    'Show OSD glyphs': '显示 OSD 字符',
    'Show link status bar': '显示链路状态栏',
    'Size': '尺寸',
    'Show or hide the GPS map overlay on the video.': '显示或隐藏视频上的 GPS 地图叠加层。',
    'Starting…': '正在启动…',
    'Step back 1 frame (←)': '后退一帧（←）',
    'Step forward 1 frame (→)': '前进一帧（→）',
    'Stop render': '停止渲染',
    'Street map (OSM)': '街道地图（OSM）',
    'Style:': '样式：',
    'Theme Editor': '主题编辑器',
    'Theme Editor — VueOSD': '主题编辑器 — VueOSD',
    'This will install FFmpeg via winget.\nContinue?': '这将通过 winget 安装 FFmpeg。\n是否继续？',
    'Tick dial': '刻度表盘',
    'Tiles download on first use and are cached offline; the map auto-zooms to the path. Reposition it with “Layout locked/unlocked” in Custom Widgets.': '地图瓦片在首次使用时下载并缓存以供离线使用；地图会自动缩放到轨迹。可在“自定义组件”中通过“布局锁定/解锁”调整位置。',
    'Toggle light / dark theme': '切换浅色 / 深色主题',
    'UI scale': '界面缩放',
    'Unlock the layout to drag and resize widgets — including the GPS map — directly on the video preview. Click again to lock.': '解锁布局后，可直接在视频预览上拖动并调整组件大小（包括 GPS 地图）。再次点击可锁定。',
    'X offset': 'X 偏移',
    'Y offset': 'Y 偏移',
    'Update failed': '更新失败',
    'Update installed': '更新已安装',
    'Update now': '立即更新',
    'Updating VueOSD': '正在更新 VueOSD',
    'Upscale output:': '输出放大：',
    'Visible fields:': '可见字段：',
    'Visual alpha-beta smoothing for bars and gauges. 0% disables smoothing completely; values above 300% can be typed for testing.': '进度条和仪表的视觉 alpha-beta 平滑。0% 完全关闭平滑；可手动输入高于 300% 的值进行测试。',
    'VueOSD': 'VueOSD',
    'VueOSD update available': 'VueOSD 有新版本',
    'Widgets read live telemetry from the SRT track. Toggle edit mode then drag on the preview to reposition.': '组件从 SRT 轨道读取实时遥测数据。切换编辑模式后，可在预览上拖动以重新定位。',
    'Your FFmpeg lacks libplacebo — GLSL shader will be skipped.\nBuilt-in LUT correction still works.': '你的 FFmpeg 未编译 libplacebo——将跳过 GLSL 着色器。\n内置 LUT 校正仍然可用。',
    'analog': '模拟',
    'bar': '条形',
    'digital': '数字',
    'dot': '圆点',
    'gauge': '仪表',
    'none': '无',
    'plane': '飞机',
    'quadcopter': '四轴',
    'ring': '环形',
    'satellite': '卫星',
    'semicircle': '半圆',
    'street': '街道',
    't = 0.0s  |  OSD —': 't = 0.0秒  |  OSD —',
    'tickdial': '刻度表盘',
    '…': '…',
    '↓  Download fonts from GitHub': '↓  从 GitHub 下载字体',
    '↺': '↺',
    '↺  Reset': '↺  重置',
    '↺  Reset to defaults': '↺  恢复默认',
    '− Remove': '− 移除',
    '⚠ FFmpeg not found': '⚠ 未找到 FFmpeg',
    '⚠ No OSD elements in trim window — rendering without OSD overlay': '⚠ 裁剪区间内没有 OSD 元素——将以无 OSD 叠加方式渲染',
    '⚠ This install is a git working copy. Updating will overwrite tracked files, which will show up in <code>git status</code>. Commit or stash first if that matters.': '⚠ 当前安装是 git 工作副本。更新会覆盖已跟踪文件，这些更改会显示在 <code>git status</code> 中。如有需要，请先提交或暂存。',
    '⚡ GPU': '⚡ GPU',
    '✓  Apply & Save': '✓  应用并保存',
    '✓ FFmpeg found': '✓ 已找到 FFmpeg',
    '✓ FFmpeg installed successfully': '✓ FFmpeg 安装成功',
    '⏹ Stopped': '⏹ 已停止',
    '✕': '✕',
    '＋ Add': '＋ 添加',
    '🎨': '🎨',
    '🔍  Diagnose OSD glyphs': '🔍  诊断 OSD 字符',
}


def get_language() -> str:
    return _CURRENT


def toggle_label() -> str:
    """Short label for the language button — shows the language to switch TO."""
    return '中' if _CURRENT == 'en' else 'EN'


def load_language() -> str:
    global _CURRENT
    try:
        data = json.loads(_LANG_FILE.read_text(encoding='utf-8'))
        _CURRENT = 'en' if data.get('language') == 'en' else 'zh'
    except Exception:
        _CURRENT = 'zh'
    return _CURRENT


def set_language(lang: str) -> None:
    global _CURRENT
    _CURRENT = 'zh' if lang == 'zh' else 'en'
    try:
        _LANG_FILE.write_text(
            json.dumps({'language': _CURRENT}, ensure_ascii=False),
            encoding='utf-8')
    except OSError:
        pass


def tr(text: str) -> str:
    """Translate *text* into the active language (unknown text is unchanged)."""
    if _CURRENT == 'zh':
        return ZH.get(text, text)
    return text


def apply_language() -> None:
    """Re-translate every visible widget/action after a language switch.

    Translation is keyed by the currently displayed text: English keys map to
    Chinese values and vice versa, so this works in both directions without
    instrumenting individual widgets.
    """
    try:
        from PyQt6.QtWidgets import QApplication
        from PyQt6.QtGui import QAction
    except ImportError:
        return

    reverse = {v: k for k, v in ZH.items()}

    def conv(text):
        if not isinstance(text, str) or not text:
            return text
        if _CURRENT == 'zh':
            return ZH.get(text, text)
        return reverse.get(text, text)

    def retext(obj, getter, setter):
        try:
            cur = getattr(obj, getter)()
            new = conv(cur)
            if new != cur:
                getattr(obj, setter)(new)
        except Exception:
            pass

    for widget in QApplication.allWidgets():
        retext(widget, 'windowTitle', 'setWindowTitle')
        retext(widget, 'text', 'setText')
        retext(widget, 'title', 'setTitle')
        retext(widget, 'toolTip', 'setToolTip')
        if hasattr(widget, 'titleText'):          # CollapsibleGroupBox
            try:
                cur = widget.titleText()
                new = conv(cur)
                if new != cur:
                    widget.setTitle(new)
            except Exception:
                pass
        retext(widget, 'statusTip', 'setStatusTip')
        retext(widget, 'placeholderText', 'setPlaceholderText')

        try:
            count = widget.count()
        except Exception:
            count = 0
        if count:
            if hasattr(widget, 'tabText') and hasattr(widget, 'setTabText'):
                for i in range(count):
                    cur = widget.tabText(i)
                    new = conv(cur)
                    if new != cur:
                        widget.setTabText(i, new)
            elif hasattr(widget, 'itemText') and hasattr(widget, 'setItemText'):
                for i in range(count):
                    cur = widget.itemText(i)
                    new = conv(cur)
                    if new != cur:
                        widget.setItemText(i, new)

        if hasattr(widget, 'horizontalHeaderItem'):
            try:
                for i in range(widget.columnCount()):
                    item = widget.horizontalHeaderItem(i)
                    if item is not None:
                        cur = item.text()
                        new = conv(cur)
                        if new != cur:
                            item.setText(new)
            except Exception:
                pass

        try:
            for action in widget.findChildren(QAction):
                retext(action, 'text', 'setText')
                retext(action, 'toolTip', 'setToolTip')
        except Exception:
            pass
