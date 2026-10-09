<?php
$server = "localhost";
$userDb = "root";
$passDb = "";
$nameDb = "roblox";
$conecta = mysqli_connect($server,$userDb,$passDb,$nameDb);


function buscar($conecta){
    $sql = "SELECT * FROM usuarios ORDER BY nome";
    $action = mysqli_query($conecta,$sql);
    $dados = mysqli_fetch_all($action, MYSQLI_ASSOC);
    return $dados;
}

function insertUsers($conecta){
    if(isset($_POST['cadastrar'])){
        $nome = mysqli_real_escape_string($conecta,$_POST['nome']);
        $email = filter_input(INPUT_POST,'email',FILTER_VALIDATE_EMAIL);
        $senha = password_hash($_POST['senha'],PASSWORD_DEFAULT);
        $erros = [];
        if (empty($nome) or empty($email) or empty($senha)) {
            echo "preencha corretamente todos os campos";
        }else{
            echo $sql = "INSERT INTO usuarios(nome,email,senha,data) VALUES ('$nome','$email','$senha',NOW())";
            $action = mysqli_query($conecta,$sql);
            if ($action) {
                echo "usuario inserido com sucesso";
            }else{
                echo "erro ao inserir";
            }
        }
    }
}

