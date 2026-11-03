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
    <title>Categorias</title>
</head>
<body class="bg-light">
<div class="container py-4">
    <div class="d-flex justify-content-between align-items-center mb-4">
        <h1 class="h3 mb-0">Categorias</h1>
        <a href="usuario.php" class="btn btn-outline-secondary">Voltar</a>
    </div>
    <div class="card shadow-sm mb-4">
        <div class="card-body">
            <h2 class="h5 mb-3">Cadastrar categoria</h2>
            <div class="mb-2"><?php cadastrarCategoria($conecta); ?></div>
            <form method="post" class="row g-2">
                <div class="col-md-10">
                    <input type="text" class="form-control" name="nome" placeholder="nome" required>
                </div>
                <div class="col-md-2 d-grid">
                    <button class="btn btn-success" name="cadastrarC">Cadastrar</button>
                </div>
            </form>
        </div>
    </div>
    <div class="table-responsive">
        <table class="table table-striped table-bordered bg-white">
            <thead class="table-dark">
                <tr>
                    <th>Nome</th>
                    <th>Data</th>
                    <th>Ações</th>
                </tr>
            </thead>
            <tbody>
            <?php foreach (buscarCategorias($conecta) as $c) : ?>
                <tr>
                    <td><?= htmlspecialchars($c['nome']) ?></td>
                    <td><?= $c['data'] ? date('d/m/Y', strtotime($c['data'])) : '-' ?></td>
                    <td>
                        <a href="deletar.php?id=<?= $c['id_cat'] ?>&nome=<?= urlencode($c['nome']) ?>" class="btn btn-sm btn-outline-danger">Excluir</a>
                        <a href="editar.php?id=<?= $c['id_cat'] ?>" class="btn btn-sm btn-outline-primary">Editar</a>
                    </td>
                </tr>
            <?php endforeach; ?>
            </tbody>
        </table>
</div>
</body>
</html>