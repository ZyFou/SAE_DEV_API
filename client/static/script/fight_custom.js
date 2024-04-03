var nb_turn = 0;

var playerAttackCooldowns = {
    "Counter": 0,
};

var ennemyAttackCooldowns = {
    "Counter": 0,
};


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


function action(sender, target, data, initial_health) {
    if (sender == "player" && target == "ennemy" && playerTurn(nb_turn)) {
        playerAction(data, initial_health)
    } else if (sender == "player" && target == "ennemy" && playerTurn(nb_turn) == false) {
        console.log("It's ennemy Turn")
    } else if (sender == "ennemy" && target == "player" && playerTurn(nb_turn) == false) {
        ennemyAction(data, initial_health)
    }
    else if (sender == "ennemy" && target == "player" && playerTurn(nb_turn)) {
        console.log("It's Player Turn")
    }

}



function playerAction(data) {
    const YourhealthBar = document.getElementById('YourHealth');
    const EnnemyhealthBar = document.getElementById('EnnemyHealth');

    const YourEnergyBar = document.getElementById('YourEnergy');
    const EnnemyEnergyBar = document.getElementById('EnnemyEnergy');

    var damages = data.damages;
    var cost = data.cost;
    var name = data.name

    if (!isOnCoolDown('player', name)) {
        console.log('Not cooldown')
    } else {
        console.log('Cooldown')
    }

    if (hasEnoughEnergy(cost, YourEnergyBar.textContent)) {
        if (data.name == "ChargeKi") {
            updateEnergy('player', 20)
            increaseTurn()
        } else {
            if (attackEmitted(data)) {
                updateEnergy('player', cost * -1)
                increaseTurn()
                updateEnnemyHealth(damages)
            } else {
                updateEnergy('player', (cost / 2) * -1)
                increaseTurn()
            }
        }
    } else {
        console.log('Not enough energy')
        return
    }

}




function ennemyAction(data) {
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
            if (attackEmitted(data)) {
                updateEnergy('ennemy', cost * -1)
                increaseTurn()
                updatePlayerHealth(damages)
            } else {
                updateEnergy('ennemy', (cost / 2) * -1)
                increaseTurn()
            }
        }
    } else {
        console.log('Not enough energy')
        return
    }

}

function isOnCoolDown(sender, technique) {
    if (sender == "player") {
        return playerAttackCooldowns[technique] > 0
    } else if (sender == "ennemy") {
        return ennemyAttackCooldowns[technique] > 0
    }
}

function updateCoolDown(sender, technique) {
    if (sender == "player") {
        if (playerAttackCooldowns[technique] > 0) {
            playerAttackCooldowns[technique] -= 1
        }
    }
    else if (sender == "ennemy") {
        if (ennemyAttackCooldowns[technique] > 0) {
            ennemyAttackCooldowns[technique] -= 1
        }
    }
}

function attackEmitted(data) {
    return (Math.floor(Math.random() * 100) + 1) >= data.accuracy
}

function updatePlayerHealth(damages) {

    const YourhealthBar = document.getElementById('YourHealth');

    var damages = calculateDamages(ennemyStats, playerStats, damages)

    var health = parseInt(YourhealthBar.textContent);
    var remainingHealth = Math.max(health - damages, 0);
    var healthPercentage = (remainingHealth / playerInitialHealth) * 100; // 1800 est le nombre total de points de vie

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

function updateEnnemyHealth(damages) {
    const EnnemyhealthBar = document.getElementById('EnnemyHealth');

    var damages = calculateDamages(playerStats, ennemyStats, damages)

    var health = parseInt(EnnemyhealthBar.textContent);
    var remainingHealth = Math.max(health - damages, 0);
    var healthPercentage = (remainingHealth / ennemyInitialHealth) * 100;

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


function calculateDamages(senderStats, receiverStats, damages) {
    if (damages == 0) {
        return 0
    }
    else {
        senderStats = JSON.parse(senderStats)
        receiverStats = JSON.parse(receiverStats)
        var newDamages = (damages + senderStats.strength) - receiverStats.defense

        return newDamages
    }

}


function hasEnoughEnergy(cost, value) {
    if (value >= cost) {
        return true
    }
    else {
        return false
    }
}

function playerTurn(nb_turn) {
    return nb_turn % 2 == 0;
}

function increaseTurn() {
    const whoplays = document.getElementById('whoplays')
    if (whoplays.textContent == "Player") {
        whoplays.textContent = "Ennemy";
    } else {
        whoplays.textContent = "Player";
    };

    nb_turn += 1
    const turns_counter = document.getElementById('turns')
    turns_counter.textContent = nb_turn;
}



