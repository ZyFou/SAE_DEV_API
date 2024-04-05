var nb_turn = 0;


var lastPlayerAttack;
var playerAttackCooldowns = {
    "Counter": 0,
    "Guard": 0
};

var lastEnnemyAttack;
var ennemyAttackCooldowns = {
    "Counter": 0,
    "Guard": 0
};

var DamageBonus = {
    'player': 0,
    'ennemy': 0
}

var ReductionBonus = {
    'player': 0,
    'ennemy': 0
}


let playerHasPlayed = false
let ennemyHasPlayed = false

var playerMove;
var playerMoveData;

var ennemyMove;
var ennemyMoveData;





// AI PART AI PART AI PART PART AI PART AI PART PART AI PART AI PART
// AI PART AI PART AI PART PART AI PART AI PART PART AI PART AI PART
// AI PART AI PART AI PART PART AI PART AI PART PART AI PART AI PART
// AI PART AI PART AI PART PART AI PART AI PART PART AI PART AI PART
// AI PART AI PART AI PART PART AI PART AI PART PART AI PART AI PART
// AI PART AI PART AI PART PART AI PART AI PART PART AI PART AI PART




function triggerAi(sender, techniques, initial_health, AIEnergy, AISmartness, playerEnergy) {
    var aiChoice = Math.floor(Math.random() * techniques.length);
    var technique_used;

    technique_used = AIBrain(sender, techniques, aiChoice, AIEnergy, AISmartness, initial_health, technique_used, playerEnergy);
    console.log("Ai Action : ", technique_used.name)
}

function getAIHealth() {
    return parseInt(document.getElementById('EnnemyHealth').textContent)
}

function getPlayerHealth() {
    return parseInt(document.getElementById('YourHealth').textContent)
}


function checkHealth() {
    var YourPickAttacks = document.getElementById('YourPickAttacks')
    var EnnemyAttacks = document.getElementById('EnnemyAttacks')


    if (getPlayerHealth() == 0) {
        Swal.fire({
            icon: "error",
            title: "Vous avez perdu !",
            text: "",
        });
        YourPickAttacks.style.display = 'none'
        EnnemyAttacks.style.display = 'none'

        setTimeout(() => {
            window.location.href = "/gameMode";
        }, 3000);
    }
    else if (getAIHealth() == 0) {
        Swal.fire({
            icon: "error",
            title: "L'adversaire a perdu !",
            text: "",
        });

        YourPickAttacks.style.display = 'none'
        EnnemyAttacks.style.display = 'none'

        setTimeout(() => {
            window.location.href = "/gameMode";
        }, 3000);
    }
}

