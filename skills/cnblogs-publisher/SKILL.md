---
name: cnblogs-publisher
description: 发布博客到博客园（cnblogs.com）。当用户需要向博客园发布文章、编辑文章、删除文章、上传图片、获取分类列表，或请求将 Markdown/内容发布到博客园时触发。
---

# CNBlogs Publisher

通过 MetaWeblog API 将文章发布到博客园。

## 配置管理

首次使用自动提示输入以下配置，保存到 `~/.cnblogs_config`：

- **api_url**: `https://rpc.cnblogs.com/metaweblog/account`
- **blog_id**: 博客园后台 -> 管理 -> 设置 -> 博客接口 获取
- **username**: 博客园用户名
- **token**: 博客园后台获取的密钥

### 更新配置

```bash
# 删除旧配置后重新输入
rm ~/.cnblogs_config
```

## 发布文章

### 直接发布

用户提供文章标题和内容后，直接调用 `scripts/publish.py`：

```bash
python scripts/publish.py new --title "标题" --content "内容" [--categories "分类1,分类2"]
```

### 带文件发布

文章内容在文件中时：

```bash
python scripts/publish.py new --title "标题" --file ./post.md [--categories "技术,Python"]
```

### 常用 categories

查看可用分类：

```bash
python scripts/publish.py categories
```

### 上传图片

```bash
python scripts/publish.py upload --file ./image.png
```

## 编辑文章

```bash
python scripts/publish.py edit --post-id <文章ID> --title "新标题" --content "新内容"
```

## 删除文章

```bash
python scripts/publish.py delete --post-id <文章ID>
```

## 获取文章列表

```bash
python scripts/publish.py recent --count 10
```

## 完整 API 参考

见 [references/MetaWeblog.md](references/MetaWeblog.md)

## 注意事项

- **XML 转义**: 内容中的 `&`、`<`、`>`、`"`、`'` 会自动转义
- **Token 过期**: 如发布失败提示认证错误，删除 `~/.cnblogs_config` 重新配置
- **重复标题**: 博客园允许重复标题，但建议保持唯一
- **分类不存在**: 会自动使用默认分类
- **Windows 兼容**: 使用 Python 脚本，跨平台兼容
