document.addEventListener('DOMContentLoaded', function() {
    console.log('网站加载完成！');
});

document.addEventListener('DOMContentLoaded', function () {
    const backToTopButton = document.getElementById('back-to-top');

    // 显示或隐藏按钮
    window.addEventListener('scroll', function () {
        if (window.scrollY > 300) { // 当页面滚动超过 300px 时显示按钮
            backToTopButton.style.display = 'block';
        } else {
            backToTopButton.style.display = 'none';
        }
    });

    // 点击按钮返回最上方
    backToTopButton.addEventListener('click', function () {
        window.scrollTo({
            top: 0,
            behavior: 'smooth' // 平滑滚动
        });
    });
});
