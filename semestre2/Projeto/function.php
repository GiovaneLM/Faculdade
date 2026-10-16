<?php

$server = "localhost";
$userDb = "root";
$passDb = "";
$nameDb = "gachalive";
$conecta = mysqli_connect($server,$userDb,$passDb,$nameDb);


function cadastrar($conecta){
    if(isset($_POST['cadastrar'])){
        $nome = mysqli_real_escape_string($conecta,$_POST['nome']);
        $email = filter_input(INPUT_POST,'email',FILTER_VALIDATE_EMAIL);
        $senha = password_hash($_POST['senha'],PASSWORD_DEFAULT);
        $erros = [];
        if(empty($nome) or empty($email) or empyt($senha))
    }
}