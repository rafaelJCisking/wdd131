/**
 * Handles the review confirmation page functionality:
 * - Displays submitted form data
 * - Tracks and increments the review counter using localStorage
 */

// Product data array (needed to map product IDs to names)
const products = [
  {
    id: "fc-1888",
    name: "flux capacitor",
    averagerating: 4.5
  },
  {
    id: "fc-2050",
    name: "power laces",
    averagerating: 4.7
  },
  {
    id: "fs-1987",
    name: "time circuits",
    averagerating: 3.5
  },
  {
    id: "ac-2000",
    name: "low voltage reactor",
    averagerating: 3.9
  },
  {
    id: "jj-1969",
    name: "warp equalizer",
    averagerating: 5.0
  }
];

/**
 * Gets the product name from the product ID
 */
function getProductName(productId) {
    const product = products.find(p => p.id === productId);
    return product ? product.name : "Unknown Product";
}

/**
 * Parses URL parameters from the form submission (method="get")
 */
function getFormData() {
    const params = new URLSearchParams(window.location.search);
    return {
        product: params.get('product'),
        rating: params.get('rating'),
        installDate: params.get('installDate'),
        features: params.getAll('features'),
        reviewText: params.get('reviewText'),
        username: params.get('username')
    };
}

/**
 * Displays the submitted form data on the page
 */
function displayReviewData() {
    const data = getFormData();

    // Display product name (map ID to name)
    if (data.product) {
        document.getElementById('display-product').textContent = getProductName(data.product);
    }

    // Display rating with stars
    if (data.rating) {
        const stars = '★'.repeat(parseInt(data.rating)) + '☆'.repeat(5 - parseInt(data.rating));
        document.getElementById('display-rating').textContent = stars + ` (${data.rating}/5)`;
    }

    // Display installation date
    if (data.installDate) {
        document.getElementById('display-date').textContent = data.installDate;
    }

    // Display useful features
    if (data.features && data.features.length > 0) {
        document.getElementById('display-features').textContent = data.features.join(', ');
    } else {
        document.getElementById('display-features').textContent = 'None selected';
    }

    // Display written review
    if (data.reviewText) {
        document.getElementById('display-review').textContent = data.reviewText;
    } else {
        document.getElementById('display-review').textContent = 'No review provided';
    }

    // Display username
    if (data.username) {
        document.getElementById('display-username').textContent = data.username;
    } else {
        document.getElementById('display-username').textContent = 'Anonymous';
    }
}

/**
 * Increments and displays the review counter using localStorage
 */
function updateReviewCounter() {
    // Get current count from localStorage (default to 0 if not exists)
    let count = localStorage.getItem('reviewCount');
    count = count ? parseInt(count) : 0;

    // Increment the counter
    count++;

    // Save back to localStorage
    localStorage.setItem('reviewCount', count);

    // Display the count
    document.getElementById('review-count').textContent = count;
}

// Run when page loads
document.addEventListener("DOMContentLoaded", function() {
    displayReviewData();
    updateReviewCounter();
});