# MetaWeblog API 文档

博客园 MetaWeblog API 参考文档

## 支持的方法

| 方法 | 说明 |
|------|------|
| `blogger.deletePost` | 删除文章 |
| `blogger.getUsersBlogs` | 获取用户博客列表 |
| `metaWeblog.editPost` | 编辑文章 |
| `metaWeblog.getCategories` | 获取分类列表 |
| `metaWeblog.getPost` | 获取单篇文章 |
| `metaWeblog.getRecentPosts` | 获取最近文章 |
| `metaWeblog.newMediaObject` | 上传媒体文件 |
| `metaWeblog.newPost` | 发布新文章 |
| `wp.newCategory` | 创建分类 |

---

## blogger.deletePost

删除文章

### 参数

| 类型 | 字段 | 说明 |
|------|------|------|
| string | appKey | 可选 |
| string | postid | 文章ID |
| string | username | 用户名 |
| string | password | 密码 |
| boolean | publish | 是否重新发布 |

### 返回值

| 类型 | 说明 |
|------|------|
| boolean | 始终返回 true |

---

## blogger.getUsersBlogs

获取用户所有博客信息

### 参数

| 类型 | 字段 |
|------|------|
| string | appKey |
| string | username |
| string | password |

### 返回值

| 类型 | 说明 |
|------|------|
| array of BlogInfo | 博客信息数组 |

### BlogInfo 结构

| 字段 | 类型 | 说明 |
|------|------|------|
| blogid | string | 博客ID |
| url | string | 博客URL |
| blogName | string | 博客名称 |

---

## metaWeblog.editPost

更新已发布的文章

### 参数

| 类型 | 字段 | 说明 |
|------|------|------|
| string | postid | 文章ID |
| string | username | 用户名 |
| string | password | 密码 |
| Post | post | 文章结构 |
| boolean | publish | 是否发布 |

### 返回值

| 类型 | 说明 |
|------|------|
| any | 更新结果 |

---

## metaWeblog.getCategories

获取博客分类列表

### 参数

| 类型 | 字段 |
|------|------|
| string | blogid |
| string | username |
| string | password |

### 返回值

| 类型 | 说明 |
|------|------|
| array of CategoryInfo | 分类信息数组 |

### CategoryInfo 结构

| 字段 | 类型 | 说明 |
|------|------|------|
| description | string | 分类描述 |
| htmlUrl | string | 分类页面URL |
| rssUrl | string | 分类RSS地址 |
| title | string | 分类标题 |
| categoryid | string | 分类ID |

---

## metaWeblog.getPost

获取单篇文章

### 参数

| 类型 | 字段 |
|------|------|
| string | postid |
| string | username |
| string | password |

### 返回值

| 类型 | 说明 |
|------|------|
| Post | 文章结构 |

---

## metaWeblog.getRecentPosts

获取最近文章列表

### 参数

| 类型 | 字段 | 说明 |
|------|------|------|
| string | blogid | 博客ID |
| string | username | 用户名 |
| string | password | 密码 |
| integer | numberOfPosts | 获取数量 |

### 返回值

| 类型 | 说明 |
|------|------|
| array of Post | 文章数组 |

---

## metaWeblog.newMediaObject

上传媒体文件

### 参数

| 类型 | 字段 | 说明 |
|------|------|------|
| string | blogid | 博客ID |
| string | username | 用户名 |
| string | password | 密码 |
| FileData | file | 文件数据 |

### FileData 结构

| 字段 | 类型 | 说明 |
|------|------|------|
| bits | base64 | 文件内容（Base64编码） |
| name | string | 文件名 |
| type | string | MIME类型 |

### 返回值

| 类型 | 说明 |
|------|------|
| UrlData | URL信息 |

### UrlData 结构

| 字段 | 类型 |
|------|------|
| url | string |

---

## metaWeblog.newPost

发布新文章

### 参数

| 类型 | 字段 | 说明 |
|------|------|------|
| string | blogid | 博客ID |
| string | username | 用户名 |
| string | password | 密码 |
| Post | post | 文章结构 |
| boolean | publish | 是否立即发布 |

### 返回值

| 类型 | 说明 |
|------|------|
| string | 新文章ID |

---

## wp.newCategory

创建新分类

### 参数

| 类型 | 字段 | 说明 |
|------|------|------|
| string | blog_id | 博客ID |
| string | username | 用户名 |
| string | password | 密码 |
| WpCategory | category | 分类信息 |

### WpCategory 结构

| 字段 | 类型 | 说明 |
|------|------|------|
| name | string | 分类名称 |
| slug | string | URL别名（可选） |
| parent_id | integer | 父分类ID |
| description | string | 分类描述（可选） |

### 返回值

| 类型 | 说明 |
|------|------|
| integer | 新分类ID |

---

## Post 结构

发布文章时使用的主要数据结构

