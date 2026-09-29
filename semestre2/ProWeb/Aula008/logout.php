<?php 
    session_start();

    //limpar os caches da session
    session_unset();

    //encerrar a session
    session_destroy();

    echo "sessao encerrada com sucesso!";

    header("Refresh:3; url=index.php");
?>