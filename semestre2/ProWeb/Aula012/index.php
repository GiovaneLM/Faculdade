<?php 
    require_once "function.php";
    criarTabelaCategorias($conecta);
    criarTabelaProdutos($conecta);
    criarTabelaUsuarios($conecta);
    criarAdminPadrao($conecta);
?>
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-sRIl4kxILFvY47J16cr9ZwB07vP4J8+LH7qKQnuqkuIAvNWLzeN8tE5YBujZqJLB" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.bundle.min.js" integrity="sha384-FKyoEForCGlyvwx9Hj09JcYn3nv7wiPVlz7YYwJrWVcXK/BmnVDxM+D2scQbITxI" crossorigin="anonymous"></script>
    <title>Produtos</title>
</head>
<body class="bg-light">
    <div class="container mt-5">
        <div class="d-flex justify-content-between align-items-center mb-4">
            <h2 class="fw-bold text-dark">Lista de Produtos</h2>
            <a href="login.php" class="btn btn-success">Área de trabalho</a>
        </div>
        <div class="card shadow-sm border-0">
            <div class="card-header bg-primary text-white py-3">
                <h5 class="mb-0">Produtos cadastrados</h5>
            </div>
            <div class="card-body">
                <div class="table-responsive">
                    <table class="table table-striped table-hover table-bordered align-middle mb-0">
                        <thead class="table-dark">
                            <tr>
                                <th>Nome</th>
                                <th>Descrição</th>
                                <th>Preço</th>
                                <th>Categoria</th>
                                <th>Data</th>
                            </tr>
                        </thead>
                        <tbody>
                        <?php $produtos = buscarProdutos($conecta);foreach ($produtos as $produto) :?>
                            <tr>
                                <td><?php echo $produto['nome'] ?></td>
                                <td><?php echo $produto['descricao'] ?></td>
                                <td>R$ <?php echo number_format($produto['preco']) ?></td>
                                <td><?php echo $produto['categoria_nome'] ?></td>
                                <td><?php $data = date_create($produto['data']);echo date_format($data, "d/m/Y");?></td>
                            </tr>
                        <?php endforeach ?>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    </div>
</body>
</html>