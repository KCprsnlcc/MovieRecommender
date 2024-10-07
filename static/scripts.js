// scripts.js

document.addEventListener('DOMContentLoaded', () => {
        const themeToggle = document.getElementById('theme-toggle');
        const colorBlindToggle = document.getElementById('color-blind-toggle');
    
        // Load saved theme from localStorage
        const savedTheme = localStorage.getItem('theme');
        if (savedTheme) {
            document.body.classList.add(savedTheme);
        }
    
        updateThemeButton();
        updateColorBlindButton();
    
        // Event listener for theme toggle
        themeToggle.addEventListener('click', () => {
            if (document.body.classList.contains('dark-mode')) {
                document.body.classList.remove('dark-mode');
                localStorage.setItem('theme', '');
            } else {
                document.body.classList.add('dark-mode');
                document.body.classList.remove('color-blind-mode');
                localStorage.setItem('theme', 'dark-mode');
            }
            updateThemeButton();
        });
    
        // Event listener for color blind mode toggle
        colorBlindToggle.addEventListener('click', () => {
            if (document.body.classList.contains('color-blind-mode')) {
                document.body.classList.remove('color-blind-mode');
                localStorage.setItem('theme', '');
            } else {
                document.body.classList.add('color-blind-mode');
                document.body.classList.remove('dark-mode');
                localStorage.setItem('theme', 'color-blind-mode');
            }
            updateColorBlindButton();
        });
    
        function updateThemeButton() {
            if (document.body.classList.contains('dark-mode')) {
                themeToggle.textContent = 'Switch to Light Mode';
            } else {
                themeToggle.textContent = 'Switch to Dark Mode';
            }
        }
    
        function updateColorBlindButton() {
            if (document.body.classList.contains('color-blind-mode')) {
                colorBlindToggle.textContent = 'Disable Color Blind Mode';
            } else {
                colorBlindToggle.textContent = 'Enable Color Blind Mode';
            }
        }
    });
    document.addEventListener('DOMContentLoaded', function() {
        const searchInput = document.getElementById('search-input');
        if (searchInput) {
            const movieList = document.getElementById('movie-list');
            const movieCards = movieList.querySelectorAll('.movie-card');
    
            searchInput.addEventListener('keyup', function() {
                const filter = searchInput.value.toLowerCase();
    
                movieCards.forEach(function(card) {
                    const title = card.querySelector('h3').textContent.toLowerCase();
                    if (title.includes(filter)) {
                        card.style.display = '';
                    } else {
                        card.style.display = 'none';
                    }
                });
            });
        }
    });
    