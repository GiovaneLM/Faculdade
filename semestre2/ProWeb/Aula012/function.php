<?php

$server = "localhost";
$userDb = "root";
$passDb = "";
$nameDb = "lojinha";
$conecta = mysqli_connect($server,$userDb,$passDb,$nameDb);


#################CRIAÇÃO DE TABELAS E USUARIO#################
function criarTabelaUsuarios($conecta){
    $sql = "CREATE TABLE IF NOT EXISTS usuarios (
        id_user INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(100) NOT NULL,
        email VARCHAR(150) NOT NULL UNIQUE,
        senha VARCHAR(255) NOT NULL,
        data DATETIME DEFAULT CURRENT_TIMESTAMP
    )";

    return mysqli_query($conecta, $sql);
}

function criarTabelaCategorias($conecta){
    $sql = "CREATE TABLE IF NOT EXISTS categorias (
        id_cat INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(100) NOT NULL,
        data DATETIME DEFAULT CURRENT_TIMESTAMP
    )";

    return mysqli_query($conecta, $sql);
}

function criarTabelaProdutos($conecta){
    $sql = "CREATE TABLE IF NOT EXISTS produtos (
        id_pro INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(150) NOT NULL,
        descricao TEXT,
        preco DECIMAL(10,2) NOT NULL,
        categoria INT NOT NULL,
        data DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (categoria) REFERENCES categorias(id_cat)
    ) ENGINE=InnoDB";

    return mysqli_query($conecta, $sql);
}

function criarAdminPadrao($conecta){
    $resultado = mysqli_query($conecta, "SELECT COUNT(*) AS total FROM usuarios");
    $linha = mysqli_fetch_assoc($resultado);
    if ($linha['total'] == 0) {
        $nome  = "admin";
        $email = "admin@email.com";
        $senha = password_hash("admin12345", PASSWORD_DEFAULT);
        $stmt = mysqli_prepare($conecta, "INSERT INTO usuarios (nome, senha, email) VALUES (?, ?, ?)");
        mysqli_stmt_bind_param($stmt, "sss", $nome, $senha, $email);
        mysqli_stmt_execute($stmt);
        mysqli_stmt_close($stmt);
    }
}



#################BUSCAR#################
function buscarProdutos($conecta){
$sql = "SELECT p.id_pro, p.nome, p.descricao, p.preco, p.data,c.nome AS categoria_nome
    FROM produtos p
    INNER JOIN categorias c ON p.categoria = c.id_cat
    ORDER BY p.nome";
    $action = mysqli_query($conecta,$sql);
    $dados = mysqli_fetch_all($action, MYSQLI_ASSOC);
    return $dados;
}


function buscarCategorias($conecta){
    $sql = "SELECT id_cat, nome, data FROM categorias ORDER BY nome";
    $action = mysqli_query($conecta, $sql);
    return mysqli_fetch_all($action, MYSQLI_ASSOC);
}

function buscarUsuarios($conecta){
    $sql = "SELECT id_user, nome, email, data FROM usuarios ORDER BY nome";
    $action = mysqli_query($conecta, $sql);
    return mysqli_fetch_all($action, MYSQLI_ASSOC);
}


function buscarCategoria($conecta, $id){
    $id = filter_var($id,FILTER_VALIDATE_INT);
    if(!empty($id)){
        $sql = "SELECT * FROM categorias WHERE id_cat = $id";
        $action = mysqli_query($conecta,$sql);
        $dados = mysqli_fetch_assoc($action);
        return $dados;
    }
}

function buscarProduto($conecta,$id){
$sql = "SELECT p.id_pro, p.nome, p.descricao, p.preco, p.data,c.nome AS categoria_nome
    FROM produtos p
    INNER JOIN categorias c ON p.categoria = c.id_cat
    WHERE id_pro = $id";
    $action = mysqli_query($conecta,$sql);
    $dados = mysqli_fetch_assoc($action);
    return $dados;
}

function buscarUsuario($conecta, $id){
    $id = filter_var($id,FILTER_VALIDATE_INT);
    if(!empty($id)){
        $sql = "SELECT * FROM usuarios WHERE id_user = $id";
        $action = mysqli_query($conecta,$sql);
        // o marcelo que me disse que fetch all era bidimensional e que precisava ser assoc, senão era precisa puxar [0]['atributo'] ou usando foreach pra 1 produto
        $dados = mysqli_fetch_assoc($action);
        return $dados;
    }
}
#################CADASTRAR AS COISAS#################
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



#################LOGIN#################
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

