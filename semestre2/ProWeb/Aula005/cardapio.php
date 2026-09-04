<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="style.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,100..900;1,100..900&display=swap" rel="stylesheet">
    <title>Restaurante - joao protagonista</title>
</head>
<body>
    <!-- topo do site -->
    <?php require "layout/topo.php"; ?>

    <main>
        <h1 style="margin-top: 100px">conheça nosso cardapio completo</h1>
    </main>
    <section class="pratos">
        <div class="container">
            <div class="coluna">
                <div class="imagem"><img src="img/prato.jpg" alt=""></div>
                <h3>receita um</h3>
            </div>

            <div class="coluna">
                <div class="imagem"><img src="img/prato.jpg" alt=""></div>
                <h3>receita dois</h3>
            </div>

            <div class="coluna">
                <div class="imagem"><img src="img/prato.jpg" alt=""></div>
                <h3>receita tres</h3>
            </div>

            <div class="coluna">
                <div class="imagem"><img src="img/prato.jpg" alt=""></div>
                <h3>receita quatro</h3>
            </div>
        </div>
    </section>
    <footer class="rodape">
        <?php include "layout/menu.php" ?>
        <?php include "layout/rodape.php" ?>
    </footer>
</body>
</html>