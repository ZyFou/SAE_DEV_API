function displayAnimation(text, gif, duration, x = 400, y = 200) {
    Swal.fire({
        position: "top",

        title: text,
        text: "",
        imageUrl: gif,
        imageWidth: x,
        imageHeight: y,
        imageAlt: "Custom image",
        showConfirmButton: false,
        timer: duration
    });
}


function fightLogic(PlayerMove, EnemyMove, playerMoveData, enemyMoveData) {
    console.log("PlayerMove : ", PlayerMove, "EnemyMove : ", EnemyMove)

    var player = 'player';
    var enemy = 'ennemy';
    // NORMALATTACK
    if (PlayerMove == "normal_attack" && EnemyMove == PlayerMove) {
        attackLogic(player, enemy, playerMoveData)
        attackLogic(enemy, player, enemyMoveData)
    }

    if (PlayerMove == "normal_attack" && EnemyMove == "defense") {
        attackLogic(enemy, player, enemyMoveData)
        attackLogic(player, enemy, playerMoveData)

    } else if (EnemyMove == "normal_attack" && PlayerMove == "defense") {
        attackLogic(player, enemy, playerMoveData)
        attackLogic(enemy, player, enemyMoveData)

    }

    if (PlayerMove == "normal_attack" && EnemyMove == "counter_attack") {
        attackLogic(enemy, player, enemyMoveData)
        attackLogic(player, enemy, playerMoveData)
        // displayAnimation("L'adverse contre", enemyMoveData['image'], 2200)

    } else if (EnemyMove == "normal_attack" && PlayerMove == "counter_attack") {
        attackLogic(player, enemy, playerMoveData)
        attackLogic(enemy, player, enemyMoveData)
    }

    if (PlayerMove == "normal_attack" && EnemyMove == "special") {
        attackLogic(enemy, player, enemyMoveData)

    } else if (EnemyMove == "normal_attack" && PlayerMove == "special") {
        attackLogic(player, enemy, playerMoveData)

    }

    // DEFENSE LOGIC
    if (PlayerMove == "defense" && EnemyMove == PlayerMove) {
        attackLogic(player, enemy, playerMoveData)
        attackLogic(enemy, player, enemyMoveData)
        var gif = "https://i.pinimg.com/originals/bb/5a/51/bb5a51c34c62a307ffb0e180eadc260c.gif"
        displayAnimation("Vous vous défendez tout les 2.", gif, 2200, 400, 300)
    }

    if (PlayerMove == "defense" && EnemyMove == "special") {
        attackLogic(player, enemy, playerMoveData)
        attackLogic(enemy, player, enemyMoveData)

    } else if (EnemyMove == "defense" && PlayerMove == "special") {
        attackLogic(enemy, player, enemyMoveData)
        attackLogic(player, enemy, playerMoveData)
    }

    // CHARGE KI LOGIC
    if (PlayerMove == "chargeKi" && EnemyMove == PlayerMove) {
        attackLogic(player, enemy, playerMoveData)
        attackLogic(enemy, player, enemyMoveData)
    }

    if (PlayerMove == "normal_attack" && EnemyMove == "chargeKi") {
        attackLogic(player, enemy, playerMoveData)
        attackLogic(enemy, player, enemyMoveData)
    } else if (EnemyMove == "normal_attack" && PlayerMove == "chargeKi") {
        attackLogic(enemy, player, enemyMoveData)
        attackLogic(player, enemy, playerMoveData)
    }

    if (PlayerMove == "defense" && EnemyMove == "chargeKi") {
        attackLogic(player, enemy, playerMoveData)
        attackLogic(enemy, player, enemyMoveData)
    } else if (EnemyMove == "defense" && PlayerMove == "chargeKi") {
        attackLogic(enemy, player, enemyMoveData)
        attackLogic(player, enemy, playerMoveData)
    }

    if (PlayerMove == "counter_attack" && EnemyMove == "chargeKi") {
        attackLogic(player, enemy, playerMoveData)
        attackLogic(enemy, player, enemyMoveData)
    } else if (EnemyMove == "counter_attack" && PlayerMove == "chargeKi") {
        attackLogic(enemy, player, enemyMoveData)
        attackLogic(player, enemy, playerMoveData)
    }

    if (PlayerMove == "special" && EnemyMove == "chargeKi") {
        attackLogic(player, enemy, playerMoveData)

    } else if (EnemyMove == "special" && PlayerMove == "chargeKi") {
        attackLogic(enemy, player, enemyMoveData)

    }

    // counter_attack LOGIC
    if (PlayerMove == "counter_attack" && EnemyMove == PlayerMove) {
        attackLogic(player, enemy, playerMoveData)
        attackLogic(enemy, player, enemyMoveData)
    }

    if (PlayerMove == "counter_attack" && EnemyMove == "defense") {
        attackLogic(player, enemy, playerMoveData)
        attackLogic(enemy, player, enemyMoveData)
    } else if (EnemyMove == "counter_attack" && PlayerMove == "defense") {
        attackLogic(enemy, player, enemyMoveData)
        attackLogic(player, enemy, playerMoveData)
    }

    if (PlayerMove == "counter_attack" && EnemyMove == "special") {
        attackLogic(enemy, player, enemyMoveData)
        attackLogic(player, enemy, playerMoveData)
    } else if (EnemyMove == "counter_attack" && PlayerMove == "special") {
        attackLogic(player, enemy, playerMoveData)
        attackLogic(enemy, player, enemyMoveData)
    }

    // SPECIAL LOGIC
    if (PlayerMove == "special" && EnemyMove == PlayerMove) {
        attackLogic(player, enemy, playerMoveData)
        attackLogic(enemy, player, enemyMoveData)
    }
}
