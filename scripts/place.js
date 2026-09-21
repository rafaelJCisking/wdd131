const temperature = 18;
const windSpeed = 12;

function calculateWindChill(temperature, windSpeed) {
  return (
    13.12 +
    0.6215 * temperature -
    11.37 * windSpeed ** 0.16 +
    0.3965 * temperature * windSpeed ** 0.16
  );
}

document.addEventListener("DOMContentLoaded", () => {
  const currentYear = document.querySelector("#currentYear");
  const lastModified = document.querySelector("#lastModified");
  const windChill = document.querySelector("#wind-chill");

  currentYear.textContent = new Date().getFullYear();
  lastModified.textContent = document.lastModified;

  if (temperature <= 10 && windSpeed > 4.8) {
    windChill.textContent = `${Math.round(calculateWindChill(temperature, windSpeed))} °C`;
  } else {
    windChill.textContent = "N/A";
  }
});
