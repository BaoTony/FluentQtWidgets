# FluentQtWidgets 二次开发指南

> 最后更新：2026-10-31 | 基于 `dev` 分支

---

## 1. 环境准备

参见 [build-environment-report.md](build-environment-report.md)，已就绪：

| 组件 | 路径 |
|------|------|
| MSVC 编译器 | `C:\Program Files\Microsoft Visual Studio\18\Enterprise\VC\Tools\MSVC\14.51.36231\bin\Hostx64\x64\` |
| Qt 6.7.3 | `C:\Qt\6.7.3\msvc2019_64\` |
| CMake 4.4.4 | `D:\tool\mingw64\bin\cmake.exe` |
| Ninja | `D:\tool\mingw64\bin\ninja.exe` |

### 快速构建

```powershell
powershell -ExecutionPolicy Bypass -File build_msvc.ps1
```

或手动：

```powershell
cmake --preset local-msvc-debug
cmake --build --preset local-msvc-debug --parallel
```

---

## 2. 项目架构

### 2.1 四层架构

```
┌─────────────────────────────────────────────┐
│  4. Applications                            │
│     Gallery / examples / tests              │
├─────────────────────────────────────────────┤
│  3. Composition                             │
│     Dialogs / Navigation / Settings /       │
│     Date-time / Flyout / Window shells      │
├─────────────────────────────────────────────┤
│  2. Controls                                │
│     Button / Label / Input / Slider /       │
│     Switch / Progress / InfoBar ...         │
├─────────────────────────────────────────────┤
│  1. Core                                    │
│     Theme / StyleSheet / FluentIcon /       │
│     Config / Translator                     │
└─────────────────────────────────────────────┘
```

### 2.2 源码目录

```
FluentQtWidgets/
├── include/FluentQtWidgets/          # 公开头文件
│   ├── FluentQtWidgets.h             # 聚合头
│   ├── Global.h                      # 全局定义、枚举
│   ├── Theme.h / StyleSheet.h        # 核心：主题和样式
│   ├── DateTime/                     # 日期时间控件
│   ├── Dialogs/                      # 对话框
│   ├── Layout/                       # 布局
│   ├── Navigation/                   # 导航控件
│   ├── Settings/                     # 设置卡片
│   ├── Views/                        # 列表/树/表视图
│   ├── Widgets/                      # 基础控件
│   └── Window/                       # 窗口框架
├── src/                              # 源文件（对应 include 结构）
├── resources/fluentqtwidgets/        # 资源文件
│   ├── qss/light/*.qss               # 浅色主题 QSS
│   ├── qss/dark/*.qss                # 深色主题 QSS
│   └── images/                       # 图标、图片
├── examples/                         # 53 个独立示例
├── tests/                            # 19 个测试程序
├── docs/                             # 文档
└── cmake/                            # CMake 模块
```

### 2.3 CMake 目标

| Target | 说明 |
|--------|------|
| `FluentQtWidgets::Widgets` | **公共目标**，使用者只需链接此目标 |
| `FluentQtWidgets::FluentQtWidgets` | 兼容别名 |
| `FluentQtWidgets::Multimedia` | 可选：多媒体模块 |
| `FluentQtWidgets::DesignerPlugin` | 可选：Qt Designer 插件 |
| `FluentQtWidgets::WindowEffects` | 可选：窗口特效 |

**关键 CMake 选项**：

| 选项 | 默认值 | 说明 |
|------|--------|------|
| `FQW_BUILD_SHARED` | `ON` | 构建动态库 |
| `FQW_BUILD_EXAMPLES` | `ON` | 构建示例 |
| `FQW_BUILD_TESTS` | `OFF` | 构建测试 |
| `FQW_QT_MAJOR_VERSION` | `6` | Qt 主版本 |

---

## 3. IDE 选择

本机已安装 **Visual Studio 2026 Enterprise** 和 **VS Code**。

### 3.1 Visual Studio 2026 Enterprise（推荐）

| 项目 | 信息 |
|------|------|
| 入口 | `C:\Program Files\Microsoft Visual Studio\18\Enterprise\Common7\IDE\devenv.exe` |
| C++ 工作负载 | 已安装 |
| 编译器 | MSVC v14.51.36231 (v145) |

**为什么推荐 VS2026：**

1. **原生 CMake 集成** — 无需装插件，直接在 VS 中打开 CMake 项目
2. **MSVC 原生编译** — 无需额外配置 MSVC 环境变量
3. **顶级调试体验** — 可视化断点、内存检查、性能分析
4. **IntelliSense 完备** — 代码补全、跳转定义、重构

**打开项目方式：**

```
启动 VS2026 → "打开本地文件夹" → 选择项目根目录
```

> **重要**：必须用「打开本地文件夹」，不是「创建新项目」或「打开解决方案」

**首次配置步骤：**

1. 打开文件夹后，顶部工具栏 CMake 预设下拉 → 选择 **Local MSVC Debug**（不是 Ninja Debug）
2. 查看「输出」窗口 → 选择「CMake」，确认 `Found Qt6: C:/Qt/6.7.3/msvc2019_64`
3. 确认后 `Ctrl+Shift+B` 编译

| 操作 | 快捷键 |
|------|--------|
| 构建全部 | `Ctrl+Shift+B` |
| 运行/调试 | `F5` |
| 断点切换 | `F9` |
| 跳转定义 | `F12` |
| 查找文件 | `Ctrl+,` |

### 3.2 VS Code（备选）

| 项目 | 信息 |
|------|------|
| 入口 | `code` 命令（已在 PATH） |
| 已配置 | `.vscode/tasks.json`、`.vscode/launch.json` |

```powershell
code D:\dev\store\txp666\FluentQtWidgets
```

### 3.3 建议分工

| 场景 | 推荐 |
|------|------|
| 编译/调试/性能分析 | **VS2026** |
| 快速浏览/搜索替换 | VS Code |

---

## 4. 预览 UI 效果

本项目是**纯代码 UI 开发**，没有 `.ui` 文件，界面完全通过 C++ 代码构建。

### 方式一：运行已编译示例

```powershell
# 综合 Gallery
out\msvc\examples\gallery\FluentQtWidgetsGallery.exe

# 各控件示例
out\msvc\examples\basic_input\button\fqw_basic_input_button_demo.exe
out\msvc\examples\date_time\calendar_picker\fqw_date_time_calendar_picker_demo.exe
out\msvc\examples\window\login\fqw_window_login_demo.exe
```

### 方式二：改代码 → 增量编译 → 运行

```
┌──────────────┐     ┌──────────────────┐     ┌──────────────┐
│ 修改 .cpp     │ ──▶ │ Ctrl+Shift+B     │ ──▶ │ F5 运行看效果  │
└──────────────┘     └──────────────────┘     └──────────────┘
```

---

## 5. 开发流程

### 5.1 增量编译

```powershell
cmake --build --preset local-msvc-debug --parallel
```

### 5.2 运行测试

```powershell
cmake --preset local-msvc-debug -DFQW_BUILD_TESTS=ON
cmake --build --preset local-msvc-debug --parallel
cd out\msvc\tests
.\tst_basic_input.exe
```

### 5.3 格式化代码

```powershell
clang-format -i src/widgets/Button.cpp
```

---

## 6. 添加新控件（以 RatingControl 为例）

### 头文件 `include/FluentQtWidgets/Widgets/RatingControl.h`：

```cpp
#pragma once
#include <FluentQtWidgets/Global.h>
#include <QWidget>

FQW_NAMESPACE_BEGIN

class RatingControl : public QWidget
{
    Q_OBJECT
    Q_PROPERTY(int maxRating READ maxRating WRITE setMaxRating)
    Q_PROPERTY(int rating READ rating WRITE setRating NOTIFY ratingChanged)

public:
    explicit RatingControl(QWidget *parent = nullptr);
    int maxRating() const;
    void setMaxRating(int max);
    int rating() const;
    void setRating(int rating);

signals:
    void ratingChanged(int rating);

protected:
    void paintEvent(QPaintEvent *event) override;
    void mousePressEvent(QMouseEvent *event) override;

private:
    int m_maxRating = 5;
    int m_rating = 0;
};

FQW_NAMESPACE_END
```

### 源文件 `src/widgets/RatingControl.cpp`：

```cpp
#include <FluentQtWidgets/Widgets/RatingControl.h>
#include <QPainter>
#include <QMouseEvent>

FQW_NAMESPACE_BEGIN

RatingControl::RatingControl(QWidget *parent) : QWidget(parent)
{
    setMinimumSize(120, 24);
}

int RatingControl::maxRating() const { return m_maxRating; }
void RatingControl::setMaxRating(int max) { m_maxRating = max; update(); }
int RatingControl::rating() const { return m_rating; }

void RatingControl::setRating(int rating)
{
    if (m_rating != rating) {
        m_rating = rating;
        emit ratingChanged(m_rating);
        update();
    }
}

void RatingControl::paintEvent(QPaintEvent *event)
{
    Q_UNUSED(event)
    QPainter painter(this);
    painter.setRenderHint(QPainter::Antialiasing);
    for (int i = 0; i < m_maxRating; ++i) {
        QRect rect(i * 24, 0, 24, 24);
        painter.fillRect(rect, (i < m_rating) ? Qt::yellow : Qt::lightGray);
    }
}

void RatingControl::mousePressEvent(QMouseEvent *event)
{
    setRating(event->position().x() / 24 + 1);
}

FQW_NAMESPACE_END
```

### 注册到 CMakeLists.txt：

- `FQW_PUBLIC_HEADERS` 添加 `include/FluentQtWidgets/Widgets/RatingControl.h`
- `FQW_SOURCES` 添加 `src/widgets/RatingControl.cpp`

### 重新构建：

```powershell
powershell -ExecutionPolicy Bypass -File build_msvc.ps1
```

---

## 7. 代码规范

### 7.1 命名空间

```cpp
FQW_NAMESPACE_BEGIN
// 你的代码
FQW_NAMESPACE_END
```

### 7.2 类命名

| Python 参考 | C++ 实现 |
|-------------|----------|
| `PushButton` | `FluentQt::PushButton` |
| `PrimaryPushButton` | `FluentQt::PrimaryPushButton` |

### 7.3 样式系统

- 每个控件独立 QSS：`:/qfluentwidgets/qss/{light|dark}/button.qss`
- 动态属性配合 QSS 选择器（`isPressed`、`isHover`）
- 修改动态属性后必须调用 `polish/unpolish`

### 7.4 图标处理

按钮使用 `_icon` 模型：图标在控件内部自行绘制，Qt 基类的 `icon` 保持为空。

### 7.5 主题响应

通过 `StyleSheetManager` 注册需要响应主题切换的控件。

---

## 8. 调试技巧

| 操作 | 快捷键 |
|------|--------|
| 启动调试 | `F5` |
| 逐语句 | `F11` |
| 逐过程 | `F10` |
| 运行到光标 | `Ctrl+F10` |

### 常见问题

| 问题 | 排查 |
|------|------|
| CMake 找不到 Qt | 切换预设到 **Local MSVC Debug** |
| 链接错误 | 检查 `.cpp` 是否在 `FQW_SOURCES` 中 |
| 头文件找不到 | 检查是否在 `FQW_PUBLIC_HEADERS` 中 |
| 样式不生效 | 检查 QSS 是否在 `.qrc` 中注册 |

---

## 9. 提交与推送

```powershell
git checkout dev
git add src/widgets/RatingControl.cpp include/FluentQtWidgets/Widgets/RatingControl.h
git commit -m "feat: add RatingControl widget"
git push origin dev
```

| 前缀 | 用途 |
|------|------|
| `feat:` | 新功能/新控件 |
| `fix:` | Bug 修复 |
| `build:` | 构建系统 |
| `docs:` | 文档 |
| `refactor:` | 重构 |

---

## 10. 参考资源

| 文档 | 路径 |
|------|------|
| 编译环境报告 | [docs/build-environment-report.md](build-environment-report.md) |
| 快速入门 | [docs/quick-start.md](quick-start.md) |
| 架构说明 | [docs/architecture.md](architecture.md) |
| 控件列表 | [docs/controls-basic.md](controls-basic.md) |
| Python→C++ 移植指南 | [docs/porting-guide.md](porting-guide.md) |
| API 路线图 | [docs/api-roadmap.md](api-roadmap.md) |