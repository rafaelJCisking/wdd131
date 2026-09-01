// getdates.js - WDD 131
// Muestra el año actual y la fecha de última modificación en el footer

const yearElement = document.getElementById('currentyear');
const modifiedElement = document.getElementById('lastModified');

if (yearElement) {
    yearElement.textContent = new Date().getFullYear();
}

if (modifiedElement) {
    const lastMod = document.lastModified;
    const modDate = new Date(lastMod);
    const formattedDate = modDate.toLocaleDateString('en-US', {
        year: 'numeric',
        month: 'long',
        day: 'numeric'
    });
    modifiedElement.textContent = `Last Modified: ${formattedDate}`;
}