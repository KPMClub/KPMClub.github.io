document.addEventListener('DOMContentLoaded', function() {
    const languageSwitcher = document.getElementById('language-switcher');
    const themeSwitcher = document.getElementById('theme-switcher');
    const elements = document.querySelectorAll('[data-lang]');

    // 加载语言
    function loadLanguage(lang) {
        fetch(`lang/${lang}.json?t=${new Date().getTime()}`)
            .then(response => {
                if (!response.ok) {
                    throw new Error(`Failed to load language file: ${response.statusText}`);
                }
                return response.json();
            })
            .then(data => {
                // 更新所有带有 data-lang 属性的元素
                elements.forEach(element => {
                    const key = element.getAttribute('data-lang');
                    if (data[key]) {
                        element.textContent = data[key];
                    }
                });

                // 更新主题选择器的选项文本
                const themeOptions = themeSwitcher.querySelectorAll('option');
                themeOptions.forEach(option => {
                    const themeKey = option.getAttribute('data-lang');
                    if (data[themeKey]) {
                        option.textContent = data[themeKey];
                    }
                });

                // 保存用户选择的语言
                localStorage.setItem('preferredLanguage', lang);
            })
            .catch(error => {
                console.error('Error loading language file:', error);
            });
    }

    // 切换语言
    languageSwitcher.addEventListener('change', function() {
        const selectedLang = this.value;
        loadLanguage(selectedLang);
    });

    // 设置默认语言
    function setDefaultLanguage() {
        const savedLanguage = localStorage.getItem('preferredLanguage');
        const browserLanguage = navigator.language || 'en';
        const defaultLanguage = savedLanguage || (browserLanguage.startsWith('zh') ? 'zh-CN' : 'en');
        languageSwitcher.value = defaultLanguage;
        loadLanguage(defaultLanguage);
    }

    // 初始化
    setDefaultLanguage();
});
