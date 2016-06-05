$(window).load(function(){
	/*$("button[id='id-front-btn']").click(function() {
	    $("input[id='id-front-input']").focus().click();
	});

	$("button[id='id-back-btn']").click(function() {
	    $("input[id='id-back-input']").focus().click();
	});*/
	
    $("#id-front-input").change(function () {    	
        if (this.files && this.files[0]) {
            var reader = new FileReader();
            reader.onload = imageIsLoaded;
            reader.readAsDataURL(this.files[0]);
        }
    });
    
	function imageIsLoaded(e) {
	    $("#id-front-img").attr('src', e.target.result);
	};
	
});

// video capture with web rtc