#################DELETAR#################
function deleteCategoria($conecta, $id){
    if (is_numeric($id) and !empty($id)) {
        $sql = "DELETE FROM categorias WHERE id_cat = $id";
        $action = mysqli_query($conecta,$sql);
        if ($action) {
            echo "Categoria deletada com sucesso!";
            //echo "<script> window.location.ref = 'isiarios.php' </script>";
            header("Refresh: 2; url=cad_categoria.php");//para ter redicirionamento com delay
            //header("Location: usuarios.php"); //para ter redirecionamento automatico
        }else{
            echo "erro ao deletar Categoria!";
        }
    }
}

function deleteProduto($conecta, $id){
    if (is_numeric($id) and !empty($id)) {
        $sql = "DELETE FROM produtos WHERE id_pro = $id";
        $action = mysqli_query($conecta,$sql);
        if ($action) {
            echo "Produto deletado com sucesso!";
            //echo "<script> window.location.ref = 'isiarios.php' </script>";
            header("Refresh: 2; url=cad_produto.php");//para ter redicirionamento com delay
            //header("Location: usuarios.php"); //para ter redirecionamento automatico
        }else{
            echo "erro ao deletar Produto!";
        }
    }
}


function deleteUsuario($conecta, $id){
    if (is_numeric($id) and !empty($id)) {
        $sql = "DELETE FROM usuarios WHERE id_user = $id";
        $action = mysqli_query($conecta,$sql);
        if ($action) {
            echo "Usuario deletado com sucesso!";
            //echo "<script> window.location.ref = 'isiarios.php' </script>";
            header("Refresh: 2; url=cad_usuario.php");//para ter redicirionamento com delay
            //header("Location: usuarios.php"); //para ter redirecionamento automatico
        }else{
            echo "erro ao deletar Usuario!";
        }
    }
}


#################EDITAR#################
function EditarCategoria($conecta,$id){
    $id = filter_var($id,FILTER_VALIDATE_INT);
    if(!empty($id) and isset($_POST['atualizar'])){
        $nome = mysqli_real_escape_string($conecta,$_POST['nome']);
        $erros = [];
        if(empty($nome)){
            echo "Preencha todos os campos corretamente!";
        }else{
            /*if(empty($_POST['senha'])){
                $sql = "UPDATE usuarios SET nome = '$nome' , email = '$email' , data = '$data' WHERE id = '$id'";
            }else{
                $sql = "UPDATE usuarios SET nome = '$nome' , email = '$email' , data = '$data' , senha = '$senha' WHERE id = '$id'";
            }*/
            $sql = "UPDATE categorias SET nome = '$nome'  ";
            $sql .= " WHERE id_cat = $id ";
            $action = mysqli_query($conecta,$sql);
            if ($action) {
                echo "categoria atualizada com sucesso";
                header("Refresh: 2; url=cad_categoria.php");
            }else{
                echo "erro ao atualizar";
            }
        }
    }
}

function EditarProduto($conecta, $id){
    $id = filter_var($id, FILTER_VALIDATE_INT);
    if(!empty($id) and isset($_POST['atualizar'])){
        $nome = mysqli_real_escape_string($conecta, $_POST['nome']);
        $descricao = mysqli_real_escape_string($conecta, $_POST['descricao']);
        $preco = filter_input(INPUT_POST, "preco", FILTER_VALIDATE_FLOAT);
        $categoria = filter_input(INPUT_POST, "categoria", FILTER_VALIDATE_INT);
        $erros = [];
        if(empty($nome) or empty($descricao) or $preco === false or $preco === null or $categoria === false or $categoria === null){
            echo "Preencha todos os campos corretamente!";
        }else{
            $sql = "UPDATE produtos SET nome = '$nome' , preco = $preco ";
            $sql .= !empty($_POST['descricao']) ? " , descricao = '$descricao' " : "";
            $sql .= !empty($_POST['categoria']) ? " , categoria = '$categoria' " : "";
            $sql .= !empty($_POST['data']) ? " , data = '$data' " : "";
            $sql .= " WHERE id_pro = $id";
            $action = mysqli_query($conecta, $sql);
            if($action){
                echo "Produto atualizado com sucesso";
                header("Refresh: 2; url=cad_produto.php");
            }else{
                echo "Erro ao atualizar produto";
            }
        }
    }
}

function EditarUsuario($conecta,$id){
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
            $sql = "UPDATE usuarios SET nome = '$nome' , email = '$email'  ";
            $sql .= !empty($_POST['data']) ? " , data = '$data' " : "";
            $sql .= !empty($_POST['senha']) ? " , senha = '$senha' " : "";
            $sql .= " WHERE id_user = $id ";
            $action = mysqli_query($conecta,$sql);
            if ($action) {
                echo "usuario atualizado com sucesso";
                header("Refresh: 2; url=cad_usuario.php");
            }else{
                echo "erro ao atualizar";
            }
        }
    }
}

