function nameFun(){
var name = document.getElementById("name").value;
    var nameLength = name.length;
var nameLengthText = "The length of your name is: " + nameLength;
    document.getElementById("nameLength").innerHTML = nameLengthText;
}