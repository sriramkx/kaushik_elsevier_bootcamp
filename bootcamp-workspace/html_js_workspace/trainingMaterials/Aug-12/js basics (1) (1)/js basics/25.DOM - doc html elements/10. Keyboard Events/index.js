
  // keycode.info
  //  to know which key is clicked //
  
//document.body.addEventListener('keydown',function(e){
	//var keyCode = e.keyCode;
	//console.log(keyCode + 'key is clicked')
	
//});

// keycode 13 is for enter

document.body.addEventListener('keydown',function(e){
	var keyCode = e.keyCode;
	if(keyCode === 13){
	console.log('keydown =>' + keyCode);
	}
});

document.body.addEventListener('keyup',function(e){
	var keyCode = e.keyCode;
	if(keyCode === 13){
	console.log('keyup =>' + keyCode);
	}
});

document.body.addEventListener('keypress',function(e){
	var keyCode = e.keyCode;
	if(keyCode === 13){
	console.log('keypress =>' + keyCode);
	}
});



