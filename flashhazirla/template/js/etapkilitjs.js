function anahtarKodBilgi() {
	mesaj({mesaj:"Tahta kurulumunda kullandığınız anahtar kodu girmelisiniz. Aksi durumda usb anahtar çalışmayacaktır.",renk:"mavi"})
}

function initialize() {
	pywebview.api.init().then(mesaj);
  //~ pywebview.api.doHeavyStuff().then(function(s) {
		//~ mesaj(s)
		//~ btn.onclick = doHeavyStuff
		//~ btn.innerText = 'Perform a heavy operation'
	//~ })

}

function usbListesiGuncelle(s) {
    pywebview.api.log(s)
//    mesaj({"mesaj":"Usb listesi okunuyor","renk":"s-mavi"});
    $("#usbListe").html('');
    for (i in s) {
         $("#usbListe").append('<option value="'+s[i]["value"]+'">'+s[i]["label"]+'<span>'+s[i]["name"]+' '+s[i]["filesistem"]+' '+s[i]["size"]+'</option>');
    }
}

function usListesiYenile() {
	pywebview.api.getUsbListesi().then(function(s) {
        usbListesiGuncelle(s);
	});
}

function getSifreKodu() {
	pywebview.api.getSifreKodu().then(function(s) {$("#anahtarkodu").val(s);});
}

function flashHazirla() {
	pywebview.api.flashHazirla($("#usbListe").val(),$("#anahtarkodu").val()).then(mesaj);
}

function sifreGosterGizle() {
	$('#anahtarkodu').attr('type')=="text"?$('#anahtarkodu').attr('type','password'):$('#anahtarkodu').attr('type','text');
}

function exit() {
 	pywebview.api.exit();
}


function mesaj(s) {
    if($("#snackbar").hasClass("hide")) {
      $("#snackbar").removeClass("hide").addClass("show").addClass(s.renk);
      $("#snackbar").html(s.mesaj);

      msjSure=setTimeout(function(){

          $("#snackbar").removeClass("show").removeClass(s.renk).addClass("hide");
        }, 3500);
    }
}

 $(document).ready(function() {
 try  {
 	setTimeout(usListesiYenile,1000);
	setTimeout(getSifreKodu,1000);
}catch(e) {
    pywebview.api.error(e)
}

});


