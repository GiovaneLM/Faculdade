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
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.bundle.min.js"></script>
    <title>Editar Produto</title>
</head>
<body class="bg-light">
    <div class="container mt-5">
        <?php 
            $id = $_GET['id_pro'];
            $produto = buscarProduto($conecta, $id); 
        ?>
        <div class="row justify-content-center">
            <div class="col-md-7">
                <div class="card shadow-sm border-0">
                    <div class="card-header bg-primary text-white text-center py-3">
                        <h4 class="mb-0">Editar Produto</h4>
                    </div>
                    <div class="card-body p-4">
                        <h5 class="text-center mb-4">
                            Editando o produto:
                            <span class="text-primary"><?php echo htmlspecialchars($produto['nome']); ?></span>
                        </h5>
                        <form action="" method="post">
                            <input type="hidden" name="id" value="<?php echo $produto['id_pro']; ?>">
                            <div class="mb-3">
                                <label for="nome" class="form-label">Nome do Produto</label>
                                <input type="text" name="nome" id="nome" class="form-control" value="<?php echo htmlspecialchars($produto['nome']); ?>" required>
                            </div>
                            <div class="mb-3">
                                <label for="descricao" class="form-label">Descrição</label>
                                <textarea name="descricao" id="descricao" class="form-control" rows="3" required><?php echo htmlspecialchars($produto['descricao']); ?></textarea>
                            </div>
                            <div class="mb-3">
                                <label for="preco" class="form-label">Preço</label>
                                <input type="number" name="preco" id="preco" class="form-control" step="0.01" value="<?php echo $produto['preco']; ?>" required>
                            </div>
                            <div class="mb-3">
                                <label for="categoria" class="form-label">Categoria</label>
                                <select class="form-select" name="categoria" id="categoria" required>
                                    <option value="">Selecione uma categoria</option>
                                    <?php foreach (buscarCategorias($conecta) as $c) : ?>
                                        <option value="<?= $c['id_cat'] ?>" <?= ($c['id_cat']) ? 'selected' : '' ?>>
                                            <?= htmlspecialchars($c['nome']) ?>
                                        </option>
                                    <?php endforeach; ?>
                                    
                                </select>
                            </div>
                            <div class="mb-4">
                                <label for="data" class="form-label">Data</label>
                                <input type="date" name="data" id="data" class="form-control" value="<?php echo date('Y-m-d', strtotime($produto['data'])); ?>" required>
                            </div>
                            <div class="d-flex justify-content-between">
                                <a href="cad_produto.php" class="btn btn-secondary">Voltar</a>
                                <button type="submit" name="atualizar" class="btn btn-success">Atualizar Produto</button>
                            </div>
                        </form>
                        <?php EditarProduto($conecta, $id); ?>
                    </div>
                </div>
            </div>
        </div>
    </div>
</body>
</html>