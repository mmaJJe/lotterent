function init() {
    const input = document.querySelector('input');

    input.addEventListener('focus', () => {
        input.placeholder = ''        
    });
    input.addEventListener('blur', () => {
        input.placeholder = '검색어를 입력하세요'
    })
}

init();