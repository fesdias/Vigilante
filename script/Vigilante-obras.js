const html = document.documentElement;
const canvas = document.getElementById("hero-lightpass");
const context = canvas.getContext("2d");
const overlayText = document.getElementById("overlayText");

const frameCount = 256;

// SETTINGS - IMAGE
// Function to generate the path for the image of a specific frame index
const currentFrame = index => (
    `../assets/photos/2023-08-v10_${index.toString().padStart(4, '0')}.png`
);

// Function to preload images into the browser cache
const preloadImages = () => {
    for (let i = 1; i <= frameCount; i++) {
        const img = new Image();
        img.src = currentFrame(i);
    }
};

// Create an Image object and set its initial source to the first frame
const img = new Image();
img.src = currentFrame(1);

// Function to update the image source and redraw it on the canvas
const updateImage = frameIndex => {
    img.src = currentFrame(frameIndex);

    img.onload = function () {
        canvas.width = Math.min(window.innerWidth, img.width);
        drawImageToFit();
    };
};


// SETTINGS - TEXT OVERLAY
const jsonUrl = 'assets/vigilante_obras-2023-08-v10-data.json';
let textData = [];

// Function to update the overlay text based on the frame index
const updateText = frameIndex => {

    const textEntry = textData.find(entry => entry.index === frameIndex);
    const textValue = textEntry ? textEntry.text : '';
    const formattedText = textValue.replace(/\n/g, '<br>');
    overlayText.innerHTML = formattedText;
};

// Function to preload text data from the JSON file
const preloadTextData = async () => {
    try {
        const response = await fetch(jsonUrl);
        textData = await response.json();
    } catch (error) {
        console.error('Error fetching or parsing JSON:', error.message);
    }
};


// BUILD CANVAS
// Set initial canvas size based on the window and image dimensions
canvas.width = Math.min(window.innerWidth, img.width);
canvas.height = window.innerHeight;

// Event listener for the image load event to redraw the image on the canvas
img.onload = function () {
    drawImageToFit();
};

// Function to draw the image on the canvas, maintaining aspect ratio
const drawImageToFit = () => {
    context.clearRect(0, 0, canvas.width, canvas.height);
    const aspectRatio = img.width / img.height;
    const scaledHeight = canvas.width / aspectRatio;
    const offsetY = (canvas.height - scaledHeight) / 2;
    context.drawImage(img, 0, offsetY, canvas.width, scaledHeight);
};

// Function to update the frame index based on the scroll position
const updateFrameIndex = () => {
    const scrollTop = html.scrollTop;
    const maxScrollTop = html.scrollHeight - window.innerHeight;
    const scrollFraction = scrollTop / maxScrollTop;

    // Calculate the frame index based on the scroll position
    const frameIndex = Math.min(frameCount - 1, Math.ceil(scrollFraction * frameCount));

    // Update the overlay text and image based on the calculated frame index
    updateText(frameIndex + 1);
    updateImage(frameIndex + 1);
};

preloadTextData();
preloadImages();
updateFrameIndex();

window.addEventListener('scroll', updateFrameIndex);