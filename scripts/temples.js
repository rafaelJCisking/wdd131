// Wait for the HTML document to be completely loaded
document.addEventListener('DOMContentLoaded', () => {
    
    // ==========================================
    // 1. Dynamic Footer Dates
    // ==========================================
    
    // Get the current year (e.g., 2026)
    const currentYearSpan = document.getElementById('currentYear');
    if (currentYearSpan) {
        currentYearSpan.textContent = new Date().getFullYear();
    }

    // Get the last modified date of the file and format it cleanly
    const lastModifiedSpan = document.getElementById('lastModified');
    if (lastModifiedSpan) {
        // document.lastModified returns a string like "09/24/2026 14:30:00"
        // We parse it into a Date object and format it to standard MM/DD/YYYY
        const modDate = new Date(document.lastModified);
        lastModifiedSpan.textContent = modDate.toLocaleDateString();
    }

    // ==========================================
    // 2. Responsive Hamburger Menu Toggle
    // ==========================================
    const hamburger = document.getElementById('hamburger');
    const navMenu = document.getElementById('navMenu');
    const navLinks = document.querySelectorAll('#navMenu a');

    if (hamburger && navMenu) {
        // Toggle menu when hamburger is clicked
        hamburger.addEventListener('click', () => {
            // Toggle the CSS class that shows/hides the menu
            navMenu.classList.toggle('active');
            
            // Update accessibility attribute for screen readers
            const isExpanded = navMenu.classList.contains('active');
            hamburger.setAttribute('aria-expanded', isExpanded);
        });

        // Optional but recommended UX: Close the menu when a link is clicked on mobile
        navLinks.forEach(link => {
            link.addEventListener('click', () => {
                if (navMenu.classList.contains('active')) {
                    navMenu.classList.remove('active');
                    hamburger.setAttribute('aria-expanded', 'false');
                }
            });
        });
    }
});