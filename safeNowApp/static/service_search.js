document.addEventListener('DOMContentLoaded', () => {
    const searchInput = document.querySelector('input[name="search"]');
    const categorySelect = document.querySelector('select[name="category"]');
    const servicesContainer = document.querySelector('.grid'); // your grid container

    function fetchServices() {
        const search = searchInput.value;
        console.log(search);
        const category = categorySelect.value;

        fetch(`/filter_services/?search=${encodeURIComponent(search)}&category=${encodeURIComponent(category)}`)
            .then(res => res.json())
            .then(data => {
                servicesContainer.innerHTML = data.html;
            })
            .catch(err => console.error('Error:', err));
    }

    searchInput.addEventListener('input', fetchServices);
    categorySelect.addEventListener('change', fetchServices);
});
