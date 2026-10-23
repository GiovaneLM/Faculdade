<?php
$server = "localhost";
$userDb = "root";
$passDb = "";
$nameDb = "roblox";
$conecta = mysqli_connect($server,$userDb,$passDb,$nameDb);




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
                header("location:usuarios.php");
            }else{
                echo "usuario ou senha incorretos";
            }
        }else{
            echo "usuario ou senha invalidos";
        }
    }
}








function buscaId($conecta, $id){
    $id = filter_var($id,FILTER_VALIDATE_INT);
    if(!empty($id)){
        $sql = "SELECT * FROM usuarios WHERE id = $id";
        $action = mysqli_query($conecta,$sql);
        $dados = mysqli_fetch_assoc($action);
        return $dados;
    }
}


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

function delete($conecta, $id){
    if (is_numeric($id) and !empty($id)) {
        $sql = "DELETE FROM usuarios WHERE id = $id";
        $action = mysqli_query($conecta,$sql);
        if ($action) {
            echo "usuario deletado com sucesso!";
            //echo "<script> window.location.ref = 'isiarios.php' </script>";
            header("Refresh: 2; url=usuarios.php");//para ter redicirionamento com delay
            //header("Location: usuarios.php"); //para ter redirecionamento automatico
        }else{
            echo "erro ao deletar usuario!";
        }
    }
}


function updateUser($conecta,$id){
    $id = filter_var($id,FILTER_VALIDATE_INT);
    if(!empty($id) and isset($_POST['atualizar'])){
        $nome = mysqli_real_escape_string($conecta,$_POST['nome']);
        $email = filter_input(INPUT_POST,'email',FILTER_VALIDATE_EMAIL);
        $senha = password_hash($_POST['senha'],PASSWORD_DEFAULT);
        $data = mysqli_real_escape_string($conecta,$_POST['data']);
        $erros = [];
        if(empty($nome) or empty($email)){
            echo "Preencha todos os campos corretamente!";
        }else{
            /*if(empty($_POST['senha'])){
                $sql = "UPDATE usuarios SET nome = '$nome' , email = '$email' , data = '$data' WHERE id = '$id'";
            }else{
                $sql = "UPDATE usuarios SET nome = '$nome' , email = '$email' , data = '$data' , senha = '$senha' WHERE id = '$id'";
            }*/
            $sql = "UPDATE usuarios SET nome = '$nome' , email = '$email' , data = '$data' ";
            $sql .= !empty($_POST['senha']) ? " , senha = '$senha' " : "";
            $sql .= " WHERE id = $id ";
            $action = mysqli_query($conecta,$sql);
            if ($action) {
                echo "usuario atualizado com sucesso";
                header("Refresh: 2; url=usuarios.php");
            }else{
                echo "erro ao atualizar";
            }
        }
    }
}

