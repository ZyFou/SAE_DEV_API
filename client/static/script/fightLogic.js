
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
        console.log("damage p1 -> p2 special Logic")
    } else if (EnemyMove == "special" && PlayerMove == "chargeKi") {
        console.log("damage p2 -> p1 special Logic")
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
        console.log("damage p2 -> p1 counter_attack Logic")
    } else if (EnemyMove == "counter_attack" && PlayerMove == "special") {
        console.log("damage p1 -> p1 counter_attack Logic")
    }

    // SPECIAL LOGIC
    if (PlayerMove == "special" && EnemyMove == PlayerMove) {
        console.log("p1 -> cost ki special Logic")
        console.log("p2 -> cost ki special Logic")
    }
}
