self.addEventListener("push", function(event) {
    if (event.data) {
      showNotification(event.data.text());
    }
  });
  
  function showNotification(message) {
    self.registration.showNotification("Inactivity Alert", {
      body: message,
      icon: "./icon.png"
    });
  }
  