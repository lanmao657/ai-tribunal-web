# 《AI法庭》Ren'Py 导出 HTML5 并部署到 Vercel 完全指南

> **面向**：零基础用户
> **目标**：将 Ren'Py 视觉小说游戏导出为网页版，并部署到 Vercel 免费托管
> **预计耗时**：30-60 分钟（首次）

---

## 目录

1. [准备工作](#一准备工作)
2. [Ren'Py 导出 Web 步骤](#二renpy-导出-web-步骤)
3. [HTML5 导出注意事项](#三html5-导出注意事项)
4. [Vercel 部署步骤](#四vercel-部署步骤)
5. [文件结构说明](#五文件结构说明)
6. [常见错误解决方案](#六常见错误解决方案)
7. [进阶优化](#七进阶优化)

---

## 一、准备工作

### 1.1 你需要准备的东西

| 项目 | 说明 | 获取方式 |
|------|------|---------|
| Ren'Py SDK | 8.2.3 或更高版本 | [renpy.org](https://www.renpy.org/latest.html) 免费下载 |
| 项目文件 | `game/` 文件夹（含 script.rpy 等） | 已在 `e:\2026-项目\galgame\game\` |
| Vercel 账号 | 免费注册即可 | [vercel.com](https://vercel.com) |
| GitHub 账号 | 用于托管代码（可选，推荐） | [github.com](https://github.com) |
| 现代浏览器 | Chrome / Edge / Firefox | 用于本地测试 |

### 1.2 安装 Ren'Py SDK

**Windows 用户：**

1. 访问 https://www.renpy.org/latest.html
2. 下载 `renpy-8.x.x-sdk.zip`（约 100MB+）
3. 解压到一个**没有中文和空格**的路径，例如：
   ```
   ✅ 正确：D:\renpy\renpy-8.2.3-sdk
   ❌ 错误：D:\我的工具\renpy 8.2.3 sdk
   ```
4. 双击运行 `renpy.exe`，启动 Ren'Py 启动器

**Mac 用户：**
1. 下载 `renpy-8.x.x-sdk.zip`
2. 解压到 `~/renpy/renpy-8.2.3-sdk`
3. 终端运行 `./renpy.sh`

### 1.3 将项目添加到 Ren'Py 启动器

1. 打开 Ren'Py 启动器
2. 点击右下角 **「首选项」** → **「项目目录」**
3. 设置为 `E:\2026-项目`（注意：是 galgame 的**上一级**目录）
4. 返回主界面，点击 **「+ 创建新项目」** 旁边的下拉框
5. 应该能看到 `galgame` 项目出现在列表中
6. 选中 `galgame`

> **如果看不到项目**：检查 `game/` 文件夹是否在 `E:\2026-项目\galgame\` 下，且包含 `script.rpy`、`options.rpy` 等文件。

---

## 二、Ren'Py 导出 Web 步骤

### 2.1 导出操作

1. 在 Ren'Py 启动器中选中 `galgame` 项目
2. 点击主界面的 **「Web (Beta)」** 按钮
   - 如果看不到，点击 **「打开 项目目录」** 旁边的箭头展开更多选项
3. 点击 **「Build Web Application」**（构建 Web 应用）
4. 等待构建完成（首次约 1-3 分钟，取决于游戏体积）
5. 构建完成后会显示成功提示

### 2.2 本地测试

**强烈建议先本地测试，再部署。**

1. 在 Web (Beta) 面板点击 **「Build and Open in Browser」**
2. Ren'Py 会自动启动本地服务器并打开浏览器
3. 测试以下功能：
   - 主菜单能正常显示 ✓
   - 点击「开始游戏」能进入 ✓
   - 对白文字能正常显示 ✓
   - 存档/读档功能正常 ✓
   - 选择支能正常弹出 ✓
   - 证据展示界面能弹出 ✓
   - 案件档案界面能打开 ✓
4. 如果一切正常，进入下一步

### 2.3 找到导出文件

构建完成后，导出文件位于：

```
E:\2026-项目\galgame-1.0-dists\
└─ galgame-1.0-web\
   ├─ index.html          ← 网页入口
   ├─ game.zip            ← 游戏数据压缩包
   ├─ renpy-pre.js
   ├─ renpy.js
   ├─ renpy.wasm          ← WebAssembly 运行时（核心）
   ├─ pygame_..._script.js
   ├─ ...（其他文件）
   └─ index.html
```

同时会生成一个压缩包：`galgame-1.0-web.zip`

### 2.4 打开构建目录

- 在 Web (Beta) 面板点击 **「Open build Directory」**
- 这会直接打开包含导出文件的文件夹

---

## 三、HTML5 导出注意事项

### 3.1 功能限制

Web 版相比桌面版有如下限制（**本游戏不受影响**）：

| 功能 | Web 版支持 | 说明 |
|------|----------|------|
| 对白与选择 | ✅ 完全支持 | — |
| 存档/读档 | ✅ 完全支持 | 存储在浏览器 IndexedDB |
| 多结局 | ✅ 完全支持 | — |
| 自定义界面 | ✅ 完全支持 | — |
| 视频播放 | ⚠️ 受限 | 仅支持浏览器原生格式（mp4/webm） |
| 多线程 | ❌ 不支持 | Web 沙箱限制 |
| 网络请求 | ❌ 不支持 | 浏览器沙箱限制 |
| Live2D | ❌ 不支持 | — |

**本游戏的 script.rpy 没有使用上述受限功能，可放心导出。**

### 3.2 音频注意事项

- 浏览器**禁止自动播放音频**，必须用户点击一次游戏区域后才有声音
- OGG 格式在 Safari 不支持，建议同时提供 MP3 备份
- 如果游戏只有 MP3 音乐，在 `options.rpy` 添加：
  ```renpy
  define config.webaudio_required_types = [ "audio/mpeg" ]
  ```

### 3.3 文件大小建议

| 限制项 | 数值 | 说明 |
|--------|------|------|
| 单文件缓存上限 | 50MB | 超过的文件每次都会重新下载 |
| Vercel 单文件上限 | 25MB | 免费版限制 |
| 首次加载时间 | 建议 < 30s | 影响玩家留存 |

**本游戏使用纯色背景（Solid），文件体积极小，完全在限制内。**

### 3.4 渐进式下载配置（可选优化）

如果未来添加大量图片/音频，可在项目根目录创建 `progressive_download.txt`：

```
# RenPyWeb progressive download rules
# '+' = 按需下载, '-' = 启动时下载（默认）
# +/- type path
- image game/gui/**
+ image game/**
+ music game/audio/**
+ voice game/voice/**
```

这样图片和音乐会按需加载，加快首次启动。

### 3.5 添加网页图标与加载画面（可选）

在项目根目录（与 `game/` 同级）放置以下文件：

| 文件名 | 说明 | 规格 |
|--------|------|------|
| `web-icon.png` | 网页标签图标 | 512×512，正方形 |
| `web-presplash.png` | 加载启动图 | 任意尺寸，建议 1920×1080 |

重新构建 Web 版后，这些文件会自动包含。

---

## 四、Vercel 部署步骤

> Vercel 是一个免费的静态网站托管平台，非常适合托管 Ren'Py Web 版。

### 方法 A：通过 GitHub 部署（推荐，支持自动更新）

#### 步骤 1：创建 GitHub 仓库

1. 登录 [github.com](https://github.com)
2. 点击右上角 **「+」** → **「New repository」**
3. 仓库名填：`ai-tribunal-web`
4. 选择 **Public**（公开）或 **Private**（私有）均可
5. 点击 **「Create repository」**

#### 步骤 2：上传导出文件到 GitHub

**方式一：网页拖拽上传（最简单）**

1. 在本地打开构建目录：
   ```
   E:\2026-项目\galgame-1.0-dists\galgame-1.0-web\
   ```
2. 选中该文件夹内的**所有文件**
3. 在 GitHub 仓库页面点击 **「uploading an existing file」**
4. 将所有文件拖入上传区域
5. 在底部填写 commit message：`初始部署 AI法庭 Web 版`
6. 点击 **「Commit changes」**

> **注意**：Vercel 单文件上限 25MB。如果 `game.zip` 超过 25MB，参考第六章错误解决方案。

**方式二：使用 Git 命令行（进阶）**

```powershell
# 在 PowerShell 中执行
cd "E:\2026-项目\galgame-1.0-dists\galgame-1.0-web"
git init
git remote add origin https://github.com/你的用户名/ai-tribunal-web.git
git add .
git commit -m "初始部署 AI法庭 Web 版"
git branch -M main
git push -u origin main
```

#### 步骤 3：连接 Vercel

1. 访问 [vercel.com](https://vercel.com) 并登录（可用 GitHub 账号直接登录）
2. 进入 Dashboard 后点击 **「Add New…」** → **「Project」**
3. 在「Import Git Repository」中找到 `ai-tribunal-web` 仓库
4. 点击 **「Import」**

#### 步骤 4：配置部署

在配置页面：

| 配置项 | 填写内容 |
|--------|---------|
| Framework Preset | **Other**（其他） |
| Root Directory | `./`（默认） |
| Build Command | **留空**（不填写） |
| Output Directory | `./`（默认） |
| Install Command | **留空** |

> **关键**：Ren'Py Web 版已经是构建好的静态文件，Vercel 不需要再构建，直接托管即可。

5. 点击 **「Deploy」**
6. 等待 10-30 秒，显示 **「Congratulations!」** 即部署成功

#### 步骤 5：获取访问地址

部署完成后，Vercel 会给你一个地址，类似：
```
https://ai-tribunal-web-xxx.vercel.app
```

点击即可在浏览器中游玩你的游戏！

#### 步骤 6：自定义域名（可选）

1. 进入 Vercel 项目 → **Settings** → **Domains**
2. 输入你自己的域名（如 `ai-court.mydomain.com`）
3. 按提示在域名服务商处添加 CNAME 记录
4. 等待 DNS 生效（几分钟到几小时）

### 方法 B：通过 Vercel CLI 直接上传（无需 GitHub）

#### 步骤 1：安装 Node.js

1. 访问 [nodejs.org](https://nodejs.org) 下载 LTS 版本
2. 安装（一路 Next 即可）

#### 步骤 2：安装 Vercel CLI

打开 PowerShell，执行：

```powershell
npm install -g vercel
```

#### 步骤 3：登录 Vercel

```powershell
vercel login
```

按提示输入邮箱，完成登录验证。

#### 步骤 4：部署

```powershell
cd "E:\2026-项目\galgame-1.0-dists\galgame-1.0-web"
vercel
```

按提示操作：
- `Set up and deploy?` → 输入 `Y`
- `Which scope?` → 直接回车
- `Link to existing project?` → 输入 `N`
- `What's your project's name?` → 输入 `ai-tribunal`
- `In which directory?` → 直接回车
- `Want to modify settings?` → 输入 `N`

完成后会输出一个预览地址。正式部署执行：

```powershell
vercel --prod
```

---

## 五、文件结构说明

### 5.1 完整项目结构

```
ai-tribunal-web/                    ← Vercel 部署根目录
│
├─ index.html                       ← 网页入口（必须）
├─ game.zip                         ← 游戏数据包（核心，<25MB）
├─ game.data                        ← game.zip 的备用名（见错误处理）
├─ renpy-pre.js                     ← Ren'Py 预加载脚本
├─ renpy.js                         ← Ren'Py 主程序
├─ renpy.wasm                       ← WebAssembly 运行时（必须）
├─ pygame_..._script.js             ← Pygame.js 桥接脚本
├─ favicon.ico                      ← 网页图标
├─ web-icon.png                     ← 自定义图标（可选）
├─ web-presplash.png                ← 加载画面（可选）
├─ pwa/                             ← PWA 相关（可选）
│   ├─ manifest.json
│   └─ ...
├─ vercel.json                      ← Vercel 配置文件（建议添加）
└─ ...其他支持文件
```

### 5.2 关键文件说明

| 文件 | 作用 | 能否删除 |
|------|------|---------|
| `index.html` | 网页入口，加载所有脚本 | ❌ 不能 |
| `renpy.wasm` | WebAssembly 核心，运行 Ren'Py | ❌ 不能 |
| `renpy.js` | JavaScript 引导程序 | ❌ 不能 |
| `game.zip` | 你的游戏全部数据（脚本/图片/音频） | ❌ 不能 |
| `renpy-pre.js` | 预加载与初始化 | ❌ 不能 |
| `web-icon.png` | 浏览器标签图标 | ✅ 可选 |
| `web-presplash.png` | 加载时的启动图 | ✅ 可选 |

### 5.3 添加 vercel.json 配置（重要）

在部署根目录创建 `vercel.json` 文件，内容如下：

```json
{
  "headers": [
    {
      "source": "/(.*)\\.wasm",
      "headers": [
        {
          "key": "Content-Type",
          "value": "application/wasm"
        }
      ]
    },
    {
      "source": "/(.*)",
      "headers": [
        {
          "key": "Cross-Origin-Opener-Policy",
          "value": "same-origin"
        },
        {
          "key": "Cross-Origin-Embedder-Policy",
          "value": "require-corp"
        }
      ]
    }
  ]
}
```

**作用：**
- 让 `.wasm` 文件以正确的 MIME 类型传输（加载更快）
- 设置跨域隔离头（部分 WebAssembly 功能需要）

---

## 六、常见错误解决方案

### 错误 1：游戏加载卡住 / 白屏

**现象**：打开网页后一直白屏，或卡在加载界面。

**解决方案**：

1. **检查 game.zip 是否上传成功**
   - 大文件可能上传超时
   - 用方法 B（CLI）上传更稳定

2. **重命名 game.zip 为 game.data**
   - 有些服务器对 `.zip` 后缀有特殊处理
   - 将 `game.zip` 重命名为 `game.data`
   - 用文本编辑器打开 `index.html`
   - 找到 `game.zip` 替换为 `game.data`
   - 重新上传

3. **检查浏览器控制台**
   - 按 `F12` 打开开发者工具
   - 查看 Console 标签的红色错误信息
   - 常见错误见下文

### 错误 2：Vercel 报错 "File size limit exceeded"

**现象**：部署时提示单个文件超过 25MB 限制。

**解决方案**：

1. **压缩 game.zip**
   - 检查 `game/` 下是否有大体积文件（视频、高清图片）
   - 压缩图片：使用 [tinypng.com](https://tinypng.com) 批量压缩
   - 音频转 MP3 128kbps
   - 重新构建 Web 版

2. **使用渐进式下载**
   - 编辑 `progressive_download.txt`（见 3.4 节）
   - 让大文件按需加载，不打包进 game.zip

3. **改用其他平台**
   - 如果游戏体积确实很大（>100MB），考虑：
     - [itch.io](https://itch.io)（上限 1GB，更适合游戏）
     - [Cloudflare Pages](https://pages.cloudflare.com)（单文件 25MB，但可拆分）
     - 自建服务器（Nginx 托管）

### 错误 3：中文字体显示为方块/乱码

**现象**：英文正常，中文显示为 □□□ 或乱码。

**原因**：浏览器默认字体不含中文字形。

**解决方案**：

本游戏的 `gui.rpy` 已使用 `DejaVuSans.ttf`，该字体**不含中文**。需要修改：

1. 下载中文字体，如思源黑体：
   - [思源黑体 GitHub](https://github.com/adobe-fonts/source-han-sans/releases)
   - 下载 `SourceHanSansSC-Regular.otf`

2. 将字体文件放入：
   ```
   E:\2026-项目\galgame\game\gui\font\SourceHanSansSC-Regular.otf
   ```

3. 修改 `gui.rpy`，找到字体定义部分，改为：
   ```renpy
   define gui.text_font = "gui/font/SourceHanSansSC-Regular.otf"
   define gui.name_text_font = "gui/font/SourceHanSansSC-Regular.otf"
   define gui.interface_text_font = "gui/font/SourceHanSansSC-Regular.otf"
   define gui.system_font = "gui/font/SourceHanSansSC-Regular.otf"
   ```

4. 重新构建 Web 版并部署

> **提示**：思源黑体完整版约 10MB，会增加游戏体积。可使用字体子集化工具（如 fontmin）提取常用字，压缩到 2-3MB。

### 错误 4：音频不播放

**现象**：游戏能运行，但没有背景音乐或音效。

**原因**：浏览器禁止自动播放音频。

**解决方案**：
- 这是正常行为，不是 Bug
- 玩家需要**点击游戏画面一次**后，音频才会播放
- 建议在 `index.html` 的加载画面添加提示：「点击进入游戏」

### 错误 5：存档丢失

**现象**：关闭浏览器后重新打开，存档没了。

**原因**：浏览器清除了 IndexedDB 数据。

**解决方案**：
- 这是 Web 版固有特性
- 游戏左上角有「汉堡菜单」（☰），提供**导出存档**功能
- 玩家可下载存档文件备份
- 换设备时用**导入存档**功能恢复

### 错误 6：移动端显示异常

**现象**：手机上画面比例不对，或点击不灵敏。

**解决方案**：

在 `index.html` 的 `<head>` 中确认有以下 meta 标签：

```html
<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no" />
```

如果没有，手动添加。这能确保移动端正确缩放。

### 错误 7：Vercel 部署成功但打开是 404

**现象**：访问域名显示 404 Not Found。

**解决方案**：
1. 检查仓库根目录是否有 `index.html`
2. 在 Vercel 项目设置中确认：
   - Output Directory 为 `./` 或留空
   - 不要勾选 "Override Build Command"
3. 重新部署

### 错误 8：控制台报错 "wasm compilation failed"

**现象**：F12 控制台显示 WebAssembly 编译失败。

**解决方案**：
1. 确认浏览器版本足够新（Chrome 90+ / Firefox 90+ / Safari 15+）
2. 确认 `vercel.json` 中 `.wasm` 的 MIME 类型配置正确
3. 确认 `renpy.wasm` 文件完整上传（对比本地文件大小）

### 错误 9：git push 报错文件过大

**现象**：`git push` 时报错 `file too large`。

**解决方案**：

GitHub 单文件限制 100MB。如果 game.zip 超过 100MB：

1. 安装 [Git LFS](https://git-lfs.com)
2. 在项目目录执行：
   ```powershell
   git lfs install
   git lfs track "*.zip"
   git lfs track "*.wasm"
   git add .gitattributes
   ```
3. 重新 add 和 commit

或者**直接用 Vercel CLI 部署**（方法 B），绕过 GitHub。

---

## 七、进阶优化

### 7.1 添加 PWA 支持（可安装为 App）

Ren'Py Web 版默认支持 PWA。部署后：
- 在 Chrome 中访问游戏
- 地址栏右侧会出现「安装」图标
- 点击安装后，游戏可像原生 App 一样从桌面启动

### 7.2 自定义加载画面

1. 制作一张加载图 `web-presplash.png`（建议 1920×1080）
2. 放入项目根目录（与 `game/` 同级）
3. 重新构建 Web 版

### 7.3 添加访问统计（可选）

在 `index.html` 的 `</body>` 前添加统计代码，如 Google Analytics 或 Umami。

### 7.4 加速首次加载

1. **压缩 game.zip**：目标 < 10MB
2. **使用 CDN**：将 `renpy.wasm` 等核心文件放到 Cloudflare CDN
3. **开启 Brotli 压缩**：Vercel 默认已开启

### 7.5 更新游戏

**通过 GitHub 部署的**：
1. 修改代码后在本地重新构建 Web 版
2. 将新的导出文件覆盖到 GitHub 仓库
3. Vercel 自动检测到更新并重新部署（约 30 秒）

**通过 CLI 部署的**：
```powershell
cd "E:\2026-项目\galgame-1.0-dists\galgame-1.0-web"
vercel --prod
```

---

## 附录：完整部署 Checklist

按顺序勾选，确保万无一失：

### 准备阶段
- [ ] 安装 Ren'Py SDK 8.2.3+
- [ ] 项目能正常在 Ren'Py 启动器中打开
- [ ] 注册 GitHub 账号
- [ ] 注册 Vercel 账号（用 GitHub 登录）

### 构建阶段
- [ ] 点击「Build and Open in Browser」本地测试通过
- [ ] 确认主菜单、对白、选择、存档功能正常
- [ ] 确认中文字体能正常显示
- [ ] 检查 `game.zip` 大小（建议 < 25MB）

### 部署阶段
- [ ] 创建 GitHub 仓库 `ai-tribunal-web`
- [ ] 上传 `galgame-1.0-web` 文件夹内所有文件
- [ ] 添加 `vercel.json` 配置文件
- [ ] 在 Vercel 导入项目
- [ ] Framework Preset 选择 Other
- [ ] Build Command 和 Install Command 留空
- [ ] 点击 Deploy 并等待成功

### 验证阶段
- [ ] 访问 Vercel 提供的地址
- [ ] 游戏能正常加载
- [ ] 能进入主菜单
- [ ] 能开始游戏并看到对白
- [ ] 能存档和读档
- [ ] 在手机浏览器测试（可选）

---

**文档版本**：v1.0
**最后更新**：2026-06-18
**参考来源**：[Ren'Py 官方 Web 文档](https://www.renpy.org/doc/html/web.html)

遇到问题无法解决？检查第六章常见错误，或访问：
- [Ren'Py 官方论坛](https://lemmasoft.renai.us)
- [Ren'Py 中文社区](https://doc.renpy.cn)
