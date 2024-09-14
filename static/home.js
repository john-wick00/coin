window.Telegram.WebApp.ready();

const userInfoDiv = document.getElementById("user-info");
const continueButton = document.getElementById("continue-button");

// Fetching user data from Telegram WebApp
const initDataUnsafe = window.Telegram.WebApp.initDataUnsafe;

// Display the user's first name, user id, and username
if (initDataUnsafe && initDataUnsafe.user) {
    const firstName = initDataUnsafe.user.first_name;
    const userId = initDataUnsafe.user.id;
    const username = initDataUnsafe.user.username || "Not available";

    userInfoDiv.innerHTML = `
        <p>First Name: ${firstName}</p>
        <p>User ID: ${userId}</p>
        <p>Username: @${username}</p>
    `;
} else {
    userInfoDiv.innerHTML = "<p>Failed to retrieve user information.</p>";
}

// Adding click event to the continue button for redirection
continueButton.addEventListener("click", function() {
    // Redirect to the farming page
    window.location.href = "/farming";
});
console.log("home.js loaded correctly");
