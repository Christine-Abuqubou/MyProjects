let mediaRecorder;
let audioChunks = [];

const textBtn = document.getElementById("text-btn");
const voiceBtn = document.getElementById("voice-btn");
const imageBtn = document.getElementById("image-btn");

const textArea = document.getElementById("text-description");
const imageInput = document.getElementById("image-upload");
const voiceControls = document.getElementById("voice-controls");
const recordBtn = document.getElementById("record-btn");
const recordStatus = document.getElementById("record-status");
const audioInput = document.getElementById("audio_data");
console.log("script loaded");

// Show Text description
textBtn.addEventListener("click", () => {
    textArea.classList.remove("hidden");
    textBtn.classList.add("bg-red-400");
    voiceControls.classList.add("hidden");
    voiceBtn.classList.remove("bg-red-400");
    imageInput.classList.add("hidden");
    imageBtn.classList.remove("bg-red-400");
});

// Show Voice recorder
voiceBtn.addEventListener("click", () => {
    voiceControls.classList.remove("hidden");
    voiceBtn.classList.add("bg-red-400");
    textArea.classList.add("hidden");
    textBtn.classList.remove("bg-red-400");
    imageInput.classList.add("hidden");
    imageBtn.classList.remove("bg-red-400");
});

// Show Image uploader
imageBtn.addEventListener("click", () => {
    imageInput.classList.remove("hidden");
    imageBtn.classList.add("bg-red-400");
    textArea.classList.add("hidden");
    textBtn.classList.remove("bg-red-400");
    voiceControls.classList.add("hidden");
    voiceBtn.classList.remove("bg-red-400");
});

// Voice recording logic
recordBtn.addEventListener("click", async () => {
    if (!mediaRecorder || mediaRecorder.state === "inactive") {
        // Start recording
        const stream = await navigator.mediaDevices.getUserMedia({
            audio: true,
        });
        mediaRecorder = new MediaRecorder(stream);
        audioChunks = [];
        mediaRecorder.ondataavailable = (e) => {
            audioChunks.push(e.data);
        };
        mediaRecorder.onstop = () => {
            const audioBlob = new Blob(audioChunks, {type: "audio/webm"});
            const reader = new FileReader();
            reader.readAsDataURL(audioBlob);
            reader.onloadend = () => {
                audioInput.value = reader.result; // Base64 encoded audio
            };
        };
        mediaRecorder.start();
        recordStatus.textContent = "Recording...";
        recordBtn.textContent = "Stop Recording";
    } else if (mediaRecorder.state === "recording") {
        // Stop recording
        mediaRecorder.stop();
        recordStatus.textContent = "Recording stopped";
        recordBtn.textContent = "Start Recording";
    }
});


function initLanguageMenu() {
    const menuItem = document.querySelector('.language-menu');
    if (!menuItem) return;
    const dropdown = menuItem.querySelector('.dropdown');
    let timer;
    clearTimeout(timer);
    dropdown.classList.remove('hidden');

    dropdown.addEventListener('mouseleave', () => {
        timer = setTimeout(() => dropdown.classList.add('hidden'), 200);
    });
}

