const statusText = document.getElementById("server-status");
const checkStatusButton = document.getElementById("check-status-button");

const startButton = document.getElementById("start-button");
const stopButton = document.getElementById("stop-button");
const restartButton = document.getElementById("restart-button");
const messageText = document.getElementById("message");
const logsButton = document.getElementById("logs-button");
const serverLogs = document.getElementById("server-logs");

async function checkStatus() {
  try {
    const response = await fetch("http://127.0.0.1:8000/status");

    if (!response.ok) {
      throw new Error(`HTTP error: ${response.status}`);
    }

    const data = await response.json();

    statusText.textContent = data.status;
  } catch (error) {
    console.error(error);
    statusText.textContent = "Error";
  }
}

async function sendServerCommand(endpoint) {
  try {
    messageText.textContent = "Working...";

    const response = await fetch(
      `http://127.0.0.1:8000/${endpoint}`,
      {
        method: "POST"
      }
    );

    if (!response.ok) {
      throw new Error(`HTTP error: ${response.status}`);
    }

    const data = await response.json();

    messageText.textContent = data.message;
    statusText.textContent = data.status;
  } catch (error) {
    console.error(error);
    messageText.textContent = "Command failed";
  }
}

async function getLogs() {
  try {
    const response = await fetch("http://127.0.0.1:8000/logs");

    if (!response.ok) {
      throw new Error(`HTTP error: ${response.status}`);
    }

    const data = await response.json();

    serverLogs.textContent = data.logs;

  } catch (error) {
    console.error(error);
    serverLogs.textContent = "Unable to load logs.";
  }
}



checkStatusButton.addEventListener("click", checkStatus);

logsButton.addEventListener("click", function () {
  getLogs();
});

startButton.addEventListener("click", function () {
  sendServerCommand("start");
});

stopButton.addEventListener("click", function () {
  sendServerCommand("stop");
});

restartButton.addEventListener("click", function () {
  sendServerCommand("restart");
});
