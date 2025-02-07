document.addEventListener('DOMContentLoaded', function() {
    // Function to duplicate items for seamless scrolling
    function duplicateItems() {
        const logoWrapper = document.querySelector('.scroll-wrapper.logos');
        const thumbnailWrapper = document.querySelector('.scroll-wrapper.thumbnails');
        
        if (logoWrapper) {
            const logoContent = logoWrapper.innerHTML;
            logoWrapper.innerHTML = logoContent + logoContent;
        }
        
        if (thumbnailWrapper) {
            const thumbnailContent = thumbnailWrapper.innerHTML;
            thumbnailWrapper.innerHTML = thumbnailContent + thumbnailContent;
        }
    }
    
    // Call the function when the page loads
    duplicateItems();

    // Pause animations on hover
    const scrollWrappers = document.querySelectorAll('.scroll-wrapper');
    scrollWrappers.forEach(wrapper => {
        wrapper.addEventListener('mouseenter', () => {
            wrapper.style.animationPlayState = 'paused';
        });
        
        wrapper.addEventListener('mouseleave', () => {
            wrapper.style.animationPlayState = 'running';
        });
    });
});
