<?php


if (!function_exists('somar')) {
    function somar($a, $b) {
        return $a + $b;
    }
}

if (!function_exists('media')) {
    function media($a, $b) {

        return ($a + $b)/2;
    }
}

if (!function_exists('divisao')) {
    function divisao($a, $b) {

        return $a / $b;
    }
}

function gerarDetalhes($nome, $idade) {
    return [
    'nome' => $nome,
    'idade' => $idade,
    'maioridade' => $idade >= 18 ? 'Sim' : 'Não'
    ];
}

?>