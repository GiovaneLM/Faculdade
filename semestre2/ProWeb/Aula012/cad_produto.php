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
    <title>Produtos</title>
</head>
<body class="bg-light">

<div class="container py-4">

    <div class="d-flex justify-content-between align-items-center mb-4">
        <h1 class="h3 mb-0">Produtos</h1>
        <a href="usuario.php" class="btn btn-outline-secondary">Voltar</a>
    </div>

    <div class="card shadow-sm mb-4">
        <div class="card-body">
            <h2 class="h5 mb-3">Cadastrar produto</h2>
            <div class="mb-2"><?php cadastrarProduto($conecta); ?></div>
            <form method="post" class="row g-2">
                <div class="col-md-3">
                    <input type="text" class="form-control" name="nome" placeholder="nome" required>
                </div>
                <div class="col-md-3">
                    <textarea class="form-control" name="descricao" placeholder="descrição" rows="1" required></textarea>
                </div>
                <div class="col-md-2">
                    <input type="number" class="form-control" name="preco" placeholder="valor" step="0.01" min="0" required>
                </div>
                <div class="col-md-2">
                    <select class="form-select" name="categoria" required>
                        <option value="">categoria</option>
                        <?php foreach (buscarCategorias($conecta) as $c) : ?>
                            <option value="<?= $c['id_cat'] ?>"><?= htmlspecialchars($c['nome']) ?></option>
                        <?php endforeach; ?>
                    </select>
                </div>
                <div class="col-md-2 d-grid">
                    <button class="btn btn-success" name="cadastrarP">Cadastrar</button>
                </div>
            </form>
        </div>
    </div>

    <div class="table-responsive">
        <table class="table table-striped table-bordered bg-white">
            <thead class="table-dark">
                <tr>
                    <th>Nome</th>
                    <th>Descrição</th>
                    <th>Preço</th>
                    <th>Categoria</th>
                    <th>Data</th>
                    <th>Ações</th>
                </tr>
            </thead>
            <tbody>
            <?php foreach (buscarProduto($conecta) as $p) : ?>
                <tr>
                    <td><?= htmlspecialchars($p['nome']) ?></td>
                    <td><?= htmlspecialchars($p['descricao']) ?></td>
                    <td>R$ <?= number_format($p['preco'], 2, ',', '.') ?></td>
                    <td><?= htmlspecialchars($p['categoria_nome']) ?></td>
                    <td><?= $p['data'] ? date('d/m/Y', strtotime($p['data'])) : '-' ?></td>
                    <td>
                        <a href="deletar_produto.php?id_pro=<?= $p['id_pro'] ?>&nome=<?= urlencode($p['nome']) ?>" class="btn btn-sm btn-outline-danger">Excluir</a>
                        <a href="editar.php?id=<?= $p['id_pro'] ?>" class="btn btn-sm btn-outline-primary">Editar</a>
                    </td>
                </tr>
            <?php endforeach; ?>
            </tbody>
        </table>
    </div>
</div>
</body>
</html>