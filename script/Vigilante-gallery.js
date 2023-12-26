// Get all the elements with class "timelapse"
var videos = document.querySelectorAll('.timelapse');

// Add event listeners for hover and mouse leave to each video
videos.forEach(function(video) {
    // Pause the video by default
    video.pause();

    // Add event listener for hover
    video.parentElement.addEventListener('mouseenter', function () {
        // Play the video on hover
        video.play();
    });

    // Add event listener for mouse leave
    video.parentElement.addEventListener('mouseleave', function () {
        // Pause the video when not hovering
        video.pause();
    });
});
