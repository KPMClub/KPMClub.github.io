document.addEventListener('DOMContentLoaded', function () {
    const blogPostsContainer = document.getElementById('blog-posts');

    // 博客文件列表
    const blogFiles = [
        { id: 1, file: 'blogs/blog1.md', html: 'blog-detail/blog1.html' },
        { id: 2, file: 'blogs/blog2.md', html: 'blog-detail/blog2.html' },
        { id: 3, file: 'blogs/2023-10-15-How-to-Use-Markdown.md', html: 'blog-detail/2023-10-15-How-to-Use-Markdown.html' }
    ];

    // 加载并渲染博客
    blogFiles.forEach(blog => {
        fetch(blog.file)
            .then(response => {
                if (!response.ok) {
                    throw new Error(`Failed to load blog file: ${blog.file}`);
                }
                return response.text();
            })
            .then(markdown => {
                // 将 Markdown 转换为 HTML
                const html = marked.parse(markdown);

                // 创建博客文章容器
                const blogPost = document.createElement('article');
                blogPost.className = 'blog-post';

                // 提取标题和内容
                const tempDiv = document.createElement('div');
                tempDiv.innerHTML = html;
                const title = tempDiv.querySelector('h1')?.innerText || 'Untitled';
                const content = tempDiv.querySelector('p')?.innerText || 'No content available.';

                // 创建博客文章链接
                const postLink = document.createElement('a');
                postLink.href = blog.html;  // 指向 blog-detail 目录下的 HTML 文件
                postLink.innerHTML = `<h3>${title}</h3>`;
                postLink.setAttribute('data-lang', `blog-post-${blog.id}-title`);

                // 创建博客文章内容
                const postContent = document.createElement('p');
                postContent.innerText = content;
                postContent.setAttribute('data-lang', `blog-post-${blog.id}-content`);

                // 创建发布日期
                const postDate = document.createElement('p');
                postDate.innerHTML = `<small>发布日期: 2023-10-01</small>`;
                postDate.setAttribute('data-lang', `blog-post-${blog.id}-date`);

                // 将链接、内容和日期添加到博客文章容器
                blogPost.appendChild(postLink);
                blogPost.appendChild(postContent);
                blogPost.appendChild(postDate);

                // 添加到页面
                blogPostsContainer.appendChild(blogPost);
            })
            .catch(error => {
                console.error('Error loading blog:', error);
            });
    });
});
