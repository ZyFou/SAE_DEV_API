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


function sendFight() {
    var dataToSend = { "yourPick": yourCharacter, "ennemy": yourEnnemy, "stage": stagePicked, "mode": 'solo', "AISmartness": AiBrain, "EXPearned": EXPearned / EXPearned };
    var queryString = convertToQueryString(dataToSend);
    window.location.href = `/gameMode/customGame?` + queryString
}


