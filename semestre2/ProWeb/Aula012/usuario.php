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
    <title>Painel</title>
</head>
<body class="bg-light">
<div class="container min-vh-100 d-flex align-items-center justify-content-center">
    <div class="card shadow-sm w-100" style="max-width: 400px;">
        <div class="card-body p-4 text-center">
            <h1 class="h3 mb-4">Painel</h1>
            <div class="d-grid gap-2">
                <a href="cad_categoria.php" class="btn btn-primary">Categorias</a>
                <a href="cad_produto.php" class="btn btn-primary">Produtos</a>
                <a href="cad_usuario.php" class="btn btn-primary">Usuários</a>
                <a href="logout.php" class="btn btn-danger">Logout</a>
            </div>
        </div>
    </div>
</div>
</body>
</html>