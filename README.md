# ATM9 中文附加包

给 **All the Mods 9（ATM9）** 加的三样东西，都是独立于原版内容之外的附加内容：

| 内容 | 说明 |
|---|---|
| 🧭 **模组入门引导任务线** | **19 章 / 828 个任务**，自制的中文入门教程，**可选 · 仅供参考**，欢迎指正修改 |
| 🌏 **汉化资源包** | 模组简体中文本地化，来源为 CFPA 汉化包 + 柠娜提供的汉化补丁 + AI 翻译补全 |
| ➕ **新增模组** | 官方 ATM9 之外额外加装的 16 个模组，清单见下 |

> 本仓库**不包含 ATM9 本体，也不包含任何 ATM9 的原版文件**。
> 请先自行安装 ATM9，再把这里的内容叠加上去。

---

## 快速开始

**前置**：已安装 **All the Mods 9**（1.20.1 / Forge），版本建议 1.1.0 及以上。

```text
1. 下载本仓库（Code → Download ZIP，或 git clone）
2. 把 overrides/ 里的内容复制到 ATM9 实例根目录，遇到同名文件夹选择「合并」
3. 打开 config/ftbquests/quests/chapter_groups.snbt，
   把 install/chapter_groups.追加片段.snbt 里那一行追加进 chapter_groups 数组
4. 启动游戏 → 按 Q 打开任务书 → 顶部会多出一个「科技入门教程」标签页
```

汉化资源包会在第 2 步一并装好（进入 `resourcepacks/`）。若游戏内没生效，到
`选项 → 资源包` 里把它移到右侧启用。

---

## 新增模组清单

基准：**官方 ATM9 1.1.0**（CurseForge 文件 `6985843`，433 个模组）。

| 模组 | 模组 ID | 版本 |
|---|---|---|
| 车万女仆 Touhou Little Maid | `touhou_little_maid` | 1.5.3 |
| 通用拼音搜索 Just Enough Characters | `jecharacters` | 4.6.9 |
| 输入法冲突修复 IMBlocker | `imblocker` | 5.6.1 |
| I18nUpdateMod | `i18nupdatemod` | 3.6.2 |
| ME 综合工作终端 AE2 WCWT | `wcwt` | 1.20.1.10 |
| AE2 Utility | `ae2utility` | 20.1.0 |
| AE2NetworkAnalyzer | `ae2netanalyser` | 1.20-1.0.6 |
| AppliedE | `appliede` | 0.14.3 |
| ProjectE（等价交换重制版） | `projecte` | 1.0.1 |
| ExtendedAE Plus | `extendedae_plus` | 1.6.1 |
| Sign Plates | `sign_plates` | 1.1.2 |
| Big Signs | `big_signs` | 1.1 |
| Improved Sign Editing | `improvedsignediting` | 1.5 |
| Collective | `collective` | 8.39 |
| Colorwheel | `colorwheel` | 1.0.0+mc1.20.1 |
| Draconic Evolution Render Patcher | `derenderpatcher` | 1.3.0 |

> 官方后续发布的 **1.1.1** 里已收录 Colorwheel、并把 Oculus 加了回来，
> 另有 66 个模组版本变动。升到 1.1.1 之后这份清单要重新比对，别直接沿用。

详细的差异分析与复核方法见 [`docs/新增模组清单.md`](docs/新增模组清单.md)。

---

## 目录结构

```
.
├── overrides/                      叠加到 ATM9 实例根目录
│   ├── config/ftbquests/quests/chapters/   19 个自创章节 t00 ~ t18
│   └── resourcepacks/                      汉化资源包
├── install/
│   └── chapter_groups.追加片段.snbt         需手动追加的分组注册行
├── docs/
│   ├── 新增模组清单.md
│   ├── 任务线说明.md
│   └── 汉化包说明.md
├── LICENSE
└── README.md
```

---

## 一些实话

**关于这条任务线。** 它是**自制的辅助引导线**，目的是帮新手入门各个模组，**可选**——
玩家可以自由探索 ATM9 原本的任务线，不跟着走、只挑某几章看、打乱顺序，都没关系。
内容**仅供参考**，是一种可行做法而非最优解。发现错漏欢迎在本仓库提 issue 或 PR 指正。

**关于兼容性。** 任务里所有物品 ID 都取自 ATM9 1.1.0 的实际注册表，并在安装前做过四层校验
（资产层 / 数据层 / 代码层 / 脚本层），923 处引用、701 个唯一 ID，**0 个不存在**。
但如果你用的 ATM9 版本差得比较多，个别 ID 可能失效——那种情况下去对应章节里点一下问号图标就知道是哪个。

**关于安装方式。** 任务线是 **19 个新增章节文件**，不改动 ATM9 的任何原有任务。
不想要了，把 `chapters/` 里 `t00_overview.snbt` ~ `t18_magic_adventure.snbt` 这 19 个删掉即可
（那个分组注册行留着也无害，只会显示一个空分组）。

**关于汉化包。** 来源有三块：**CFPA 汉化包的转换版**、**柠娜提供的汉化补丁**，
以及**自己用 AI 跑出来的翻译补全**。署名详见 `docs/汉化包说明.md`。

---

## 更新日志

### 2026-09-15

- 以官方 ATM9 1.1.0（`manifest.json` + `modlist.html`，各 433 条）为基准，
  重新核对手上这份模组清单，订正此前记忆有误的地方。
- 版本订正：Applied Energistics 2 → 官方 **15.4.8**；
  AE2 Wireless Terminals → 官方 **15.2.3**；Applied Botanics → 官方 **1.5.0**。
- 归类订正：ExtendedAE Plus 官方清单里没有（只有 ExtendedAE 本体 `ex-pattern-provider`），
  从「替换」改为「新增」；CC: Tweaked 官方 1.1.0 交付的就是 **1.116.1**，不是本包升级。
- 清单结构改为只保留「现有模组 + 模组 ID + 版本」，移除所有作用描述与历史变动记录。
- 补充汉化资源包的来源署名：CFPA 汉化包 + 柠娜提供的汉化补丁 + 自己用 AI 跑的翻译补全。

---

## 许可

| 部分 | 许可 |
|---|---|
| 本仓库的**任务线文本与文档** | [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.zh) |
| **汉化资源包** | CC BY-NC-SA 4.0（沿用 CFPA 原许可，署名 CFPA 团队） |

一句话：**可以自由分享和修改，但要署名、不能商用、改完必须用同样的许可发布。**

**All the Mods 9 本身是 All Rights Reserved。** 本仓库不含其任何文件，
也请不要把本仓库内容与原版任务书打包后公开转载。

---

## 致谢

- [CFPA 汉化项目](https://cfpa.site/) — 汉化资源包的原作者
- **柠娜** — 提供汉化补丁，补上了 CFPA 未覆盖的那部分条目
- [All the Mods 9](https://www.curseforge.com/minecraft/modpacks/all-the-mods-9) — 整合包本体
- 以及所有模组的作者
