<?php 
    require_once "function.php"; 
    session_start();
    isset($_SESSION['ativa']) ? "" : header("location:index.php");
?>
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-sRIl4kxILFvY47J16cr9ZwB07vP4J8+LH7qKQnuqkuIAvNWLzeN8tE5YBujZqJLB" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.bundle.min.js" integrity="sha384-FKyoEForCGlyvwx9Hj09JcYn3nv7wiPVlz7YYwJrWVcXK/BmnVDxM+D2scQbITxI" crossorigin="anonymous"></script>
    <title>Editar Usuario</title>
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