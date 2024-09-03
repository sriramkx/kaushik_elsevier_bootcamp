console.log('JS Loaded');

var countdownElement = document.getElementById('countdown');


var initialCountdownVal = countdownElement.innerHTML;

setInterval(function() {
    initialCountdownVal = initialCountdownVal > 0 ? initialCountdownVal - 1 : 0;

    countdownElement.innerHTML = initialCountdownVal;
    
}, 1000);