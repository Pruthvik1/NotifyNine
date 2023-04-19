let inactivityTime = 0;
let notificationTimer = null;

// Log keyboard and mouse events
document.addEventListener("keydown", resetTimer);
document.addEventListener("mousemove", resetTimer);
document.addEventListener("mousedown", resetTimer);
document.addEventListener("touchstart", resetTimer);
document.addEventListener("click", resetTimer);

function resetTimer() {
  console.log("Mouse or keyboard event occurred");
  inactivityTime = 0;
  if (notificationTimer !== null) {
    clearTimeout(notificationTimer);
    console.log("Notification timer reset");
  }
  notificationTimer = setTimeout(showNotification, 4* 1000); // 10 minutes
}

// Log remaining time
setInterval(function() {
  inactivityTime++;
  console.log(`Inactive for ${inactivityTime} seconds`);
  if (inactivityTime >= 4) { // 10 minutes
    console.log("User is inactive");
    showNotification();
  }
}, 1000);

// Show notification
function showNotification() {
  console.log("Showing notification");
  if (Notification.permission === "granted") {
    const notificationOptions = {
      body: "You've been inactive for 10 minutes. Please take a break.",
      icon: "./icon.png"
    };
    const notification = new Notification("Inactive Reminder", notificationOptions);
    playSound();
  } else if (Notification.permission !== "denied") {
    Notification.requestPermission().then(permission => {
      if (permission === "granted") {
        const notificationOptions = {
          body: "You've been inactive for 10 minutes. Please take a break.",
          icon: "./icon.png"
        };
        const notification = new Notification("Inactive Reminder", notificationOptions);
        playSound();
      }
    });
  }
}

// Play sound
function playSound() {
  const audio = new Audio("./sound.wav");
  audio.play();
}
