document.addEventListener('DOMContentLoaded', function() {
    const themeSwitcher = document.getElementById('theme-switcher');

    // 加载保存的主题
    function loadTheme() {
        const savedTheme = localStorage.getItem('preferredTheme') || 'default';
        themeSwitcher.value = savedTheme;
        document.body.className = `${savedTheme}-theme`;
    }

    // 切换主题
    themeSwitcher.addEventListener('change', function() {
        const selectedTheme = this.value;
        document.body.className = `${selectedTheme}-theme`;
        localStorage.setItem('preferredTheme', selectedTheme);
    });

    // 初始化主题
    loadTheme();
});
