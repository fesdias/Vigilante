const html = document.documentElement;
const canvas = document.getElementById("hero-lightpass");
const context = canvas.getContext("2d");
const overlayText = document.getElementById("overlayText");

const frameCount = 197;

// SETTINGS - IMAGE
// Function to generate the path for the image of a specific frame index
const currentFrame = index => (
    `../assets/gallery/vigilante_01_004/webp/vigilante_01_004_${index.toString().padStart(4, '0')}.webp`
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
let jsonUrl = window.innerWidth < 700
  ? 'assets/gallery/vigilante_01_004/vigilante_data_en_mobile_01_004.json'
  : 'assets/gallery/vigilante_01_004/vigilante_data_en_desktop_01_004.json';

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

    // Calculate scaled dimensions based on the aspect ratio
    let scaledWidth = window.innerWidth;
    let scaledHeight = window.innerWidth / aspectRatio;

    // If the calculated height is less than the screen height, use screen height
    if (scaledHeight < window.innerHeight) {
        scaledHeight = canvas.height;
        scaledWidth = canvas.height * aspectRatio;
    } else {
        scaledHeight = canvas.width / aspectRatio;
        scaledWidth = canvas.width;
    }

    // Center the image both vertically and horizontally on the canvas
    const offsetX = (canvas.width - scaledWidth) / 2;
    const offsetY = (canvas.height - scaledHeight) / 2;

    context.drawImage(img, offsetX, offsetY, scaledWidth, scaledHeight);
};

// Event listener for window resize to redraw the image on the canvas
window.addEventListener('resize', drawImageToFit);


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