# Claude Code Plugins

本仓库包含一组用于扩展 Claude Code CLI 能力的配置文件。

## 项目结构

```
├── agents/              # Agent 配置文件
│   ├── document-analyzer.md
│   ├── feature-explorer.md
│   └── rest-api-tester.md
├── commands/            # 命令配置文件
│   └── implement-guide.md
├── plugins/             # 插件目录 (预留)
└── skills/              # 技能配置
    ├── git-commit-cn/
    └── webapp-testing/
```

## 功能特性

### Agents

| Agent | 用途 |
|-------|------|
| `document-analyzer` | 文档分析代理，支持 PDF、论文、技术文档等 |
| `feature-explorer` | 功能探索代理，在实现新功能前深度分析代码库 |
| `rest-api-tester` | REST API 测试代理，验证 API 端点并生成测试脚本 |

### Commands

| Command | 用途 |
|---------|------|
| `implement-guide` | 引导式分步实施流程 |

### Skills

| Skill | 用途 |
|-------|------|
| `git-commit-cn` | 生成符合约定式提交规范的中文 Git 提交信息 |
| `webapp-testing` | 使用 Playwright 进行本地 Web 应用测试 |

## 快速开始

### 使用 Skills

```bash
# 生成中文提交信息
/claude-code-plugins/skills/git-commit-cn

# Web 应用测试
/claude-code-plugins/skills/webapp-testing
```

### 使用 Agents

通过 Task 工具调用专业化的 Agents：

```bash
# 文档分析
Task --subagent-type document-analyzer --prompt "请分析这个文档"

# 功能探索
Task --subagent-type feature-explorer --prompt "请探索这个代码库的结构"

# API 测试
Task --subagent-type rest-api-tester --prompt "请测试这个 API 端点"
```

### 使用 Commands

```bash
# 实施向导
/claude-code-plugins/commands/implement-guide
```

## 详细说明

### Skills

#### git-commit-cn
自动生成符合 [Conventional Commits](https://www.conventionalcommits.org/) 规范的中文提交信息。

支持的类型：
- `feat`: 新功能
- `fix`: Bug 修复
- `docs`: 文档更新
- `style`: 代码格式调整
- `refactor`: 重构
- `perf`: 性能优化
- `test`: 测试
- `build`: 构建
- `ci`: CI 配置
- `chore`: 其他维护工作

#### webapp-testing
使用 Playwright 进行 Web 应用测试的工具包，支持：
- 前端功能验证
- UI 行为调试
- 浏览器截图
- 浏览器日志查看

### Agents

#### document-analyzer
深度分析各类文档，包括：
- 研究论文
- 技术文档
- PDF 文件
- 图片内容理解

#### feature-explorer
在实现新功能前，系统性地：
- 分析现有代码库结构
- 识别相关文件和组件
- 理解代码模式和数据流

#### rest-api-tester
自动化 API 测试流程：
- 验证 HTTP 响应行为
- 检查状态码
- 验证响应体内容
- 测试认证流程
- 生成 Python 测试脚本

### Commands

#### implement-guide
引导式分步实施工作流：
1. 上下文读取与理解
2. 计划执行与测试验证
3. 记录与洞察
4. Git 版本控制

## License

各组件可能有不同的 License，请参考各自目录下的 LICENSE 文件。
