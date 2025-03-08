document.addEventListener('DOMContentLoaded', function () {
    const galleryGrid = document.getElementById('gallery-grid');
    const modal = document.getElementById('image-modal');
    const modalImg = document.getElementById('modal-image');
    const closeBtn = document.querySelector('.close');

    // 图片文件名列表（假设图片命名为 gallery1.jpg, gallery2.jpg, ...）
    const imageFiles = [
        '1.jpg',
        '2.jpg',
        '3.jpg',
        '4.jpg',
        '5.jpg',
        '6.jpg'
    ];

    // 动态加载图片
    imageFiles.forEach((file, index) => {
        const imgPath = `images/${file}`; // 图片路径
        const galleryItem = document.createElement('div');
        galleryItem.className = 'gallery-item';

        const img = document.createElement('img');
        img.src = imgPath;
        img.alt = `Gallery Image ${index + 1}`;
        img.className = 'gallery-image';

        // 点击图片显示模态框
        img.addEventListener('click', function () {
            modal.style.display = 'block';
            modalImg.src = this.src;
        });

        galleryItem.appendChild(img);
        galleryGrid.appendChild(galleryItem);
    });

    // 点击关闭按钮隐藏模态框
    closeBtn.addEventListener('click', function () {
        modal.style.display = 'none';
    });

    // 点击模态框外部隐藏模态框
    modal.addEventListener('click', function (event) {
        if (event.target === modal) {
            modal.style.display = 'none';
        }
    });
});
