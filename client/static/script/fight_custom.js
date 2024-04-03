var nb_turn = 0;


function SetHealthBarYou(health) {
    const healthBar = document.getElementById('YourHealth');
    const healthPercentage = Math.min(Math.max(health, 0), 100);
    healthBar.style.width = healthPercentage + '%';
    healthBar.textContent = health;
}

function SetHealthBarEnnemy(health) {
    const healthBar = document.getElementById('EnnemyHealth');
    const healthPercentage = Math.min(Math.max(health, 0), 100);
    healthBar.style.width = healthPercentage + '%';
    healthBar.textContent = health;
}


function playerAttack(data, initial_health) {
    const YourhealthBar = document.getElementById('YourHealth');
    const EnnemyhealthBar = document.getElementById('EnnemyHealth');

    const YourEnergyBar = document.getElementById('YourEnergy');
    const EnnemyEnergyBar = document.getElementById('EnnemyEnergy');

    var damages = data.damages;
    var cost = data.cost;

    if (hasEnoughEnergy(cost, YourEnergyBar.textContent)) {
        if (data.name == "ChargeKi") {
            updateEnergy('player', 20)
            increaseTurn()
        } else {
            updateEnergy('player', cost * -1)
            increaseTurn()
        }
    } else {
        console.log('Not enough energy')
        return
    }

    var health = parseInt(EnnemyhealthBar.textContent);
    var remainingHealth = Math.max(health - damages, 0);
    var healthPercentage = (remainingHealth / initial_health) * 100; // 1800 est le nombre total de points de vie

    EnnemyhealthBar.style.width = healthPercentage + '%';
    EnnemyhealthBar.textContent = remainingHealth;

    if (healthPercentage <= 50) {
        EnnemyhealthBar.classList.remove('bg-success');
        EnnemyhealthBar.classList.add('bg-warning');
    }
    if (healthPercentage <= 25) {
        EnnemyhealthBar.classList.remove('bg-warning');
        EnnemyhealthBar.classList.add('bg-danger');
    }
}

function ennemyAttack(data, initial_health) {
    const YourhealthBar = document.getElementById('YourHealth');
    const EnnemyhealthBar = document.getElementById('EnnemyHealth');

    const YourEnergyBar = document.getElementById('YourEnergy');
    const EnnemyEnergyBar = document.getElementById('EnnemyEnergy');

    var damages = data.damages;
    var cost = data.cost;

    if (hasEnoughEnergy(cost, EnnemyEnergyBar.textContent)) {
        if (data.name == "ChargeKi") {
            updateEnergy('ennemy', 20)
            increaseTurn()
        } else {
            updateEnergy('ennemy', cost * -1)
            increaseTurn()
        }
    } else {
        alert('Not enough energy')
        return
    }

    var health = parseInt(YourhealthBar.textContent);
    var remainingHealth = Math.max(health - damages, 0);
    var healthPercentage = (remainingHealth / initial_health) * 100; // 1800 est le nombre total de points de vie

    YourhealthBar.style.width = healthPercentage + '%';
    YourhealthBar.textContent = remainingHealth;

    if (healthPercentage <= 50) {
        YourhealthBar.classList.remove('bg-success');
        YourhealthBar.classList.add('bg-warning');
    }
    if (healthPercentage <= 25) {
        YourhealthBar.classList.remove('bg-warning');
        YourhealthBar.classList.add('bg-danger');
    }
}


function attack(sender, target, data, initial_health) {
    const YourhealthBar = document.getElementById('YourHealth');
    const EnnemyhealthBar = document.getElementById('EnnemyHealth');

    const YourEnergyBar = document.getElementById('YourEnergy');
    const EnnemyEnergyBar = document.getElementById('EnnemyEnergy');


    if (playerTurn(nb_turn) && sender == "player") {
        console.log("player Turn")
    } else if (playerTurn(nb_turn) && sender == "ennemy") {
        console.log("player Turn")

    } else {
        console.log("Ennemy Turn")
    }

    console.log("sender : ", sender, " | target", target, " | player turn", playerTurn(nb_turn))

    if (sender == "player" && target == "ennemy" && playerTurn(nb_turn)) {
        playerAttack(data, initial_health)
    } else if (sender == "player" && target == "ennemy" && playerTurn(nb_turn) == false) {
        alert("It's ennemy Turn")
    } else if (sender == "ennemy" && target == "player" && playerTurn(nb_turn) == false) {
        ennemyAttack(data, initial_health)
    }
    else if (sender == "ennemy" && target == "player" && playerTurn(nb_turn)) {
        alert("It's Player Turn")
    }
}


function playerTurn(nb_turn) {
    return nb_turn % 2 == 0;
}

function increaseTurn() {
    nb_turn += 1
    const turns_counter = document.getElementById('turns')
    turns_counter.textContent = nb_turn;
}


function hasEnoughEnergy(cost, value) {
    if (value >= cost) {
        return true
    }
    else {
        return false
    }
}
