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

    // Smooth Scroll to Preferences and Hide Hero Section
    const heroBtn = document.querySelector('#get-started-btn');
    if (heroBtn) {
        heroBtn.addEventListener('click', function(e) {
            e.preventDefault();
            document.querySelector('#preferences').scrollIntoView({ behavior: 'smooth' });
            // Hide hero section after click
            const heroSection = document.querySelector('.hero');
            if (heroSection) {
                heroSection.style.display = 'none';
            }
        });
    }
     // Star Rating Interaction
     const starRating = document.querySelector('.star-rating');
     if (starRating) {
         const stars = starRating.querySelectorAll('i');
         const ratingValue = document.getElementById('rating-value');
 
         stars.forEach((star) => {
             star.addEventListener('click', () => {
                 const rating = parseInt(star.getAttribute('data-value'));
                 ratingValue.value = rating;
 
                 // Remove 'bxs-star' and 'selected' classes from all stars, add 'bx-star'
                 stars.forEach((s) => {
                     s.classList.remove('bxs-star', 'selected');
                     s.classList.add('bx-star');
                 });
 
                 // Add 'bxs-star' and 'selected' classes to selected stars
                 for (let i = 0; i < rating; i++) {
                     stars[i].classList.remove('bx-star');
                     stars[i].classList.add('bxs-star', 'selected');
                 }
             });
 
             star.addEventListener('mouseover', () => {
                 const rating = parseInt(star.getAttribute('data-value'));
 
                 // Highlight stars on hover
                 stars.forEach((s, index) => {
                     if (index < rating) {
                         s.classList.add('bxs-star');
                         s.classList.remove('bx-star');
                     } else {
                         s.classList.add('bx-star');
                         s.classList.remove('bxs-star');
                     }
                 });
             });
 
             star.addEventListener('mouseout', () => {
                 // Reset stars to the selected rating
                 const selectedRating = parseInt(ratingValue.value) || 0;
                 stars.forEach((s, index) => {
                     if (index < selectedRating) {
                         s.classList.add('bxs-star');
                         s.classList.remove('bx-star');
                     } else {
                         s.classList.add('bx-star');
                         s.classList.remove('bxs-star');
                     }
                 });
             });
         });
     }
});
