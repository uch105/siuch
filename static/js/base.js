function showFullText(s){
    document.getElementById("show-full-"+s).classList.remove('hide');
    document.getElementById("show-less-"+s).classList.add('hide');
}
function showLessText(s){
    document.getElementById("show-full-"+s).classList.add('hide');
    document.getElementById("show-less-"+s).classList.remove('hide');
}
function Hide(s){
    document.getElementById(s).style.display = "none";
}