<?php

namespace frontend\controllers;

use yii\web\Controller;

class TestController extends \yii\web\Controller
{
    public function actionIndex()
    {
        $data = 'datatest';
        return $this->render('index',[
            'data' => $data
        ]);
    }
    public function actionTest(){
        echo 'Chompoo';
        return $this->render('test');
    }
}



?>