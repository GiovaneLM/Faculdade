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
    <title>Editar Usuário</title>
</head>

<body class="bg-light">

    <div class="container mt-5">

        <?php 
            $id = $_GET['id_user'];
            $usuario = buscarUsuario($conecta, $id); 
        ?>

        <div class="row justify-content-center">
            <div class="col-md-6">
                <div class="card shadow-sm border-0">
                    <div class="card-header bg-primary text-white text-center py-3">
                        <h4 class="mb-0">Editar Usuário</h4>
                    </div>
                    <div class="card-body p-4">
                        <h5 class="text-center mb-4"> Editando o usuário:
                            <span class="text-primary">
                                <?php echo htmlspecialchars($usuario['nome']); ?>
                            </span>
                        </h5>
                        <form action="" method="post">
                            <input type="hidden" name="id" value="<?php echo $usuario['id_user']; ?>">
                            <div class="mb-3">
                                <label for="nome" class="form-label">Nome</label>
                                <input type="text" name="nome"  id="nome"  class="form-control" value="<?php echo htmlspecialchars($usuario['nome']); ?>" required >
                            </div>
                            <div class="mb-3">
                                <label for="email" class="form-label">E-mail</label>
                                <input type="email"  name="email"  id="email"class="form-control" value="<?php echo htmlspecialchars($usuario['email']); ?>"  required >
                            </div>
                            <div class="mb-3">
                                <label for="senha" class="form-label">Nova Senha</label>
                                <input type="password" name="senha" id="senha" class="form-control"placeholder="Digite uma nova senha">
                                <div class="form-text">Deixe vazio caso não queira alterar a senha.</div>
                            </div>
                            <div class="mb-4">
                                <label for="data" class="form-label">Data</label>
                                <input type="date" name="data" id="data" class="form-control" value="<?php echo htmlspecialchars($usuario['data']); ?>" >
                            </div>
                            <div class="d-flex justify-content-between">
                                <a href="cad_usuario.php" class="btn btn-secondary"> Voltar</a>
                                <button type="submit" name="atualizar" class="btn btn-success"> Atualizar Usuário</button>
                            </div>
                        </form>
                        <?php EditarUsuario($conecta, $id); ?>
                    </div>
                </div>
            </div>
        </div>
    </div>
</body>
</html>