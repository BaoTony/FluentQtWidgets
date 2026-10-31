# FluentQtWidgets 编译环境报告

> 生成日期：2026-10-31 | 分支：`build` / `dev`

---

## 1. 编译状态

| 项目 | 数值 |
|------|------|
| 编译目标总数 | **593 / 593** |
| 退出码 | `0`（成功） |
| 主库源文件 | 62 个 `.cpp` 文件 |
| 示例程序 | **53** 个 demo exe |
| 测试程序 | **19** 个 test exe |

---

## 2. 构建产物位置

```
d:\dev\store\txp666\FluentQtWidgets\out\msvc\
```

| 目录 | 大小 | 文件数 | 说明 |
|------|------|--------|------|
| `examples/` | ~7,224 MB | 2,771 | 53 个示例程序 + Qt 运行库 |
| `tests/` | ~566 MB | 405 | 19 个测试程序 + Qt 运行库 |
| `CMakeFiles/` | ~81 MB | 97 | CMake 构建中间文件 |
| `FluentQtWidgets_autogen/` | ~8 MB | 128 | MOC 自动生成代码 |
| **总计** | **~7.96 GB** | **3,416** | |

核心库 `FluentQtWidgets.dll` 部署在每个 exe 同级目录下。

---

## 3. 示例程序清单（53 个）

### basic_input（7 个）
```
button          → fqw_basic_input_button_demo.exe
check_box       → fqw_basic_input_check_box_demo.exe
combo_box       → fqw_basic_input_combo_box_demo.exe
model_combo_box → fqw_basic_input_model_combo_box_demo.exe
radio_button    → fqw_basic_input_radio_button_demo.exe
slider          → fqw_basic_input_slider_demo.exe
switch_button   → fqw_basic_input_switch_button_demo.exe
```

### date_time（3 个）
```
calendar_picker      → fqw_date_time_calendar_picker_demo.exe
fast_calendar_picker → fqw_date_time_fast_calendar_picker_demo.exe
time_picker          → fqw_date_time_time_picker_demo.exe
```

### dialog_flyout（7 个）
```
color_dialog        → fqw_dialog_flyout_color_dialog_demo.exe
custom_message_box  → fqw_dialog_flyout_custom_message_box_demo.exe
dialog              → fqw_dialog_flyout_dialog_demo.exe
flyout              → fqw_dialog_flyout_flyout_demo.exe
folder_list_dialog  → fqw_dialog_flyout_folder_list_dialog_demo.exe
message_dialog      → fqw_dialog_flyout_message_dialog_demo.exe
teaching_tip        → fqw_dialog_flyout_teaching_tip_demo.exe
```

### layout（2 个）
```
flow_layout           → fqw_layout_flow_layout_demo.exe
adaptive_flow_layout  → fqw_layout_adaptive_flow_layout_demo.exe
```

### material（1 个）
```
acrylic_label → fqw_material_acrylic_label_demo.exe
```

### navigation（8 个）
```
breadcrumb_bar   → fqw_navigation_breadcrumb_bar_demo.exe
pivot            → fqw_navigation_pivot_demo.exe
tab_view         → fqw_navigation_tab_view_demo.exe
navigation_view  → fqw_navigation_navigation_view_demo.exe
```

### scroll（2 个）
```
pips_pager  → fqw_scroll_pips_pager_demo.exe
scroll_area → fqw_scroll_scroll_area_demo.exe
```

### status_info（5 个）
```
info_badge     → fqw_status_info_info_badge_demo.exe
progress_bar   → fqw_status_info_progress_bar_demo.exe
progress_ring  → fqw_status_info_progress_ring_demo.exe
state_tool_tip → fqw_status_info_state_tool_tip_demo.exe
tool_tip       → fqw_status_info_tool_tip_demo.exe
```

### text（6 个）
```
font_icon  → fqw_text_font_icon_demo.exe
label      → fqw_text_label_demo.exe
line_edit  → fqw_text_line_edit_demo.exe
spin_box   → fqw_text_spin_box_demo.exe
text_edit  → fqw_text_text_edit_demo.exe
```

### view（7 个）
```
card_widget → fqw_view_card_widget_demo.exe
flip_view   → fqw_view_flip_view_demo.exe
list_view   → fqw_view_list_view_demo.exe
table_view  → fqw_view_table_view_demo.exe
tree_view   → fqw_view_tree_view_demo.exe
```

### window（8 个）
```
fluent_window  → fqw_window_fluent_window_demo.exe
login_window   → fqw_window_login_demo.exe
clock          → fqw_window_clock_demo.exe
acrylic_window → fqw_window_acrylic_window_demo.exe
```

### gallery（1 个）
```
FluentQtWidgetsGallery.exe  → 综合演示
```

---

## 4. 测试程序清单（19 个）

```
tst_basic_input.exe, tst_charts.exe, tst_combo_box.exe,
tst_config.exe, tst_datetime.exe, tst_dialog_flyout.exe,
tst_gallery_pages.exe, tst_gallery_translation.exe, tst_layout.exe,
tst_material.exe, tst_menu.exe, tst_navigation.exe,
tst_qss.exe, tst_settings.exe, tst_status_info.exe,
tst_text.exe, tst_theme.exe, tst_view.exe, tst_window.exe
```

