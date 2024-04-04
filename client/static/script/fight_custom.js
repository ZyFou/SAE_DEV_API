var nb_turn = 0;


var lastPlayerAttack;
var playerAttackCooldowns = {
    "Counter": 0,
};

var lastEnnemyAttack;
var ennemyAttackCooldowns = {
    "Counter": 0,
};

var DamageBonus = {
    'player': 0,
    'ennemy': 0
}

var ReductionBonus = {
    'player': 0,
    'ennemy': 0
}


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

let playerHasPlayed = false
let ennemyHasPlayed = false

var playerMove;
var playerMoveData;

var ennemyMove;
var ennemyMoveData;

function action(sender, data, initial_health) {
    sender == 'player' ? playerHasPlayed = true : ennemyHasPlayed = true;
    if (sender == "player" && playerHasPlayed && !checkCD(sender, data.name)) {
        playerMove = data.type
        playerMoveData = data;
    }
    else if (checkCD(sender, data.name)) {
        playerHasPlayed = false;
        alert("This technique is on CD");
    }

    if (sender == "ennemy" && ennemyHasPlayed && !checkCD(sender, data.name)) {
        ennemyMove = data.type
        ennemyMoveData = data;
    }
    else if (checkCD(sender, data.name)) {
        ennemyHasPlayed = false;
        alert("This technique is on CD");
    }

    if (playerHasPlayed && ennemyHasPlayed && playerMove != "" && ennemyMove != "") {
        fightLogic(playerMove, ennemyMove, playerMoveData, ennemyMoveData);
        playerHasPlayed = false
        ennemyHasPlayed = false
        playerMove = "";
        ennemyMove = "";
    }

}


function setLastAttack(sender, attack) {
    if (sender == "player") {
        lastPlayerAttack = attack;
    } else {
        lastEnnemyAttack = attack;
    }
}

function attackLogic(sender, target, attackData) {
    var healthBar;
    var energyBar;
    var bonus = DamageBonus[sender]


    if (sender == "player") {
        healthBar = document.getElementById('YourHealth');
        energyBar = document.getElementById('YourEnergy');

    } else {
        healthBar = document.getElementById('EnnemyHealth');
        energyBar = document.getElementById('EnnemyEnergy');
    }

    var attack_name = attackData.name;
    var damages = attackData.damages
    var accuracy = attackData.accuracy;
    var cost = attackData.cost;
    var cooldown = attackData.cooldown

    var techWithCD = "Counter";
    if (!checkCD(sender, attack_name)) {
        if (hasEnoughEnergy(cost, energyBar.textContent)) {
            if (attackEmitted(accuracy)) {
                if (attack_name == "ChargeKi") {
                    updateEnergy(sender, 500)
                    increaseTurn()
                    updateCoolDown(sender, techWithCD)

                    setLastAttack(sender, attack_name)

                } else if (attack_name == "Defense") {
                    updateEnergy(sender, cost * -1)
                    increaseTurn()
                    updateCoolDown(sender, techWithCD)

                    setLastAttack(sender, attack_name)

                } else if (attack_name == "Counter") {
                    updateEnergy(sender, cost * -1)
                    increaseTurn()
                    setCoolDown(sender, attack_name, cooldown)

                    setLastAttack(sender, attack_name)

                } else {
                    updateEnergy(sender, cost * -1)
                    increaseTurn()
                    updateCoolDown(sender, techWithCD)
                    inflictDamages(sender, target, damages, bonus, attackData)
                    setLastAttack(sender, attack_name)
                }
            }
            else {
                if (attack_name == "Counter") {
                    setCoolDown(sender, attack_name, cooldown);
                }
                console.log("Missed")
                updateEnergy(sender, (cost / 2) * -1)
                increaseTurn()
            }
        } else {
            console.log('Not enough Energy')
        }
    } else {
        console.log('Cooldown')
    }
}


