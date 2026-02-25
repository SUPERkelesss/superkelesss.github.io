import re
import time
import logging

logger = logging.getLogger("mkdocs.hooks.css_cache_bust")
logger.info("hook - css_cache_bust is loaded")

def on_post_page(output, page, config, **kwargs):
    """为本地CSS链接添加版本查询参数"""
    # 使用构建时间戳作为版本号
    version = str(int(time.time()))

    # 匹配 href 属性，支持引号或没有引号，支持相对路径如 ../stylesheets/extra.css
    # 仅匹配 stylesheets/ 目录下的CSS文件，忽略 assets/stylesheets/ 等
    # 匹配 href=["']?((?:\.\./)*stylesheets/[^"'\s>]+\.css)["']?
    pattern = r'(href=)(["\']?)((?:\.\./)*stylesheets/[^"\' >]+\.css)(["\']?)'

    def replace_css_link(match):
        href_prefix = match.group(1)  # "href="
        open_quote = match.group(2)   # optional opening quote
        css_path = match.group(3)     # CSS file path (may contain ../)
        close_quote = match.group(4)  # optional closing quote
        # 如果已经包含查询参数，跳过（避免重复添加）
        if '?' in css_path:
            return match.group(0)
        # 添加查询参数
        return f'{href_prefix}{open_quote}{css_path}?v={version}{close_quote}'

    output = re.sub(pattern, replace_css_link, output)
    logger.debug(f"为CSS链接添加版本参数: v={version}")

    return output