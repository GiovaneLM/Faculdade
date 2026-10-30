<?php 
    require_once "function.php" ;
?>
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-sRIl4kxILFvY47J16cr9ZwB07vP4J8+LH7qKQnuqkuIAvNWLzeN8tE5YBujZqJLB" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.bundle.min.js" integrity="sha384-FKyoEForCGlyvwx9Hj09JcYn3nv7wiPVlz7YYwJrWVcXK/BmnVDxM+D2scQbITxI" crossorigin="anonymous"></script>
    <title>Document</title>
</head>
<body>
    <a href="login.php"><button type="button" class="btn btn-success">area de trabalho</button></a>
<table border="1">
    <thead>
        <tr>
            <th>Nome</th>
            <th>descrição</th>
            <th>preço</th>
            <th>categoria</th>
            <th>data</th>
        </tr>
    </thead>
    <tbody>
    <?php $produtos = buscarProduto($conecta);
        foreach ($produtos as $produto) : ?>
        <tr>
            <td><?php echo $produto['nome'] ?></td>
            <td><?php echo $produto['descricao'] ?></td>
            <td><?php echo $produto['preco'] ?></td>
            <td><?php echo $produto['categoria_nome'] ?></td>
            <td><?php $data =date_create($produto['data']);echo date_format($data, "d/m/Y");?></td>
        </tr>
        <?php endforeach ?>
    </tbody>
</table>
</body>
</html>