---

## 5. 编译环境详情

### 5.1 环境总览

| 组件 | 版本 | 安装路径 |
|------|------|----------|
| OS | Windows 10/11 x64 | — |
| IDE | Visual Studio 2026 Enterprise | `C:\Program Files\Microsoft Visual Studio\18\Enterprise\` |
| MSVC 编译器 | v14.51.36231 (v145) | `C:\Program Files\Microsoft Visual Studio\18\Enterprise\VC\Tools\MSVC\14.51.36231\` |
| Windows SDK | 10.0.26100.0 | `C:\Program Files (x86)\Windows Kits\10\` |
| CMake | 4.4.4 | `D:\tool\mingw64\bin\cmake.exe` |
| Ninja | 1.13.2 | `D:\tool\mingw64\bin\ninja.exe` |
| Qt | 6.7.3 win64_msvc2019_64 | `C:\Qt\6.7.3\msvc2019_64\` |

### 5.2 MSVC 编译器路径

```
Compiler:
  cl.exe   → C:\Program Files\Microsoft Visual Studio\18\Enterprise\VC\Tools\MSVC\14.51.36231\bin\Hostx64\x64\cl.exe
  link.exe → C:\Program Files\Microsoft Visual Studio\18\Enterprise\VC\Tools\MSVC\14.51.36231\bin\Hostx64\x64\link.exe
  rc.exe   → C:\Program Files (x86)\Windows Kits\10\bin\10.0.26100.0\x64\rc.exe

Environment Script:
  vcvars64.bat → C:\Program Files\Microsoft Visual Studio\18\Enterprise\VC\Auxiliary\Build\vcvars64.bat

Include:
  C:\Program Files\Microsoft Visual Studio\18\Enterprise\VC\Tools\MSVC\14.51.36231\include\

Lib:
  C:\Program Files\Microsoft Visual Studio\18\Enterprise\VC\Tools\MSVC\14.51.36231\lib\x64\
```

### 5.3 Windows SDK 路径

```
SDK Root  : C:\Program Files (x86)\Windows Kits\10\
Bin       : C:\Program Files (x86)\Windows Kits\10\bin\10.0.26100.0\x64\
Include   : C:\Program Files (x86)\Windows Kits\10\Include\10.0.26100.0\
Lib       : C:\Program Files (x86)\Windows Kits\10\Lib\10.0.26100.0\
```

### 5.4 Qt 6.7.3 路径

```
Qt Root   : C:\Qt\6.7.3\msvc2019_64\

Tools:
  qmake.exe → C:\Qt\6.7.3\msvc2019_64\bin\qmake.exe
  moc.exe   → C:\Qt\6.7.3\msvc2019_64\bin\moc.exe
  rcc.exe    → C:\Qt\6.7.3\msvc2019_64\bin\rcc.exe
  uic.exe    → C:\Qt\6.7.3\msvc2019_64\bin\uic.exe

Core DLLs:
  C:\Qt\6.7.3\msvc2019_64\bin\Qt6Core.dll
  C:\Qt\6.7.3\msvc2019_64\bin\Qt6Gui.dll
  C:\Qt\6.7.3\msvc2019_64\bin\Qt6Widgets.dll
  C:\Qt\6.7.3\msvc2019_64\bin\Qt6Svg.dll

CMake Config:
  C:\Qt\6.7.3\msvc2019_64\lib\cmake\Qt6\Qt6Config.cmake

Include:
  C:\Qt\6.7.3\msvc2019_64\include\

Lib:
  C:\Qt\6.7.3\msvc2019_64\lib\

Plugins:
  C:\Qt\6.7.3\msvc2019_64\plugins\
```

### 5.5 项目构建脚本

| 文件 | 路径 | 用途 |
|------|------|------|
| **构建脚本** | `build_msvc.ps1` | 一键配置 + 编译 |
| **CMake 项目预设** | `CMakePresets.json` | 内置预设（ninja-debug / ninja-release） |
| **CMake 用户预设** | `CMakeUserPresets.json` | 本地 MSVC 预设，含 Qt 路径 |
| **参考示例** | `CMakeUserPresets.json.example` | 预设文件模板 |

---

## 6. 重新构建

```powershell
# 方式一：脚本
powershell -ExecutionPolicy Bypass -File build_msvc.ps1

# 方式二：手动
cmake --preset local-msvc-debug
cmake --build --preset local-msvc-debug --parallel

# 方式三：VS2026 IDE → 打开文件夹 → 选 Local MSVC Debug → Ctrl+Shift+B
```

---

## 7. 注意事项

1. **Qt 版本兼容性**：当前 Qt 安装为 `win64_msvc2019_64` 套件，兼容 MSVC 2019+（包括 VS2026 的 v145 工具链）
2. **CMakeUserPresets.json**：此文件已加入 `.gitignore`，不会提交到仓库
3. **构建产物清理**：若需完全重编，删除 `out/msvc/` 目录后重新运行构建脚本
4. **IDE 打开方式**：必须用「打开本地文件夹」而非「从现有代码创建项目」