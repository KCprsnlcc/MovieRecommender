document.addEventListener('DOMContentLoaded', function() {
    // Theme Toggle Logic
    const themeToggle = document.getElementById('theme-toggle');
    const currentTheme = localStorage.getItem('theme');

    if (currentTheme === 'light') {
        document.body.classList.add('light-theme');
        themeToggle.checked = true;
    }

    themeToggle.addEventListener('change', function() {
        if (this.checked) {
            document.body.classList.add('light-theme');
            localStorage.setItem('theme', 'light');
        } else {
            document.body.classList.remove('light-theme');
            localStorage.setItem('theme', 'dark');
        }
    });

    // Search Functionality
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

    // Smooth Scroll to Preferences
    const heroBtn = document.querySelector('.hero-btn');
    if (heroBtn) {
        heroBtn.addEventListener('click', function(e) {
            e.preventDefault();
            document.querySelector('#preferences').scrollIntoView({ behavior: 'smooth' });
        });
    }
});
