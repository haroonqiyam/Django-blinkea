document.addEventListener('DOMContentLoaded', function() {
    // Function to duplicate items for seamless scrolling
    function duplicateItems() {
        const scrollWrappers = document.querySelectorAll('.scroll-wrapper');
        
        scrollWrappers.forEach(wrapper => {
            const items = wrapper.innerHTML;
            wrapper.innerHTML = items + items; // Duplicate content for seamless scroll
        });
    }
    
    // Function to handle scroll pause on hover
    function handleScrollPause() {
        const scrollWrappers = document.querySelectorAll('.scroll-wrapper');
        
        scrollWrappers.forEach(wrapper => {
            wrapper.addEventListener('mouseenter', () => {
                wrapper.style.animationPlayState = 'paused';
            });
            
            wrapper.addEventListener('mouseleave', () => {
                wrapper.style.animationPlayState = 'running';
            });
        });
    }

    // Initialize
    duplicateItems();
    handleScrollPause();
});
