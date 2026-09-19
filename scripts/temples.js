document.addEventListener('DOMContentLoaded', () => {
    // 1. Footer Copyright Year
    const currentYearSpan = document.getElementById('currentYear');
    if (currentYearSpan) {
        currentYearSpan.textContent = new Date().getFullYear();
    }
    
    // 2. Last Modified Date
    const lastModifiedSpan = document.getElementById('lastModified');
    if (lastModifiedSpan) {
        const lastModDate = new Date(document.lastModified);
        lastModifiedSpan.textContent = lastModDate.toLocaleDateString('en-US', { 
            year: 'numeric', 
            month: 'long', 
            day: 'numeric' 
        });
    }
    
    // 3. Hamburger Menu Toggle
    const hamburger = document.getElementById('hamburger');
    const navMenu = document.getElementById('navMenu');
    
    if (hamburger && navMenu) {
        hamburger.addEventListener('click', () => {
            navMenu.classList.toggle('active');
            if (navMenu.classList.contains('active')) {
                hamburger.textContent = '✕';
                hamburger.setAttribute('aria-label', 'Close navigation menu');
            } else {
                hamburger.textContent = '☰';
                hamburger.setAttribute('aria-label', 'Open navigation menu');
            }
        });
        
        // Close menu when a link is clicked
        const navLinks = navMenu.querySelectorAll('a');
        navLinks.forEach(link => {
            link.addEventListener('click', () => {
                if (navMenu.classList.contains('active')) {
                    navMenu.classList.remove('active');
                    hamburger.textContent = '☰';
                    hamburger.setAttribute('aria-label', 'Open navigation menu');
                }
            });
        });
    }
});