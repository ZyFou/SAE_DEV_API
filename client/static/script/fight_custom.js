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


function action(sender, target, data, initial_health) {
    if (sender == "player" && target == "ennemy" && playerTurn(nb_turn)) {
        attackLogic("player", target, data)

    } else if (sender == "player" && target == "ennemy" && playerTurn(nb_turn) == false) {
        console.log("It's ennemy Turn")

    } else if (sender == "ennemy" && target == "player" && playerTurn(nb_turn) == false) {
        attackLogic("ennemy", target, data)

    } else if (sender == "ennemy" && target == "player" && playerTurn(nb_turn)) {
        console.log("It's Player Turn")
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

    if (target == "player") {
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

    var techWithCD = "Counter";
    if (!checkCD(sender, attack_name)) {
        if (hasEnoughEnergy(cost, energyBar.textContent)) {
            if (attackEmitted(accuracy)) {
                if (attack_name == "ChargeKi") {
                    updateEnergy(sender, 50)
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
                    setCoolDown(sender, attack_name, 2)

                    setLastAttack(sender, attack_name)

                } else {
                    updateEnergy(sender, cost * -1)
                    increaseTurn()
                    updateCoolDown(sender, techWithCD)

                    inflictDamages(sender, target, damages, bonus)
                    setLastAttack(sender, attack_name)
                }
            }
            else {
                if (attack_name == "Counter") {
                    setCoolDown(sender, attack_name, 2)
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

function inflictDamages(sender, target, attackValue, bonus) {
    var healthBar;
    var initalHealthValue;
    var sender_stats;
    var receiverStats;

    if (target == "player") {
        healthBar = document.getElementById('YourHealth');
        initalHealthValue = playerInitialHealth;
        sender_stats = playerStats;
        receiverStats = ennemyStats;
    } else {
        healthBar = document.getElementById('EnnemyHealth');
        initalHealthValue = ennemyInitialHealth;
        sender_stats = ennemyStats;
        receiverStats = playerStats;
    }

    var newDamages = attackValue + bonus;

    var finalDamages = calculateDamages(receiverStats, sender_stats, newDamages)

    if (sender == "player" && lastEnnemyAttack == "Guard") {
        alert("Damage Reduction")
        finalDamages = bonus
    } else if (sender == "ennemy" && lastPlayerAttack == "Guard") {
        alert("Damage Reduction")
        finalDamages = bonus
    }


    var health = parseInt(healthBar.textContent);
    var remainingHealth = Math.max(health - finalDamages, 0);
    var healthPercentage = (remainingHealth / initalHealthValue) * 100;

    healthBar.style.width = healthPercentage + '%';
    healthBar.textContent = remainingHealth;

    DamageBonusChecker(sender_stats, healthPercentage, healthBar, sender)
}

function DamageBonusChecker(sender_stats, healthPercentage, healthBar, sender) {
    if (healthPercentage <= 50) {
        healthBar.classList.remove('bg-success');
        healthBar.classList.add('bg-warning');
        DamageBonus[sender] = (sender_stats.strength) * 0.1
    }
    if (healthPercentage <= 25) {

        healthBar.classList.remove('bg-warning');
        healthBar.classList.add('bg-danger');
        DamageBonus[sender] = (sender_stats.strength) * 0.5
    }
    if (healthPercentage <= 10) {
        DamageBonus[sender] = (sender_stats.strength)
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
