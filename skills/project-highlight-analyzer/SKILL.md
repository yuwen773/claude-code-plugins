---
name: project-highlight-analyzer
description: |
  Use when user asks to analyze project highlights, extract resume material,
  describe tech stack, or showcase code value.
---

# 项目亮点分析

## 分析流程

### 第零步：确认用户需求（必须）

先询问用户：
- 突出方向：技术深度/业务价值/性能优化/工程规范
- 校招还是社招？目标岗位是什么？

根据选择调整分析重点。

### 第一步：结构扫描 + 技术栈

- 扫描项目模块结构
- 读取 pom.xml 提取：Java版本、Spring版本、数据库/缓存/消息队列

### 第二步：核心架构分析

1. **先从 pom.xml 检测项目使用的技术栈**
2. **再根据检测到的技术搜索对应代码模式**

| 检测到的技术 | 搜索关键词 |
|-------------|----------|
| Redis | `RedisTemplate`、`redisTemplate`、`@Cacheable` |
| Kafka | `KafkaProducer`、`kafkaTemplate`、`@KafkaListener` |
| 异步并发 | `@Async`、`CompletableFuture`、`Executor` |
| 事务 | `@Transactional` |
| 设计模式 | `Strategy`、`Factory`、`Template` |

### 第三步：验证技术点（必须）

禁止虚构！每个亮点必须：
1. Grep 定位具体类/方法
2. Read 读取代码片段
3. 记录文件路径和行号

## 输出格式

1. **项目概述** - 背景、技术架构
2. **技术栈表** - 类别/技术/使用场景
3. **核心亮点** - 5-10个，每个含文件路径+代码
4. **STAR描述** - 2-3个核心项目经验
5. **专业技能** - 精通/熟悉/了解
6. **面试追问** - 预判可能被问的问题

## 文档生成（必须）

1. 创建 `interview-docs/` 目录（如不存在）
2. 命名：`{特色点}_{yyyyMMdd}.md`
3. 包含上述6部分 + 分析时间

## 重要提示

1. **真实可信**：只输出代码中存在的技术点
2. **量化数据**：提取具体数字（线程池大小、缓存超时等）
3. **验证优先**：每个亮点必须有文件路径+行号

## 参考资料

简历写法详见 `references/` 目录
