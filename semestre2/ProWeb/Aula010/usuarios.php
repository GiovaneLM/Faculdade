<?php require_once "function.php"; ?>
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Aula 10</title>
</head>
<body>
    <h1>Lista de Usuários</h1>
    <h2><?php insertUsers($conecta);  ?></h2>
    <form method="post">
        <input type="text" name="nome" id="" placeholder="nome" require>
        <input type="email" name="email" id="" placeholder="email" require>
        <input type="password" name="senha" id="" placeholder="senha" require>
        <input type="submit" value="cadastrar" name="cadastrar">
    </form>









    <table border="1">
        <thead>
            <tr>
                <th>Nome</th>
                <th>E_mail</th>
                <th>Data Cadastro</th>
            </tr>
        </thead>
        <tbody>
        <?php $usuarios = buscar($conecta);
            //print_r($usuarios);
            foreach ($usuarios as $usuario) : ?>
            <tr>
                <td><?php echo $usuario['nome'] ?></td>
                <td><?php echo $usuario['email'] ?></td>
                <td><?php $data =date_create($usuario['data']);
                        echo date_format($data, "d/m/Y");?></td>
            </tr>
            <?php endforeach ?>
        </tbody>
    </table>
</body>
</html>