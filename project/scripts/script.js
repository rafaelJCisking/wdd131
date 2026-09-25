// Object representing hostel configuration
const hostelConfig = {
    name: "Bahía Accesible Hostal",
    location: "Viña del Mar, Chile",
    currency: "CLP"
};

// Array of room objects
const accessibleRooms = [
    { id: 1, name: "Accessible Mixed Dorm", features: "Wide doors, lower bunk, step-free", price: 15000 },
    { id: 2, name: "Private Adapted Room", features: "Roll-in shower, grab bars, emergency cord", price: 45000 },
    { id: 3, name: "Sensory-Friendly Room", features: "Dimmable lights, quiet zone, ground floor", price: 35000 }
];

// Function 1: Render rooms using template literals exclusively
function renderRooms() {
    const container = document.getElementById("room-list");
    // Conditional branching
    if (!container) return;

    // Array method: map
    const htmlStrings = accessibleRooms.map(room => {
        return `<article class="room-card">
                    <h3>${room.name}</h3>
                    <p>${room.features}</p>
                    <p><strong>Price:</strong> $${room.price} ${hostelConfig.currency} / night</p>
                    <span class="badge">Verified Accessible</span>
                </article>`;
    });

    // DOM modification
    container.innerHTML = htmlStrings.join("");
}

// Function 2: Handle form submission and localStorage
function handleFormSubmit(event) {
    event.preventDefault();
    const form = event.target;
    
    // Object creation from form data
    const guestData = {
        name: form.elements["guestName"].value,
        email: form.elements["guestEmail"].value,
        needs: form.elements["accessibilityNeeds"].value,
        timestamp: new Date().toISOString()
    };

    // localStorage usage
    localStorage.setItem("bahiaGuestInquiry", JSON.stringify(guestData));

    // DOM interaction & template literal for output (exclusively)
    const responseEl = document.getElementById("form-response");
    responseEl.innerHTML = `<p>Thank you, ${guestData.name}! We have received your inquiry regarding: "${guestData.needs}". We will reply to ${guestData.email} within 24 hours.</p>`;
    responseEl.style.display = "block";
    
    form.reset();
}

// Function 3: Check for returning user
function checkReturningUser() {
    const savedGuest = localStorage.getItem("bahiaGuestInquiry");
    if (savedGuest) {
        const parsedGuest = JSON.parse(savedGuest);
        const welcomeEl = document.getElementById("welcome-message");
        // Conditional branching
        if (welcomeEl) {
            welcomeEl.innerHTML = `<strong>Welcome back, ${parsedGuest.name}!</strong> Ready to finalize your stay in ${hostelConfig.location}?`;
        }
    }
}

// Event Listening: DOMContentLoaded
document.addEventListener("DOMContentLoaded", () => {
    renderRooms();
    checkReturningUser();
    
    const bookingForm = document.getElementById("booking-form");
    if (bookingForm) {
        bookingForm.addEventListener("submit", handleFormSubmit);
    }
});