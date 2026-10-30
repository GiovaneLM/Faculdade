<?php 
    require_once "function.php" ;
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
    <title>usuario</title>
</head>
<body>
<a href="logout.php"><button type="button" class="btn btn-danger">Logout</button></a>

<div>
    <h1>Cadastrar Usuarios</h1>
    <?php cadastrarUsuario($conecta);  ?>
    <form method="post">
        <input type="text" name="nome" id="" placeholder="nome" require>
        <input type="email" name="email" id="" placeholder="email" require>
        <input type="password" name="senha" id="" placeholder="senha" require>
        <input type="submit" value="cadastrar Usuario" name="cadastrarU">
    </form>
</div>

<div>
    <h1>Cadastrar Categoria</h1>
    <?php cadastrarCategoria($conecta);  ?>
    <form method="post">
        <input type="text" name="nome" id="" placeholder="nome" require>
        <input type="submit" value="cadastrar Categoria" name="cadastrarC">
    </form>
</div>

<div>
    <h1>Cadastrar Produto</h1>
    <?php cadastrarProduto($conecta); ?>
    <form method="post">
        <input type="text" name="nome" placeholder="nome" required>
        <textarea name="descricao" placeholder="descrição" required></textarea>
        <input type="number" name="preco" placeholder="valor" step="0.01" min="0" required>
        <select name="categoria" required>
            <option value="">selecione uma categoria</option>
            <?php $categorias = buscarCategorias($conecta) ;
            foreach ($categorias as $c) : ?>
                <option value="<?= $c["id_cat"] ?>"><?= htmlspecialchars($c["nome"]) ?></option>
            <?php endforeach; ?>
        </select>
        <input type="submit" value="cadastrar Produto" name="cadastrarP">
    </form>
</div>



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
        //print_r($usuarios);
        foreach ($produtos as $produto) : ?>
        <tr>
            <td><?php echo $produto['nome'] ?></td>
            <td><?php echo $produto['descricao'] ?></td>
            <td><?php echo $produto['preco'] ?></td>
            <td><?php echo $produto['categoria_nome'] ?></td>
            <td><?php $data =date_create($produto['data']);echo date_format($data, "d/m/Y");?></td>
            <td>
                <a href="deletar.php?id=<?php echo $produto['id_pro']; ?>&nome=<?php echo $produto['nome']; ?>">excluir</a> - 
                <a href="editar.php?id=<?php echo $produto['id_pro']; ?>">editar</a>
            </td>
        </tr>
        <?php endforeach ?>
    </tbody>
</table>
</body>
</html>