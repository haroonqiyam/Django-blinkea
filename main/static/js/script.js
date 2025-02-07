document.addEventListener('DOMContentLoaded', () => {
    const scrollWrappers = document.querySelectorAll('.scroll-wrapper');

    scrollWrappers.forEach(wrapper => {
        const isThumbnails = wrapper.classList.contains('thumbnails');
        const speed = wrapper.dataset.speed || 15; // Default animation speed
        const gap = 20; // Gap between items (matches CSS)

        // Duplicate content to create a seamless loop
        const content = wrapper.innerHTML;
        wrapper.innerHTML += content; // Duplicate the content for seamless looping

        // Set animation speed dynamically
        wrapper.style.setProperty('--scroll-speed', `${speed}s`);
        wrapper.style.animation = `scroll var(--scroll-speed, ${speed}s) linear infinite`;

        if (isThumbnails) {
            const images = wrapper.querySelectorAll('img');

            // Dynamically calculate thumbnail width or fallback to minimum width
            const minThumbnailWidth = 400; // Minimum width for thumbnails
            const thumbnailWidth = Math.max(wrapper.dataset.width || minThumbnailWidth, minThumbnailWidth);

            // Update thumbnail widths
            images.forEach(img => {
                img.style.width = `${thumbnailWidth}px`;
                img.style.maxWidth = 'none'; // Remove any upper limit
            });

            // Ensure thumbnails and duplicated content scroll seamlessly
            const totalWidth = Array.from(images).reduce((acc, img) => {
                return acc + img.offsetWidth + gap;
            }, 0);

            wrapper.style.width = `${totalWidth}px`;
        }

        // Pause animation on hover
        wrapper.addEventListener('mouseover', () => {
            wrapper.style.animationPlayState = 'paused';
        });

        // Resume animation when not hovering
        wrapper.addEventListener('mouseout', () => {
            wrapper.style.animationPlayState = 'running';
        });
    });
});