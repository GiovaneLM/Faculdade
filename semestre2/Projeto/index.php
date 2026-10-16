<?php require_once "function.php"; ?>
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <div>
        <form action="" method="post">
            <label for="nome">Nome:</label>
            <input type="text" name="nome" id="nome" require placeholder="Nome">
            <label for="email">E-mail:</label>
            <input type="email" name="email" id="email" require placeholder="E-mail">
            <label for="senha">Senha:</label>
            <input type="password" name="senha" id="senha" require placeholder="Senha">
            <button type="cadastrar">Cadastrar</button>
        </form>
        <form action="" method="post">
            <label for="email">E-mail:</label>
            <input type="email" name="email" id="email" require placeholder="E-mail">
            <label for="senha">Senha:</label>
            <input type="password" name="senha" id="senha" require placeholder="Senha">
            <button type="logar">Logar</button>
        </form>
    </div>
</body>
</html>