#!/usr/bin/env python3
"""CNBlogs Publisher - MetaWeblog API client for cnblogs.com"""

import xmlrpc.client
import os
import sys
import argparse
from pathlib import Path
from datetime import datetime
import base64
import mistune

CONFIG_FILE = Path.home() / ".cnblogs_config"


def load_config():
    """Load configuration from ~/.cnblogs_config"""
    if not CONFIG_FILE.exists():
        return None
    config = {}
    with open(CONFIG_FILE, encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if "=" in line and not line.startswith("#"):
                key, value = line.split("=", 1)
                config[key.strip()] = value.strip().strip('"').strip("'")
    return config


def save_config(api_url, blog_id, username, token):
    """Save configuration to ~/.cnblogs_config"""
    with open(CONFIG_FILE, "w", encoding='utf-8') as f:
        f.write(f'api_url="{api_url}"\n')
        f.write(f'blog_id="{blog_id}"\n')
        f.write(f'username="{username}"\n')
        f.write(f'token="{token}"\n')
    print(f"Configuration saved to {CONFIG_FILE}")


def get_config_interactive():
    """Prompt user for configuration"""
    print("First time setup - please enter your cnblogs credentials:")
    api_url = input("API URL (https://rpc.cnblogs.com/metaweblog/用户名): ").strip()
    blog_id = input("Blog ID: ").strip()
    username = input("Username: ").strip()
    token = input("Token: ").strip()

    if not all([api_url, blog_id, username, token]):
        print("Error: All fields are required")
        sys.exit(1)

    save_config(api_url, blog_id, username, token)
    return {"api_url": api_url, "blog_id": blog_id, "username": username, "token": token}


def get_client(config):
    """Create XML-RPC client"""
    return xmlrpc.client.ServerProxy(config["api_url"], allow_none=True)


def extract_title_from_markdown(content):
    """Extract title from Markdown content (first # heading)"""
    lines = content.strip().split('\n')
    for line in lines:
        line = line.strip()
        if line.startswith('# '):
            return line[2:].strip()
    return None


def escape_xml(s):
    """Escape special XML characters"""
    if s is None:
        return ""
    s = str(s)
    s = s.replace("&", "&amp;")
    s = s.replace("<", "&lt;")
    s = s.replace(">", "&gt;")
    s = s.replace('"', "&quot;")
    s = s.replace("'", "&apos;")
    return s


def cmd_new(args, config):
    """Publish a new post"""
    client = get_client(config)

    # Read content from file if specified
    if args.file:
        with open(args.file, "r", encoding="utf-8") as f:
            original_content = f.read()
        # Convert Markdown to HTML if file is .md
        if args.file.lower().endswith('.md'):
            content = mistune.html(original_content)
            # Auto-extract title from Markdown if not provided
            if not args.title:
                args.title = extract_title_from_markdown(original_content)
        else:
            content = original_content
    else:
        content = args.content

    if not args.title:
        print("Error: --title is required when publishing without a Markdown file")
        sys.exit(1)

    categories = args.categories.split(",") if args.categories else []

    post = {
        "title": args.title,
        "description": content,
        "dateCreated": datetime.utcnow().strftime("%Y%m%dT%H:%M:%S"),
    }
    if categories:
        post["categories"] = categories

    result = client.metaWeblog.newPost(
        config["blog_id"],
        config["username"],
        config["token"],
        post,
        True
    )
    print(f"Post published successfully! Post ID: {result}")
    return result


def cmd_edit(args, config):
    """Edit an existing post"""
    client = get_client(config)

    if args.file:
        with open(args.file, "r", encoding="utf-8") as f:
            original_content = f.read()
        # Convert Markdown to HTML if file is .md
        if args.file.lower().endswith('.md'):
            content = mistune.html(original_content)
            # Auto-extract title from Markdown if not provided
            if not args.title:
                args.title = extract_title_from_markdown(original_content)
        else:
            content = original_content
    else:
        content = args.content

    if not args.title:
        print("Error: --title is required when editing without a Markdown file")
        sys.exit(1)

    post = {"title": args.title, "description": content}

    result = client.metaWeblog.editPost(
        args.post_id,
        config["username"],
        config["token"],
        post,
        True
    )
    print(f"Post updated successfully!")
    return result


def cmd_delete(args, config):
    """Delete a post"""
    client = get_client(config)
    result = client.blogger.deletePost(
        "",
        args.post_id,
        config["username"],
        config["token"],
        True
    )
    print(f"Post deleted successfully!" if result else "Delete failed")
    return result


def cmd_categories(args, config):
    """List all categories"""
    client = get_client(config)
    categories = client.metaWeblog.getCategories(
        config["blog_id"],
        config["username"],
        config["token"]
    )
    print("Available categories:")
    for cat in categories:
        print(f"  - {cat['title']} (id: {cat['categoryid']})")
    return categories


def cmd_upload(args, config):
    """Upload a media file"""
    client = get_client(config)

    file_path = Path(args.file)
    if not file_path.exists():
        print(f"Error: File not found: {args.file}")
        sys.exit(1)

    with open(file_path, "rb") as f:
        bits = base64.b64encode(f.read()).decode()

    name = file_path.name
    mime_type = {
        ".png": "image/png",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".gif": "image/gif",
        ".svg": "image/svg+xml",
    }.get(file_path.suffix.lower(), "application/octet-stream")

    file_data = {"bits": bits, "name": name, "type": mime_type}

    result = client.metaWeblog.newMediaObject(
        config["blog_id"],
        config["username"],
        config["token"],
        file_data
    )
    print(f"File uploaded: {result['url']}")
    return result


def cmd_recent(args, config):
    """Get recent posts"""
    client = get_client(config)
    posts = client.metaWeblog.getRecentPosts(
        config["blog_id"],
        config["username"],
        config["token"],
        args.count
    )
    print(f"Recent {len(posts)} posts:")
    for post in posts:
        print(f"  [{post['postid']}] {post['title']} - {post.get('dateCreated', 'N/A')}")
    return posts


def cmd_get_post(args, config):
    """Get a single post by ID"""
    client = get_client(config)
    post = client.metaWeblog.getPost(
        args.post_id,
        config["username"],
        config["token"]
    )
    print(f"Title: {post.get('title', 'N/A')}")
    print(f"PostId: {post.get('postid', 'N/A')}")
    print(f"DateCreated: {post.get('dateCreated', 'N/A')}")
    if post.get('categories'):
        print(f"Categories: {', '.join(post.get('categories', []))}")
    print(f"Description length: {len(str(post.get('description', '')))} chars")
    return post


def cmd_get_blogs(args, config):
    """Get user's blog list"""
    client = get_client(config)
    blogs = client.blogger.getUsersBlogs(
        "appkey",
        config["username"],
        config["token"]
    )
    print("Your blogs:")
    for blog in blogs:
        print(f"  BlogId: {blog.get('blogid', 'N/A')}")
        print(f"  URL: {blog.get('url', 'N/A')}")
        print(f"  BlogName: {blog.get('blogName', 'N/A')}")
        print()
    return blogs


def cmd_new_category(args, config):
    """Create a new category"""
    client = get_client(config)
    category_info = {"name": args.name}
    if args.description:
        category_info["description"] = args.description
    if args.slug:
        category_info["slug"] = args.slug
    if args.parent_id:
        category_info["parent_id"] = args.parent_id

    new_id = client.wp.newCategory(
        config["blog_id"],
        config["username"],
        config["token"],
        category_info
    )
    print(f"Category created successfully! Category ID: {new_id}")
    return new_id


def main():
    parser = argparse.ArgumentParser(description="CNBlogs Publisher")
    subparsers = parser.add_subparsers(dest="command", help="Commands")

    # new command
    p_new = subparsers.add_parser("new", help="Publish a new post")
    p_new.add_argument("--title", required=True, help="Post title")
    p_new.add_argument("--content", help="Post content")
    p_new.add_argument("--file", help="File containing post content")
    p_new.add_argument("--categories", help="Comma-separated categories")

    # edit command
    p_edit = subparsers.add_parser("edit", help="Edit an existing post")
    p_edit.add_argument("--post-id", required=True, help="Post ID to edit")
    p_edit.add_argument("--title", help="New title")
    p_edit.add_argument("--content", help="New content")
    p_edit.add_argument("--file", help="File containing post content")

    # delete command
    p_delete = subparsers.add_parser("delete", help="Delete a post")
    p_delete.add_argument("--post-id", required=True, help="Post ID to delete")

    # categories command
    subparsers.add_parser("categories", help="List all categories")

    # upload command
    p_upload = subparsers.add_parser("upload", help="Upload a media file")
    p_upload.add_argument("--file", required=True, help="File to upload")

    # recent command
    p_recent = subparsers.add_parser("recent", help="Get recent posts")
    p_recent.add_argument("--count", type=int, default=10, help="Number of posts")

    # get-post command
    p_get_post = subparsers.add_parser("get-post", help="Get a single post by ID")
    p_get_post.add_argument("--post-id", required=True, help="Post ID to retrieve")

    # get-blogs command
    subparsers.add_parser("get-blogs", help="Get user's blog list")

    # new-category command
    p_new_cat = subparsers.add_parser("new-category", help="Create a new category")
    p_new_cat.add_argument("--name", required=True, help="Category name")
    p_new_cat.add_argument("--description", help="Category description")
    p_new_cat.add_argument("--slug", help="Category slug (URL alias)")
    p_new_cat.add_argument("--parent-id", type=int, help="Parent category ID")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(1)

    # Load or setup config
    config = load_config()
    if not config:
        config = get_config_interactive()

    # Execute command
    if args.command == "new":
        if not args.content and not args.file:
            print("Error: Either --content or --file is required")
            sys.exit(1)
        cmd_new(args, config)
    elif args.command == "edit":
        if not args.content and not args.file:
            print("Error: Either --content or --file is required")
            sys.exit(1)
        # For edit, if only content is provided without file, title is also required
        if args.content and not args.file and not args.title:
            print("Error: --title is required when editing with --content")
            sys.exit(1)
        cmd_edit(args, config)
    elif args.command == "delete":
        cmd_delete(args, config)
    elif args.command == "categories":
        cmd_categories(args, config)
    elif args.command == "upload":
        cmd_upload(args, config)
    elif args.command == "recent":
        cmd_recent(args, config)
    elif args.command == "get-post":
        cmd_get_post(args, config)
    elif args.command == "get-blogs":
        cmd_get_blogs(args, config)
    elif args.command == "new-category":
        cmd_new_category(args, config)


if __name__ == "__main__":
    main()
