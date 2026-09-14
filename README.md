# ATM9 中文附加包

给 **All the Mods 9（ATM9）** 加的三样东西，都是独立于原版内容之外的附加内容：

| 内容 | 说明 |
|---|---|
| 🧭 **模组入门引导任务线** | **19 章 / 828 个任务**，原创中文教程。从零讲清每个科技/魔法模组的核心循环、方块大全、多方块结构、实战产线 |
| 🌏 **汉化资源包** | 模组简体中文本地化（CFPA 汉化包转换版，含 AI 翻译补全） |
| 📋 **新增模组清单** | 本包在原版 ATM9 之上新增/升级的模组，含作用说明 |

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

**关于兼容性。** 任务里所有物品 ID 都取自 ATM9 1.1.0 的实际注册表，并在安装前做过四层校验
（资产层 / 数据层 / 代码层 / 脚本层），923 处引用、701 个唯一 ID，**0 个不存在**。
但如果你用的 ATM9 版本差得比较多，个别 ID 可能失效——那种情况下去对应章节里点一下问号图标就知道是哪个。

**关于安装方式。** 任务线是 **19 个新增章节文件**，不改动 ATM9 的任何原有任务。
不想要了，把 `chapters/` 里 `t00_overview.snbt` ~ `t18_magic_adventure.snbt` 这 19 个删掉即可
（那个分组注册行留着也无害，只会显示一个空分组）。

**关于汉化包。** 它是 **CFPA 汉化包**的转换版，另有部分条目由 AI 翻译补全。
原文与主要工作属于 CFPA 团队，署名见 `docs/汉化包说明.md`。

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
- [All the Mods 9](https://www.curseforge.com/minecraft/modpacks/all-the-mods-9) — 整合包本体
- 以及所有模组的作者
