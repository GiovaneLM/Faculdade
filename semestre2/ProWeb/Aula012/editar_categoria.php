
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
    <title>Editar Categoria</title>
</head>
<body class="bg-light">
    <div class="container mt-5">
        <?php 
            $id = $_GET['id_cat'];
            $categoria = buscarCategoria($conecta, $id);
            ?>
        <div class="row justify-content-center">
            <div class="col-md-6">
                <div class="card shadow-sm border-0">
                    <div class="card-header bg-primary text-white text-center py-3">
                        <h4 class="mb-0">Editar Categoria</h4>
                    </div>
                    <div class="card-body p-4">
                        <h5 class="text-center mb-4">Editando a categoria:<span class="text-primary"><?php echo htmlspecialchars($categoria['nome']); ?></span></h5>
                        <form action="" method="post">
                            <input type="hidden" name="id" value="<?php echo $categoria['id_cat']; ?>">
                            <div class="mb-3">
                                <label for="nome" class="form-label">Nome da Categoria</label>
                                <input type="text" name="nome" id="nome" class="form-control" value="<?php echo htmlspecialchars($categoria['nome']); ?>" required>
                            </div>
                            <div class="d-flex justify-content-between">
                                <a href="cad_categoria.php" class="btn btn-secondary">Voltar</a>
                                <button type="submit" name="atualizar" class="btn btn-success">Atualizar Categoria</button>
                            </div>
                        </form>
                        <?php EditarCategoria($conecta, $id); ?>
                    </div>
                </div>
            </div>
        </div>
    </div>
</body>
</html>
