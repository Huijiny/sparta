

var name = $('#nameField');
var count = $('#countField');
var address = $('#addressField');
var phone = $('#phoneField');
var orderBtn = $('#orderBtn');

function check(){
	console.log(name.val());
	if(name.val()=="") {
		name.focus();
		alert("이름");
	}
	if(count.val()=="") {
		count.focus();
		alert("수량");
	}
	if(address.val()=="") {
		address.focus();
		alert("주소");
	}
	if(phone.val()=="") {
		phone.focus();
		alert("전화번호");
	}
}


function init() {
	//orderBtn.attr("onClick","check()");
	orderBtn.click(check());
}


init();