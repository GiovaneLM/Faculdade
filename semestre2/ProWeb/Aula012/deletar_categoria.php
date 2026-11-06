
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
    <title>Deletar Categoria</title>
</head>
<body class="bg-light">
    <div class="container mt-5">
        <?php if (isset($_GET['id_cat']) and !empty($_GET['nome'])) : $id = $_GET['id_cat'];?>
            <div class="row justify-content-center">
                <div class="col-md-6">
                    <div class="card shadow-sm border-0">
                        <div class="card-header bg-danger text-white text-center py-3">
                            <h4 class="mb-0">Excluir Categoria</h4>
                        </div>
                        <div class="card-body text-center p-4">
                            <h5 class="mb-3">Tem certeza que deseja excluir esta categoria?</h5>
                            <p class="fs-5 fw-bold text-danger">
                                <?php echo htmlspecialchars($_GET['nome']); ?>
                            </p>
                            <p class="text-muted">Essa ação poderá ser permanente. </p>
                            <form action="" method="post">
                                <input type="hidden" name="id" value="<?php echo $id ?>">
                                <div class="d-flex justify-content-center gap-2">
                                    <a href="cad_categoria.php" class="btn btn-primary"> Voltar</a>
                                    <button type="submit" name="excluir" class="btn btn-danger">Deletar Categoria</button>
                                </div>
                            </form>
                        </div>
                    </div>
                </div>
            </div>
            <?php 
                if (isset($_POST['excluir'])) {
                    $id = filter_input(INPUT_POST, 'id', FILTER_VALIDATE_INT);
                    deleteCategoria($conecta, $id);
                }
            ?>
        <?php endif ?>
    </div>
</body>
</html>