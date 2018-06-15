function clock(){
    window.scrollTo(0, document.body.scrollHeight);
    if(document.getElementById("#j-computer")){
        window.clearInterval(interval);
    }
}
var interval = window.setInterval("clock()",1);
