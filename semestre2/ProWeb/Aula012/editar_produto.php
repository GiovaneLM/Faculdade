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
    <title>Editar Produto</title>
</head>
<body>
    <?php 
        $id = $_GET['id_pro'];
        $produto = buscarProduto($conecta,$id); 
    ?>
    <?php
        print_r($produto);
    ?>
    <h1>editando o produto <?php echo $produto['nome']; ?></h1>
    <form action="" method="post">
        <input type="hidden" name="id" value="<?php echo $produto['id_pro']; ?>" >
        <input type="text" name="nome" value="<?php echo $produto['nome']; ?>" >
        <textarea type="text" name="descricao" value="<?php echo $produto['descricao']; ?>" >
        <input type="number" name="preco" id="" value="<?php echo $produto['preco']; ?>">
            <select class="form-select" name="categoria" required>
                <option value="">categoria</option>
                <?php foreach (buscarCategorias($conecta) as $c) : ?>
                    <option value="<?= $c['id_cat'] ?>"><?= $c['nome'] ?></option>
                <?php endforeach; ?>
            </select>
        <input type="date" name="data" value="<?php echo $produto['data']; ?>" >
        <button name="atualizar">Atualizar</button>
    </form>
    <?php EditarProduto($conecta, $id); ?>
</body>
</html>