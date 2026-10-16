<?php require_once "function.php"; ?>
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>editar usuario</title>
</head>
<body>
    <?php 
        $id = $_GET['id'];
        $usuario = buscaId($conecta,$id); 
    ?>
    <h1>editando o usuario <?php echo $usuario['nome']; ?></h1>
    <form action="" method="post">
        <input type="hidden" name="id" value="<?php echo $usuario['id']; ?>" >
        <input type="text" name="nome" value="<?php echo $usuario['nome']; ?>" >
        <input type="email" name="email" value="<?php echo $usuario['email']; ?>" >
        <input type="password" name="senha" placeholder="*****************">
        <input type="date" name="data" value="<?php echo $usuario['data']; ?>" >
        <button name="atualizar">Atualizar</button>
    </form>
    <?php updateUser($conecta, $id); ?>
</body>
</html>