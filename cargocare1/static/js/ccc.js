function toggleDropdown() {
    const dropdown = document.getElementById("dropdown");
    dropdown.style.display = dropdown.style.display === "block" ? "none" : "block";
}

function logout() {
    alert("You have been logged out.");
    // Add logout functionality here
}
function goToSection(sectionId) {
    document.getElementById(divId).scrollIntoView({ behavior: 'smooth' })};

    let onDuty = false;

    function toggleDuty() {
        onDuty = !onDuty;
        const dutyButton = document.getElementById("toggleDuty");
        dutyButton.textContent = onDuty ? "Go On Duty" : "Go Of Duty";
        dutyButton.style.backgroundColor = onDuty ? "#4CAF50" : "#ff5722";
        
        if (onDuty) {
            showRideRequest();
        } else {
            clearRideRequest();
        }
    }
    
    function showRideRequest() {
        document.getElementById("pickup").textContent = "Pick-Up Location: 123 Main St";
        document.getElementById("dropoff").textContent = "Drop-Off Location: 456 Elm St";
    }
    
    function clearRideRequest() {
        document.getElementById("pickup").textContent = "Pick-Up Location: --";
        document.getElementById("dropoff").textContent = "Drop-Off Location: --";
    }
    
    function acceptRide() {
        alert("Ride Accepted!");
        clearRideRequest();
    }
    
    function rejectRide() {
        alert("Ride Rejected!");
        clearRideRequest();
    }
    