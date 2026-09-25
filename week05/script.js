// Product data array (normally fetched from an external source)
const products = [
    { id: 1, name: "Wireless Mouse" },
    { id: 2, name: "Mechanical Keyboard" },
    { id: 3, name: "USB-C Hub" },
    { id: 4, name: "Monitor Stand" },
    { id: 5, name: "Webcam HD" }
];

/**
 * Dynamically populates the product <select> element
 * with <option> tags built from the products array.
 */
function populateProducts() {
    const selectEl = document.getElementById("product");

    products.forEach(function (product) {
        const option = document.createElement("option");
        option.value = product.name;
        option.textContent = product.name;
        selectEl.appendChild(option);
    });
}

// Run on page load
document.addEventListener("DOMContentLoaded", populateProducts);