function getRandomNumber(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

function AIBrain(sender, techniques, aiChoice, AIEnergy, AISmartness, initial_health, technique_used, playerEnergy) {
    var AIMax = 10
    console.log(techniques)
    var newAISmartness = AISmartness;

    if (AISmartness < 1) {
        newAISmartness = 1
    } else if (AISmartness > 10) {
        newAISmartness = AIMax
    }
    var AISmartRoll = Math.floor(Math.random() * AIMax) + 1
    var AISmart = false;

    console.log(newAISmartness)

    if (AISmartRoll <= newAISmartness) {
        AISmart = true
    } else {
        AISmart = false
    }

    if (AISmart) {
        console.log('DUMB');

        var AiHealth = getAIHealth();
        var playerHealth = getPlayerHealth();


        if (playerHealth > AiHealth) {
            var roll = getRandomNumber(1, 3)
            if (roll == 1) {
                var favorisedMoveId = 1; // Guard
                if (!checkCD(sender, techniques[favorisedMoveId].name) && hasEnoughEnergy(techniques[favorisedMoveId].cost, AIEnergy)) {
                    action(sender, techniques[favorisedMoveId], initial_health);
                    return techniques[favorisedMoveId];
                }
            } else if (roll == 2) {
                favorisedMoveId = 0; // Normal Attack
                if (hasEnoughEnergy(techniques[favorisedMoveId].cost, AIEnergy)) {
                    action(sender, techniques[favorisedMoveId], initial_health);
                    return techniques[favorisedMoveId];
                }
            }

            favorisedMoveId = 2; // Counter
            if (!checkCD(sender, techniques[favorisedMoveId].name) && hasEnoughEnergy(techniques[favorisedMoveId].cost, AIEnergy)) {
                action(sender, techniques[favorisedMoveId], initial_health);
                return techniques[favorisedMoveId];
            }

        } else {
            var favorisedMoveId = 0; // Normal Attack
            if (hasEnoughEnergy(techniques[favorisedMoveId].cost, AIEnergy)) {
                action(sender, techniques[favorisedMoveId], initial_health);
                return techniques[favorisedMoveId];
            }
        }

        if (AIEnergy <= playerEnergy && hasEnoughEnergy(techniques[3].cost, AIEnergy)) {
            action(sender, techniques[3], initial_health);
            return techniques[3];
        }

        favorisedMoveId = 3; // ChargeKi
        action(sender, techniques[favorisedMoveId], initial_health);
        return techniques[favorisedMoveId];


    } else {
        console.log("SMART")
        if (!checkCD(sender, techniques[aiChoice].name)) {
            if (hasEnoughEnergy(techniques[aiChoice].cost, AIEnergy)) {
                action(sender, techniques[aiChoice], initial_health);
                technique_used = techniques[aiChoice];
            } else {
                action(sender, techniques[3], initial_health);
                technique_used = techniques[3];
            }
        } else {
            if (hasEnoughEnergy(techniques[0].cost, AIEnergy)) {
                action(sender, techniques[0], initial_health);
                technique_used = techniques[0];
            } else {
                action(sender, techniques[3], initial_health);
                technique_used = techniques[3];
            }
        }
        return technique_used;
    }


}




// AI PART AI PART AI PART PART AI PART AI PART PART AI PART AI PART
// AI PART AI PART AI PART PART AI PART AI PART PART AI PART AI PART
// AI PART AI PART AI PART PART AI PART AI PART PART AI PART AI PART
// AI PART AI PART AI PART PART AI PART AI PART PART AI PART AI PART
// AI PART AI PART AI PART PART AI PART AI PART PART AI PART AI PART
// AI PART AI PART AI PART PART AI PART AI PART PART AI PART AI PART






function action(sender, data, initial_health) {
    var energy_value = sender == "player" ? parseInt(document.getElementById('YourEnergy').textContent) : parseInt(document.getElementById('EnnemyEnergy').textContent);

    if (GameMode == "solo" && sender == "player") {
        var AIEnergy = parseInt(document.getElementById('EnnemyEnergy').textContent);
        var playerEnergy = parseInt(document.getElementById('YourEnergy').textContent);
        triggerAi('ennemy', AI_Techniques, AI_Health, AIEnergy, FixedAISmartness, playerEnergy)
    }

    sender == 'player' ? playerHasPlayed = true : ennemyHasPlayed = true;
    if (sender == "player" && playerHasPlayed && !checkCD(sender, data.name)) {
        if (hasEnoughEnergy(data.cost, energy_value)) {
            playerMove = data.type;
            playerMoveData = data;
        } else {
            Swal.fire({
                icon: "info",
                position: "top",
                title: "Pas assez de Ki !",
                text: "Vous n'avez pas assez d'énergie.",
                showConfirmButton: false,
                timer: 1500
            });
            playerHasPlayed = false;
        }
    }
    else if (checkCD(sender, data.name)) {
        playerHasPlayed = false;
        console.log("This technique is on CD");
        Swal.fire({
            icon: "info",
            position: "top",
            title: "Technique en Coodldown !",
            text: "Vous ne pouvez  pas utiliser cette technique.",
            showConfirmButton: false,
            timer: 1500
        });
    }

    if (sender == "ennemy" && ennemyHasPlayed && !checkCD(sender, data.name)) {
        if (hasEnoughEnergy(data.cost, energy_value)) {
            ennemyMove = data.type;
            ennemyMoveData = data;
        } else {
            Swal.fire({
                icon: "info",
                position: "top",
                title: "Pas assez de Ki !",
                text: "Vous n'avez pas assez d'énergie.",
                showConfirmButton: false,
                timer: 1500
            });
            ennemyHasPlayed = false;
        }
    }
    else if (checkCD(sender, data.name)) {
        ennemyHasPlayed = false;
        Swal.fire({
            icon: "info",
            position: "top",
            title: "Technique en Coodldown !",
            text: "Vous ne pouvez  pas utiliser cette technique.",
            showConfirmButton: false,
            timer: 1500
        });
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

    if (!checkCD(sender, attack_name)) {
        if (hasEnoughEnergy(cost, energyBar.textContent)) {
            if (attackEmitted(accuracy)) {
                if (attack_name == "ChargeKi") {
                    updateEnergy(sender, 50)
                    increaseTurn()
                    updateCoolDown(sender)

                    setLastAttack(sender, attack_name)

                } else if (attack_name == "Guard") {
                    updateEnergy(sender, cost * -1)
                    increaseTurn()
                    setCoolDown(sender, attack_name, cooldown)

                    updateCoolDown(sender)

                    setLastAttack(sender, attack_name)

                } else if (attack_name == "Counter") {
                    updateEnergy(sender, cost * -1)
                    increaseTurn()
                    setCoolDown(sender, attack_name, cooldown)

                    setLastAttack(sender, attack_name)

                } else {
                    updateEnergy(sender, cost * -1)
                    increaseTurn()
                    updateCoolDown(sender)
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
    checkHealth()
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
        var animation = StorageTechniques[1].image;
        displayAnimation("L'adversaire se défend.", animation, 2000)

    } else if (sender == "ennemy" && lastPlayerAttack == "Guard") {
        finalDamages = bonus
        var animation = StorageTechniques[1].image;
        displayAnimation("Vous vous défendez.", animation, 2000)

    } else if (sender == "player" && lastEnnemyAttack == "Counter") {
        var animation = StorageTechniques[2].image;
        displayAnimation("L'adversaire contre.", animation, 2200)
        finalDamages = 0;

        displayDamages("ennemy", "player", calculateDamages(playerStats, ennemyStats, (attackDamage * 1.5) + DamageBonus["player"]), true);

    } else if (sender == "ennemy" && lastPlayerAttack == "Counter") {
        finalDamages = 0;
        var animation = StorageTechniques[2].image;
        displayAnimation("Vous contrez.", animation, 2200)

        displayDamages("player", "ennemy", calculateDamages(ennemyStats, playerStats, (attackDamage * 1.5) + DamageBonus["ennemy"]), true);
    }

    displayDamages(sender, target, finalDamages);

}


function displayDamages(sender, target, finalDamages, counter = false, clash = false) {
    var healthBar;
    var initalHealthValue;

    var sender_stats;
    var target_stats;

    if (target == "player") {
        healthBar = document.getElementById('YourHealth');
        initalHealthValue = playerInitialHealth;
        target_stats = playerStats;
    } else {
        healthBar = document.getElementById('EnnemyHealth');
        initalHealthValue = ennemyInitialHealth;
        target_stats = ennemyStats;
    }

    var health = parseInt(healthBar.textContent);
    var remainingHealth = Math.max(health - finalDamages, 0);

    var healthPercentage = (remainingHealth / initalHealthValue) * 100;


    healthBar.style.width = healthPercentage + '%';
    healthBar.textContent = remainingHealth;

    if (finalDamages != 0 && finalDamages != DamageBonus[sender] && !counter) {
        var animation = "https://qph.cf2.quoracdn.net/main-qimg-194420cf0a61b6c1a2b0cf3508f74879"
        displayAnimation("L'attaque fait mouche", animation, 2000)
    }

    DamageBonusChecker(target_stats, healthPercentage, healthBar, target);

}

function DamageBonusChecker(target_stats, healthPercentage, healthBar, target) {
    // console.log(sender_stats, healthPercentage, healthBar, sender)

    target_stats = JSON.parse(target_stats);

    if (healthPercentage <= 75) {
        healthBar.classList.remove('bg-success');
        healthBar.classList.add('bg-info');
        DamageBonus[target] = (target_stats["strength"]) * 0.1
    }
    if (healthPercentage <= 50) {
        healthBar.classList.remove('bg-info');
        healthBar.classList.add('bg-warning');
        DamageBonus[target] = (target_stats["strength"]) * 0.5
    }
    if (healthPercentage <= 25) {
        healthBar.classList.remove('bg-warning');
        healthBar.classList.add('bg-danger');
        DamageBonus[target] = (target_stats["strength"])
    }
    if (healthPercentage <= 10) {
        DamageBonus[target] = (target_stats["strength"]) * 1.5
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

function updateCoolDown(sender) {
    var attackCooldowns = sender == "player" ? playerAttackCooldowns : ennemyAttackCooldowns;

    for (var technique in attackCooldowns) {
        if (attackCooldowns.hasOwnProperty(technique) && attackCooldowns[technique] > 0) {
            attackCooldowns[technique]--;
        }
    }
}

function setCoolDown(sender, technique, value) {
    console.log(technique)
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

    nb_turn += 0.5
    const turns_counter = document.getElementById('turns')
    turns_counter.textContent = nb_turn;
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