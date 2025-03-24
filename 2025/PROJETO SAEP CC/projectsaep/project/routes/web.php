<?php

use Illuminate\Support\Facades\Route;
use Illuminate\Http\Request;
use App\Http\Controllers\TestController;
use App\Http\Controllers\ClientController;

Route::get('/', function () {
    return view('welcome');
});

Route::get('/soma/{a}/{b}', function ($a, $b) {
    $soma = $a + $b;

    if ($soma >= 18) {
        return "A soma de $a e $b é " . ($a + $b) . " e é maior que 18";
    }else{
       
            return "A soma de $a e $b é " . ($a + $b) . " e é menor que 18";
      
    }
    


});

Route::get('/media/{a}/{b}', function ($a, $b) {

        /*
        for($i = 1; $i <= $b; $i++){

            $codigo = rand(5, 15);
            echo "o aluo " . $i . " tem o numero sortuado de " . $codigo . "</br>";

        }*/

        
        if($a == $b){
            echo "Os valores são iguais </br>";
            echo "Este Aluno está aprovado em: " . date('d/m/Y'). "</br>";
            
        }else if($a < $b) {
            echo "A Média deste aluno é " . $a. " que é menor do que a media da instituição que é  " . $b. ". </br>";
            echo "<br>Este Aluno está de Recuperação em: " . date('d/m/Y'). "</br>";
            echo "<br>Este aluno pode fazer " . ($b - $a) . " prova(s) de recuperação </br>";            
            for($i = $b; $i > $a; $i--) {                
                $index = $b - $i +1; 
                echo $index . " - Esta prova será realizada em até " . $index * 30 . " dias  tendo como data final para realização da prova o dia "  . date('d/m/Y', strtotime('+' . $index * 30 . ' days')) .    " </br>";
            }
        }
        else {  
            echo "A Média deste aluno é " . $a. " que  é maior  do que a media da instituição que é   " . $b. ". </br>";
            echo "Aluno está aprovado em: " . date('d/m/Y') ;
        }          
        
     
             


        function adicionarDiasUteis($dataInicial, $diasUteis) {
            
            $data = strtotime($dataInicial); // Converte a data para timestamp
            $adicionados = 0;
        
            while ($adicionados < $diasUteis) {
                $data = strtotime('+1 day', $data); // Avança um dia
                // Verifica se não é sábado (6) nem domingo (0)
                if (date('N', $data) < 6) {
                    $adicionados++;
                }
            }
        
            return date('d/m/Y', $data);
        }
        
        echo "<br><br>Data atual: " . date('d/m/Y') . "<br>";
        echo "Data após 30 dias úteis: " . adicionarDiasUteis(date('Y-m-d'), 30);       

});

Route::get('/divisao/{a}/{b}', function ($a, $b) {
    return "A Divisão de $a e $b é " . ($a / $b);
});

Route::get('/multiplicacao/{a}/{b}', function ($a, $b) {
    return "A Multiplicação de $a e $b é " . ($a * $b);
});

Route::resources([
    'test' => TestController::class,
    'client' => ClientController::class,
    
]);
    