function inflictDamages(sender, target, attackValue, bonus, attackData) {
    var healthBar;
    var initalHealthValue;
    var sender_stats;
    var receiverStats;

    var attackDamage = attackData.damages

    if (target == "player") {
        healthBar = document.getElementById('YourHealth');
        initalHealthValue = playerInitialHealth;
        sender_stats = ennemyStats;
        receiverStats = playerStats;
    } else {
        healthBar = document.getElementById('EnnemyHealth');
        initalHealthValue = ennemyInitialHealth;
        sender_stats = playerStats;
        receiverStats = ennemyStats;
    }

    var newDamages = attackValue + bonus;

    var finalDamages = calculateDamages(sender_stats, receiverStats, newDamages)

    if (sender == "player" && lastEnnemyAttack == "Guard") {
        finalDamages = bonus

    } else if (sender == "ennemy" && lastPlayerAttack == "Guard") {
        finalDamages = bonus

    } else if (sender == "player" && lastEnnemyAttack == "Counter") {
        finalDamages = 0;
        displayDamages("ennemy", "player", calculateDamages(playerStats, ennemyStats, (attackDamage * 1.5) + DamageBonus["player"]));

    } else if (sender == "ennemy" && lastPlayerAttack == "Counter") {
        finalDamages = 0;
        displayDamages("player", "ennemy", calculateDamages(ennemyStats, playerStats, (attackDamage * 1.5) + DamageBonus["ennemy"]));
    }


    displayDamages(sender, target, finalDamages);

}


function displayDamages(sender, target, finalDamages) {
    var healthBar;
    var initalHealthValue;

    var sender_stats;

    if (target == "player") {
        healthBar = document.getElementById('YourHealth');
        initalHealthValue = playerInitialHealth;
    } else {
        healthBar = document.getElementById('EnnemyHealth');
        initalHealthValue = ennemyInitialHealth;
    }

    if (sender == "player") {
        sender_stats = playerStats;
    } else {
        sender_stats = ennemyStats;
    };


    var health = parseInt(healthBar.textContent);
    var remainingHealth = Math.max(health - finalDamages, 0);

    var healthPercentage = (remainingHealth / initalHealthValue) * 100;


    healthBar.style.width = healthPercentage + '%';
    healthBar.textContent = remainingHealth;

    DamageBonusChecker(sender_stats, healthPercentage, healthBar, sender);

}

function DamageBonusChecker(sender_stats, healthPercentage, healthBar, sender) {
    // console.log(sender_stats, healthPercentage, healthBar, sender)

    sender_stats = JSON.parse(sender_stats);
    if (sender == "player") {
        sender == "ennemy"
    }
    else {
        sender == "player"
    }

    if (healthPercentage <= 75) {
        healthBar.classList.remove('bg-success');
        healthBar.classList.add('bg-info');
        DamageBonus[sender] = (sender_stats["strength"]) * 0.1
    }
    if (healthPercentage <= 50) {
        healthBar.classList.remove('bg-info');
        healthBar.classList.add('bg-warning');
        DamageBonus[sender] = (sender_stats["strength"]) * 0.5
    }
    if (healthPercentage <= 25) {
        healthBar.classList.remove('bg-warning');
        healthBar.classList.add('bg-danger');
        DamageBonus[sender] = (sender_stats["strength"])
    }
    if (healthPercentage <= 10) {
        DamageBonus[sender] = (sender_stats["strength"]) * 1.5
    }

}


function checkCD(sender, technique) {
    if (sender == "player" && technique in playerAttackCooldowns) {
        return playerAttackCooldowns[technique] > 0

    } else if (sender == "ennemy" && technique in ennemyAttackCooldowns) {
        return ennemyAttackCooldowns[technique] > 0

    }
    else {
        return false
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

function setCoolDown(sender, technique, value) {
    if (sender == "player") {
        playerAttackCooldowns[technique] = value
    }
    else if (sender == "ennemy") {
        ennemyAttackCooldowns[technique] = value
    }
}

function attackEmitted(accuracy) {
    return (Math.floor(Math.random() * 100) + 1) <= accuracy
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
    return value >= cost
}

function checkIfIsPlayerTurn(nb_turn) {
    return nb_turn % 2 == 0;
}

function increaseTurn() {
    const whoplays = document.getElementById('whoplays')
    if (whoplays.textContent == "Player") {
        whoplays.textContent = "ennemy";
    } else {
        whoplays.textContent = "Player";
    };

    nb_turn += 1
    const turns_counter = document.getElementById('turns')
    turns_counter.textContent = nb_turn;
}
