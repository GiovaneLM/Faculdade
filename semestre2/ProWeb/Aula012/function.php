<?php

$server = "localhost";
$userDb = "root";
$passDb = "";
$nameDb = "lojinha";
$conecta = mysqli_connect($server,$userDb,$passDb,$nameDb);







function buscarProduto($conecta){
$sql = "SELECT p.id_pro, p.nome, p.descricao, p.preco, p.data,c.nome AS categoria_nome
    FROM produtos p
    INNER JOIN categorias c ON p.categoria = c.id_cat
    ORDER BY p.nome";
    $action = mysqli_query($conecta,$sql);
    $dados = mysqli_fetch_all($action, MYSQLI_ASSOC);
    return $dados;
}

function buscarCategorias($conecta){
    $sql = "SELECT id_cat, nome FROM categorias ORDER BY nome";
    $action = mysqli_query($conecta, $sql);
    return mysqli_fetch_all($action, MYSQLI_ASSOC);
}






function cadastrarCategoria($conecta){
    if(isset($_POST['cadastrarC'])){
        $nome = mysqli_real_escape_string($conecta,$_POST['nome']);
        $erros = [];
        if (empty($nome)){
            echo "preencha corretamente o campo";
        }else{
            $sql = "INSERT INTO categorias(nome,data) VALUES ('$nome',NOW())";
            $action = mysqli_query($conecta,$sql);
            if ($action) {
                echo "categoria cadastrada com sucesso";
            }else{
                echo "erro ao inserir";
            }
        }
    }
}

function cadastrarProduto($conecta){
    if(isset($_POST['cadastrarP'])){
        $nome = mysqli_real_escape_string($conecta,$_POST['nome']);
        $descricao = mysqli_real_escape_string($conecta,$_POST['descricao']);
        $preco = filter_input(INPUT_POST,"preco",FILTER_VALIDATE_FLOAT);
        $categoria = filter_input(INPUT_POST,"categoria",FILTER_VALIDATE_INT);
        $erros = [];
        if (empty($nome)){
            echo "preencha corretamente o campo";
        }else{
            $sql = "INSERT INTO produtos(nome,descricao,preco,categoria,data) VALUES ('$nome','$descricao',$preco,$categoria,NOW())";
            $action = mysqli_query($conecta,$sql);
            if ($action) {
                echo "categoria cadastrada com sucesso";
            }else{
                echo "erro ao inserir";
            }
        }
    }
}


function cadastrarUsuario($conecta){
    if(isset($_POST['cadastrarU'])){
        $nome = mysqli_real_escape_string($conecta,$_POST['nome']);
        $email = filter_input(INPUT_POST,'email',FILTER_VALIDATE_EMAIL);
        $senha = password_hash($_POST['senha'],PASSWORD_DEFAULT);
        $erros = [];
        if (empty($nome) or empty($email) or empty($senha)) {
            echo "preencha corretamente todos os campos";
        }else{
            $sql = "INSERT INTO usuarios(nome,email,senha,data) VALUES ('$nome','$email','$senha',NOW())";
            $action = mysqli_query($conecta,$sql);
            if ($action) {
                echo "usuario inserido com sucesso";
            }else{
                echo "erro ao inserir";
            }
        }
    }
}


function login($conecta){
    if (isset($_POST['logar'])) {
        $email = filter_input(INPUT_POST,'email',FILTER_VALIDATE_EMAIL);
        $senha = $_POST['senha'];
        if (!empty($email) and !empty($senha)) {
            $sql = "SELECT * FROM usuarios WHERE email = '$email' ";
            $action = mysqli_query($conecta, $sql);
            $retorno = mysqli_fetch_assoc($action);
            if (!empty($retorno['email']) and password_verify($senha,$retorno['senha'])) {
                //inicia a sessao para proteger as paginas
                session_start();
                $_SESSION['email'] = $retorno['email'];
                $_SESSION['nome'] = $retorno['nome'];
                $_SESSION['ativa'] = true;
                //redireciona apos o login
                header("location:usuario.php");
            }else{
                echo "usuario ou senha incorretos";
            }
        }else{
            echo "usuario ou senha invalidos";
        }
    }
}