<?php require_once "function.php" ?>
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>deletar usuario</title>
</head>
<body>
    <?php if (isset($_GET['id']) and !empty($_GET['nome'])) : 
        $id = $_GET['id'];
    ?>
    <h1>
        tem certeza que deseja excluir o usuario 
        <?php echo $_GET['nome']; ?>?
    </h1>
    <form action="" method="post">
        <input type="text" name="id" id="" value="<?php echo $id ?>" hidden>
        <button name="excluir">Deletar Usuario</button>
    </form>
    <?php 
        if (isset($_POST['excluir'])) {
            $id = filter_input(INPUT_POST,'id',FILTER_VALIDATE_INT);
            delete($conecta, $id);
        }
    ?>
<?php endif ?>
</body>
</html>