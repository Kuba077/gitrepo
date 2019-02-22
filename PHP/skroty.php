<?php
    $data1 = 'Adam Nowak';
    $data2 = 'Adam Nowak';
    echo hash('md5', $data1);
    echo '
';
    echo hash('sha256', $data2);
    echo '
';
    echo hash('haval256,5', $data2);
    
    
?>
