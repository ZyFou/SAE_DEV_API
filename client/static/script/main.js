var your_character;
var your_ennemy;


function pickYourCharacter(name) {
    var confirm_button = document.getElementById("confirm")
    var images = document.getElementsByTagName('img');
    for (var i = 0; i < images.length; i++) {
        images[i].style.boxShadow = "none";

    }
    for (var i = 0; i < images.length; i++) {
        if (images[i].alt === name) {
            your_character = name;
            images[i].style.boxShadow = "0 0 0 3px #FFDB00"
            confirm_button.style.display = "block"

            break;
        }
    }
}

function pickEnnemyCharacter(name) {
    var confirm_button = document.getElementById("confirm")
    var images = document.getElementsByClassName("ennemy");
    for (var i = 0; i < images.length; i++) {
        images[i].style.boxShadow = "none";

    }
    for (var i = 0; i < images.length; i++) {
        if (images[i].alt === name) {
            your_ennemy = name;
            images[i].style.boxShadow = "0 0 0 3px #FFDB00"
            confirm_button.style.display = "block"

            break;
        }
    }
}

var ennemy_text = document.getElementById("title2ndWord")
var your_choice_div = document.getElementById("charactersContainer")
var ennemy_choice_div = document.getElementById("EnnemycharactersContainer")

function confirmYourChoice() {
    // alert("Perso choisi : " + your_character)
    ennemy_text.textContent = "ADVERSAIRE"
    your_choice_div.style.display = "none"
    ennemy_choice_div.style.display = "block";
}