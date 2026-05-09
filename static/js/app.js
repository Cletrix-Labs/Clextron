const form = document.getElementById("research-form");
const topicInput = document.getElementById("topic");
const languageSelect = document.getElementById("language");
const submitButton = document.getElementById("submit-btn");
const statusEl = document.getElementById("status");
const resultEl = document.getElementById("result");

function setStatus(message, type = "") {
  statusEl.className = `status ${type}`.trim();
  statusEl.textContent = message;
}

async function runResearch(event) {
  event.preventDefault();

  const topic = topicInput.value.trim();
  const language = languageSelect.value;

  if (!topic) {
    setStatus("Please enter a topic.", "error");
    topicInput.focus();
    return;
  }

  submitButton.disabled = true;
  setStatus("Running research...", "");
  resultEl.textContent = "Loading...";

  try {
    const apiBaseUrl = window.API_BASE_URL || `${window.location.protocol}//${window.location.hostname}:8000`;
    const response = await fetch(`${apiBaseUrl}/research`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ topic, language }),
    });

    let payload;
    try {
      const responseText = await response.text();
      if (!responseText) {
        throw new Error("Empty response from server");
      }
      payload = JSON.parse(responseText);
    } catch (parseError) {
      // If JSON parsing fails, provide a helpful error
      throw new Error(`Server error (HTTP ${response.status}): Unable to parse response`);
    }

    if (!response.ok) {
      throw new Error(payload.detail || `Request failed (HTTP ${response.status})`);
    }

    setStatus(`Completed in ${payload.language}.`, "success");
    resultEl.textContent = payload.result;
  } catch (error) {
    setStatus(error.message, "error");
    resultEl.textContent = "No research output yet.";
  } finally {
    submitButton.disabled = false;
  }
}

form.addEventListener("submit", runResearch);
