document.addEventListener('DOMContentLoaded', function () {
    const blogPostsContainer = document.getElementById('blog-posts');

    // 博客文件列表
    const blogFiles = [
        'blogs/blog1.md',
        'blogs/blog2.md'
    ];

    // 加载并渲染博客
    blogFiles.forEach(file => {
        fetch(file)
            .then(response => {
                if (!response.ok) {
                    throw new Error(`Failed to load blog file: ${file}`);
                }
                return response.text();
            })
            .then(markdown => {
                // 将 Markdown 转换为 HTML
                const html = marked.parse(markdown);
                // 创建博客文章容器
                const blogPost = document.createElement('article');
                blogPost.className = 'blog-post';
                blogPost.innerHTML = html;
                // 添加到页面
                blogPostsContainer.appendChild(blogPost);
            })
            .catch(error => {
                console.error('Error loading blog:', error);
            });
    });
});
