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
    <title data-lang="title">鲲鹏创客社</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <link rel="stylesheet" href="../css/styles.css">
    <link rel="stylesheet" href="../css/floatbar.css">
    <link rel="stylesheet" href="../css/blog-detail.css">
</head>
<body>
    <header>
        <div class="container">
            <h1 data-lang="header-title">鲲鹏创客社</h1>
            <nav>
                <ul>
                    <li><a href="../index.html" data-lang="nav-about">关于我们</a></li>
                    <li><a href="../index.html#events" data-lang="nav-events">活动</a></li>
                    <li><a href="../index.html#members" data-lang="nav-members">成员</a></li>
                    <li><a href="../index.html#contact" data-lang="nav-contact">联系我们</a></li>
                    <li><a href="../blog.html" data-lang="nav-blog">博客</a></li>
                    <li><a href="../gallery.html" data-lang="nav-gallery">相册</a></li>
                </ul>
            </nav>
        </div>
    </header>

    <section class="section">
        <div class="container">
            <div id="blog-post">
                {content}
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
    将 Markdown 文件转换为 HTML 文件
    """
    with open(md_file, 'r', encoding='utf-8') as md:
        markdown_content = md.read()
    
    # 使用 markdown 库将 Markdown 转换为 HTML
    html_content = markdown.markdown(markdown_content)

    # 使用 BeautifulSoup 美化 HTML 内容
    soup = BeautifulSoup(html_content, 'html.parser')
    prettified_html = soup.prettify()

    # 将 HTML 内容插入模板
    title = os.path.splitext(os.path.basename(md_file))[0]
    final_html = BLOG_TEMPLATE.format(title=title, content=prettified_html)

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
