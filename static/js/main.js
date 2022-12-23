function init() {
    const client = ZAFClient.init();
    switch (action) {
      case "notifySuccess":
        client.invoke("notify", "Request successful!");
        break;
      case "notifyFailure":
        client.invoke("notify", msg, "error");
        break;
    }
  }
  
  window.addEventListener("load", init, false);