import os
import markdown
from bs4 import BeautifulSoup

# 定义 Markdown 文件目录和 HTML 输出目录
MD_DIR = 'blogs'  # Markdown 文件存放目录
HTML_DIR = 'blog-detail'  # HTML 文件输出目录

# 确保输出目录存在
if not os.path.exists(HTML_DIR):
    os.makedirs(HTML_DIR)

# 定义博客详情页面的 HTML 模板
BLOG_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <link rel="stylesheet" href="../css/styles.css">
    <link rel="stylesheet" href="../css/blog-detail.css">
    <link rel="stylesheet" href="../css/floatbar.css">
</head>
<body>
    <header>
        <div class="container">
            <h1>鲲鹏创客社</h1>
            <nav>
                <ul>
                    <li><a href="../index.html">关于我们</a></li>
                    <li><a href="../index.html#events">活动</a></li>
                    <li><a href="../index.html#members">成员</a></li>
                    <li><a href="../index.html#contact">联系我们</a></li>
                    <li><a href="../blog.html">博客</a></li>
                    <li><a href="../gallery.html">相册</a></li>
                </ul>
            </nav>
        </div>
    </header>

    <section class="section">
        <div class="container">
            <div class="blog-layout">
                <!-- 左侧目录 -->
                <div class="toc-sidebar" id="toc-sidebar">
                    <h3>目录</h3>
                    {toc}
                </div>
                <!-- 右侧博客内容 -->
                <div class="blog-content" id="blog-detail">
                    {content}
                </div>
            </div>
        </div>
    </section>

    <footer>
        <div class="container">
            <p>&copy; 2023 鲲鹏创客社. 保留所有权利。</p>
        </div>
    </footer>
    <div class="float-sidebar">
        <div class="language-switcher">
            <select id="language-switcher">
                <option value="en">🌐 English</option>
                <option value="zh-CN">🌐 简体中文</option>
                <option value="zh-TW">🌐 繁体中文</option>
            </select>
        </div>
        <div class="theme-switcher">
            <select id="theme-switcher">
                <option value="default" data-lang="theme-default">🌞 默认主题</option>
                <option value="dark" data-lang="theme-dark">🌙 暗色主题</option>
                <option value="blue" data-lang="theme-blue">🔵 蓝色主题</option>
            </select>
        </div>
        <div class="back-to-top" id="back-to-top">↑</div>
    </div>

    <script src="../js/script.js"></script>
    <script src="../js/language.js"></script>
    <script src="../js/theme.js"></script>
</body>
</html>
'''

def convert_md_to_html(md_file, html_file):
    """
    将 Markdown 文件转换为 HTML 文件，并生成目录
    """
    with open(md_file, 'r', encoding='utf-8') as md:
        markdown_content = md.read()
    
    # 使用 markdown 库将 Markdown 转换为 HTML，并启用 TOC 扩展
    md_extensions = [
        'toc',  # 启用目录扩展
        'fenced_code',  # 支持代码块
        'tables',  # 支持表格
    ]
    html_content = markdown.markdown(
        markdown_content,
        extensions=md_extensions
    )

    # 使用 BeautifulSoup 解析 HTML 内容
    soup = BeautifulSoup(html_content, 'html.parser')

    # 提取目录
    toc = soup.find('div', class_='toc')
    if toc:
        # 从正文中移除目录
        toc.extract()
        toc_html = str(toc)
    else:
        # 如果没有目录，生成一个空的目录占位符
        toc_html = '<p>No table of contents available.</p>'

    # 将目录和内容插入到模板中
    final_html = BLOG_TEMPLATE.format(
        title=os.path.splitext(os.path.basename(md_file))[0],
        toc=toc_html,
        content=str(soup)  # 使用移除目录后的内容
    )

    # 写入 HTML 文件
    with open(html_file, 'w', encoding='utf-8') as html_output:
        html_output.write(final_html)

def convert_all_md_to_html():
    """
    将指定目录下的所有 Markdown 文件转换为 HTML 文件
    """
    for filename in os.listdir(MD_DIR):
        if filename.endswith('.md'):
            md_file = os.path.join(MD_DIR, filename)
            html_file = os.path.join(HTML_DIR, filename.replace('.md', '.html'))
            convert_md_to_html(md_file, html_file)
            print(f"Converted {md_file} to {html_file}")

if __name__ == '__main__':
    convert_all_md_to_html()
