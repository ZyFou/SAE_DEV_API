var your_character;
var your_ennemy;
var stage;


function pickYourCharacter(name) {
    var confirm_button = document.getElementById("confirm")
    var images = document.getElementsByTagName('img');
    for (var i = 0; i < images.length; i++) {
        images[i].style.boxShadow = "none";

    }
    for (var i = 0; i < images.length; i++) {
        if (images[i].alt === name) {
            your_character = name;
            images[i].style.boxShadow = "0 0 0 3px #63FA4B"
            confirm_button.style.display = "block"

            break;
        }
    }
}

function pickEnnemyCharacter(name) {
    var confirm_opponent = document.getElementById("confirm_opponent")
    var images = document.getElementsByClassName("ennemy");
    for (var i = 0; i < images.length; i++) {
        images[i].style.boxShadow = "none";

    }
    for (var i = 0; i < images.length; i++) {
        if (images[i].alt === name) {
            your_ennemy = name;
            images[i].style.boxShadow = "0 0 0 3px #EC2324"
            confirm_opponent.style.display = "block"

            break;
        }
    }
}


function pickStage(name) {
    var confirm_stage = document.getElementById("confirm_stage")
    var images = document.getElementsByClassName("stage");
    for (var i = 0; i < images.length; i++) {
        images[i].style.boxShadow = "none";

    }
    for (var i = 0; i < images.length; i++) {
        if (images[i].alt === name) {
            stage = name;
            images[i].style.boxShadow = "0 0 0 3px #F2FCFF"
            confirm_stage.style.display = "block"

            break;
        }
    }
}


var ennemy_text = document.getElementById("title2ndWord")
var your_choice_div = document.getElementById("charactersContainer")
var ennemy_choice_div = document.getElementById("EnnemycharactersContainer")

var stage_choice_div = document.getElementById("StagesContainer")


function confirmYourChoice() {
    alert("Perso choisi : " + your_character)
    var confirm_button = document.getElementById("confirm")
    confirm_button.style.display = "none"
    ennemy_text.textContent = "ADVERSAIRE"
    your_choice_div.style.display = "none"
    ennemy_choice_div.style.display = "block";
}

function confirmYourChoiceOpponent() {
    alert("Adervsaire choisi : " + your_ennemy)
    var confirm_ennemy_button = document.getElementById("confirm_opponent")
    confirm_ennemy_button.style.display = "none"
    ennemy_text.textContent = "TERRAIN"
    ennemy_choice_div.style.display = "none";
    stage_choice_div.style.display = "block";
}



function convertToQueryString(params) {
    var queryString = '';

    for (var key in params) {
        if (params.hasOwnProperty(key)) {
            queryString += encodeURIComponent(key) + '=' + encodeURIComponent(params[key]) + '&';
        }
    }

    queryString = queryString.slice(0, -1);
    return queryString;
}



function confirmStage() {
    alert("Terrain choisi : " + stage)
    var confirm_stage_button = document.getElementById("confirm")
    confirm_stage_button.style.display = "none"
    ennemy_text.style.display = "none"
    stage_choice_div.style.display = "none";

    var dataToSend = { "yourPick": your_character, "ennemy": your_ennemy, "stage": stage };
    var queryString = convertToQueryString(dataToSend);
    window.location.href = `/test?` + queryString
}



