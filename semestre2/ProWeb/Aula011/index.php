<?php require_once "function.php" ?>
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="css/style.css">
    <title>login e senha</title>
</head>
<body>
    
    <div class="form">
        <form action="" method="post">
            <input type="email" name="email" id="" placeholder="seu email">
            <input type="password" name="senha" id="" placeholder="sua senha">
            <div class="aviso"><?php login($conecta); ?></div>
            <button name="logar">acessar</button>
        </form>
    </div>
</body>
</html>