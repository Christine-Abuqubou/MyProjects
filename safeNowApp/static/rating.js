document.querySelectorAll('form').forEach(form => {
    const stars = form.querySelectorAll('.star');
    const ratingDisplay = form.querySelector('span[id^="rating-display"]');

    stars.forEach(star => {
        star.addEventListener('mouseenter', () => {
            const value = parseInt(star.dataset.value);
            stars.forEach(s => {
                s.classList.toggle('text-yellow-400', parseInt(s.dataset.value) <= value);
                s.classList.toggle('text-gray-300', parseInt(s.dataset.value) > value);
            });
        });

        star.addEventListener('mouseleave', () => {
            const selectedRating = parseInt(form.querySelector('input[name="rating"]').value);
            stars.forEach(s => {
                s.classList.toggle('text-yellow-400', parseInt(s.dataset.value) <= selectedRating);
                s.classList.toggle('text-gray-300', parseInt(s.dataset.value) > selectedRating);
            });
        });

        star.addEventListener('click', () => {
            const value = parseInt(star.dataset.value);
            form.querySelector('input[name="rating"]').value = value;
            if (ratingDisplay) ratingDisplay.textContent = value + '/5';
            // Submit form immediately
            form.submit();
        });
    });
});