 document.addEventListener('DOMContentLoaded', () => {
            const searchInput = document.querySelector('input[placeholder="🔍 Search cases..."]');
            const levelSelect = document.querySelector('select[name="level"]');
            const categorySelect = document.querySelector('select[name="category"]');
            const casesContainer = document.querySelector('main');

            function fetchCases() {
                const search = searchInput.value;
                const level = levelSelect.value;
                const category = categorySelect.value;

                fetch(`/filter_cases/?search=${encodeURIComponent(search)}&level=${encodeURIComponent(level)}&category=${encodeURIComponent(category)}`)
                    .then(res => res.json())
                    .then(data => {
                        casesContainer.innerHTML = data.html;
                    })
                    .catch(err => console.error('Error:', err));
            }

            searchInput.addEventListener('input', fetchCases);
            levelSelect.addEventListener('change', fetchCases);
            categorySelect.addEventListener('change', fetchCases);
        });