| 字段 | 类型 | 说明 |
|------|------|------|
| dateCreated | dateTime | 创建时间（ISO 8601格式） |
| description | string | 文章正文（HTML内容） |
| title | string | 文章标题 |
| categories | array of string | 分类数组（可选） |
| enclosure | Enclosure | 附件信息（可选） |
| link | string | 文章链接（可选） |
| permalink | string | 永久链接（可选） |
| postid | any | 文章ID（可选） |
| source | Source | 来源信息（可选） |
| userid | string | 用户ID（可选） |
| mt_allow_comments | any | 是否允许评论（可选） |
| mt_allow_pings | any | 是否允许引用通告（可选） |
| mt_convert_breaks | any | 转换换行符（可选） |
| mt_text_more | string | "阅读更多"内容（可选） |
| mt_excerpt | string | 文章摘要（可选） |
| mt_keywords | string | 文章关键词（可选） |
| wp_slug | string | URL别名（可选） |

---

## Enclosure 结构

| 字段 | 类型 | 说明 |
|------|------|------|
| length | integer | 文件大小（可选） |
| type | string | MIME类型（可选） |
| url | string | 文件URL（可选） |

---

## Source 结构

| 字段 | 类型 | 说明 |
|------|------|------|
| name | string | 来源名称（可选） |
| url | string | 来源URL（可选） |

---

## 调用示例

### 新建文章 (newPost)

```xml
<?xml version="1.0" encoding="UTF-8"?>
<methodCall>
  <methodName>metaWeblog.newPost</methodName>
  <params>
    <!-- 参数1：c -->
    <param>
      <value><string>account</string></value>
    </param>
    <!-- 参数2：username -->
    <param>
      <value><string>username</string></value>
    </param>
    <!-- 参数3：password（可使用 MetaWeblog 访问令牌更安全） -->
    <param>
      <value><string>token</string></value>
    </param>
    <!-- 参数4：Post 结构体，这是请求的核心内容 -->
    <param>
      <value>
        <struct>
          <!-- title（标题），文档注明为 Required -->
          <member>
            <name>title</name>
            <value><string>我的第一篇 MetaWeblog API 测试文章</string></value>
          </member>
          <!-- description（正文内容），文档注明为 Required -->
          <member>
            <name>description</name>
            <value><string>这是一篇通过 MetaWeblog API 接口发布的技术测试文章。</string></value>
          </member>
          <!-- dateCreated（发布日期时间），文档注明为 Required -->
          <member>
            <name>dateCreated</name>
            <value><dateTime.iso8601>2026-02-24T15:30:00</dateTime.iso8601></value>
          </member>
          <!-- categories（分类，可选） -->
          <member>
            <name>categories</name>
            <value>
              <array>
                <data>
                  <value><string>技术</string></value>
                  <value><string>API</string></value>
                </data>
              </array>
            </value>
          </member>
          <!-- mt_keywords（标签，可选） -->
          <member>
            <name>mt_keywords</name>
            <value><string>MetaWeblog, XML-RPC, 博客园</string></value>
          </member>
        </struct>
      </value>
    </param>
    <!-- 参数5：publish（是否立即发布） -->
    <param>
      <value><boolean>1</boolean></value> <!-- 1 表示 true（立即发布），0 表示 false（保存为草稿） -->
    </param>
  </params>
</methodCall>
```

### 编辑文章 (editPost)

```xml
<?xml version="1.0" encoding="UTF-8"?>
<methodCall>
  <methodName>metaWeblog.editPost</methodName>
  <params>
    <param><value><string>文章ID</string></value></param>
    <param><value><string>用户名</string></value></param>
    <param><value><string>密码</string></value></param>
    <param>
      <value>
        <struct>
          <member>
            <name>title</name>
            <value><string>更新后的标题</string></value>
          </member>
          <member>
            <name>description</name>
            <value><string>更新后的正文</string></value>
          </member>
        </struct>
      </value>
    </param>
    <param><value><boolean>1</boolean></value></param>
  </params>
</methodCall>
```

### 删除文章 (deletePost)

```xml
<?xml version="1.0" encoding="UTF-8"?>
<methodCall>
  <methodName>blogger.deletePost</methodName>
  <params>
    <param><value><string></string></value></param>
    <param><value><string>文章ID</string></value></param>
    <param><value><string>用户名</string></value></param>
    <param><value><string>密码</string></value></param>
    <param><value><boolean>1</boolean></value></param>
  </params>
</methodCall>
```

### 上传图片 (newMediaObject)

```xml
<?xml version="1.0" encoding="UTF-8"?>
<methodCall>
  <methodName>metaWeblog.newMediaObject</methodName>
  <params>
    <param><value><string>博客ID</string></value></param>
    <param><value><string>用户名</string></value></param>
    <param><value><string>密码</string></value></param>
    <param>
      <value>
        <struct>
          <member>
            <name>bits</name>
            <value><base64>文件Base64内容</base64></value>
          </member>
          <member>
            <name>name</name>
            <value><string>image.jpg</string></value>
          </member>
          <member>
            <name>type</name>
            <value><string>image/jpeg</string></value>
          </member>
        </struct>
      </value>
    </param>
  </params>
</methodCall>
```

---

## 服务信息

- 服务类型: BlogServer.Service.XmlRpc
- 版本: 1.0.0
- XmlRpc 实现: CookComputing.XmlRpcV2
- .NET 版本: 6.0
