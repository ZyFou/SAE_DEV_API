var your_character;
var your_ennemy;
var stage;
var mode;


var infos_text = document.getElementById("title2ndWord")
var mode_container_div = document.getElementById("ModesContainer")

var your_choice_div = document.getElementById("charactersContainer")
var ennemy_choice_div = document.getElementById("EnnemycharactersContainer")
var stage_choice_div = document.getElementById("StagesContainer")



function pickYourCharacter(name) {
    var confirm_button = document.getElementById("confirm")
    var title = document.getElementsByTagName('h1');
    for (var i = 0; i < title.length; i++) {
        title[i].style.color = "#F2FCFF";

    }
    for (var i = 0; i < title.length; i++) {
        if (title[i].textContent === name) {
            your_character = name;
            title[i].style.color = "#63FA4B"
            confirm_button.style.display = "block"

            break;
        }
    }
}

function pickEnnemyCharacter(name) {
    var confirm_opponent = document.getElementById("confirm_opponent")
    var title = document.getElementsByClassName("ennemy");
    for (var i = 0; i < title.length; i++) {
        title[i].style.color = "#F2FCFF";
    }
    for (var i = 0; i < title.length; i++) {
        if (title[i].textContent === name) {
            your_ennemy = name;
            title[i].style.color = "#fe3939"
            confirm_opponent.style.display = "block"

            break;
        }
    }
}


function pickYourMode(arg) {
    var confirm_Mode = document.getElementById("confirm_Mode")
    confirm_Mode.style.display = "block"
    mode = arg
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

function confirmMode() {
    var confirm_button = document.getElementById("confirm_Mode")
    confirm_button.style.display = "none"
    infos_text.textContent = "PERSONNAGE"
    mode_container_div.style.display = "none"
    your_choice_div.style.display = "block";
}


function confirmYourChoice() {
    // alert("Perso choisi : " + your_character)
    var confirm_button = document.getElementById("confirm")
    confirm_button.style.display = "none"
    infos_text.textContent = "ADVERSAIRE"
    your_choice_div.style.display = "none"
    ennemy_choice_div.style.display = "block";
}

function confirmYourChoiceOpponent() {
    // alert("Adervsaire choisi : " + your_ennemy)
    var confirm_ennemy_button = document.getElementById("confirm_opponent")
    confirm_ennemy_button.style.display = "none"
    infos_text.textContent = "TERRAIN"
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
    // alert("Terrain choisi : " + stage)
    var confirm_stage_button = document.getElementById("confirm")
    // confirm_stage_button.style.display = "none"
    // ennemy_text.style.display = "none"
    // stage_choice_div.style.display = "none";

    var dataToSend = { "yourPick": your_character, "ennemy": your_ennemy, "stage": stage, "mode": mode };
    var queryString = convertToQueryString(dataToSend);
    window.location.href = `/gameMode/customGame?` + queryString
}


function setBackground(stageImage) {
    var imageUrl = stageImage;
    var body = document.body;

    body.style.backgroundImage = "url('" + imageUrl + "')";
    body.style.backgroundSize = "cover";
}


