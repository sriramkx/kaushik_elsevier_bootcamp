var username = document.getElementById('username');
console.log(username)

var loginForm = document.getElementById('login-form');

username.addEventListener('input', function(event) {
	//console.log(event.target.value); -- print the value that is typed in input box
    var currentValue = event.target.value;
    currentValue = currentValue.toUpperCase();
    console.log(currentValue);
    username.value = currentValue;
});

username.addEventListener('focus',  function() {
    console.log('Element Focussed');
});

username.addEventListener('blur', function(){
    console.log('Element Lost Focus');
})

loginForm.addEventListener('submit', function(e) {
    alert('Submit Button Clicked')
    e.preventDefault();
});

//e.preventDefault(); -- it will not refresh


// change event
//var username = document.getElementById('username');
//username.addEventListener('change',function(){
	
	//console.log('value changed');
	
	
//})