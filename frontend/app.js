const statusText = document.getElementById("server-status");
const checkStatusButton = document.getElementById("check-status-button");

const startButton = document.getElementById("start-button");
const stopButton = document.getElementById("stop-button");
const restartButton = document.getElementById("restart-button");
const messageText = document.getElementById("message");
const logsButton = document.getElementById("logs-button");
const serverLogs = document.getElementById("server-logs");
const serverList = document.getElementById("server-list");
const selectedServerText = document.getElementById("selected-server");
const serverNameInput = document.getElementById("server-name-input");
//const serverPortInput = document.getElementById("server-port-input");
const createServerButton = document.getElementById("create-server-button");
const createServerMessage = document.getElementById("create-server-message");

let selectedServer = "minecraft";


async function checkStatus() {
  try {
    const response = await fetch(`http://127.0.0.1:8000/servers/${selectedServer}/status`);

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

async function loadServers() {
  try {
    const response = await fetch("http://127.0.0.1:8000/servers");

    if (!response.ok) {
      throw new Error(`HTTP error: ${response.status}`);
    }

    const servers = await response.json();

    serverList.innerHTML = "";

    for (const server of servers) {
      const button = document.createElement("button");

      button.textContent = `${server.name} - ${server.status}`;

      button.addEventListener("click", function () {
        selectedServer = server.name.replace("gameserver-", "");

        selectedServerText.textContent = selectedServer;

        checkStatus();
        getLogs();
      });

      serverList.appendChild(button);
    }

  } catch (error) {
    console.error(error);
  }
}

async function createServer() {
  try {
    const name = serverNameInput.value;
  //  const port = Number(serverPortInput.value);

    const response = await fetch("http://127.0.0.1:8000/servers", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        name: name,
    //    port: port
      })
    });

    if (!response.ok) {
      throw new Error(`HTTP error: ${response.status}`);
    }

    const data = await response.json();

    createServerMessage.textContent = data.message;

    await loadServers();

  } catch (error) {
    console.error(error);
    createServerMessage.textContent = "Failed to create server";
  }
}

async function sendServerCommand(endpoint) {
  try {
    messageText.textContent = "Working...";

    const response = await fetch(
      `http://127.0.0.1:8000/servers/${selectedServer}/${endpoint}`,
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

    await loadServers();

  } catch (error) {
    console.error(error);
    messageText.textContent = "Command failed";
  }
}

async function getLogs() {
  try {
    const response = await fetch(`http://127.0.0.1:8000/servers/${selectedServer}/logs`);

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

createServerButton.addEventListener("click", createServer);

loadServers();
