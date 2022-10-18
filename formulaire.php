<?php if(isset($_GET['id'],$_GET['id2'])) {
    $prenom= $_GET['id']; 
    $nom= $_GET['id2'];
    $date=date("Y/m/d"); 

    $localhost = "localhost";
    $username = "root";
    $password = "";
    $dbname = "projet_idia_db";

    $connect = new mysqli($localhost, $username, $password, $dbname);

    if($connect->connect_error) {
        die("Connection Failed : " . $connect->connect_error);
    } 
    else { 

        $sql0 = "SELECT * FROM message_open where prenom='".$prenom."' and nom ='".$nom."';";
        $result0 = $connect->query($sql0);
        $output0 = array('data' => array());
        if($result0->num_rows > 0) {}
        else
        {
            $sql1 = "INSERT INTO message_open (prenom,nom,open_date)  VALUES ('$prenom','$nom','$date')";
            if($connect->query($sql1) === TRUE) {}

        }  

    }
    header('location: https://docs.google.com/forms/d/e/1FAIpQLScG2iPSmV4WcZexbB9046IvPPUC0gun9Z347tTqzEVRzL9b1g/viewform?usp=sf_link');

die;
}
?>




















