<?php
    session_start();

    //limpar os caches da sessao
    session_unset();

    //encerra a session(desloga)
    session_destroy();

    header("location:index.php");