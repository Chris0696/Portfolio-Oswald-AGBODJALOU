<?php 
if (isset($_POST['ENVOYER'])) 
{

//Déclaration du destinataire, objet 

$recepient = "oswaldjchris@gmail.com";
$sitename = "Mon_Portfolio"; 

//récupération des variables 

$nom = trim($_POST['Fullname']); 

$email = trim($_POST['email']); 
$text = trim($_POST['message']);
$message = "Mr $name a visité votre page $sitename \nEmail: $email \nMessage envoyé: $text";

//Déclaration du mail en format texte 
$pagetitle = "Nouveau message de votre Portfolio: \"$sitename\"";
mail($recepient, $pagetitle, $message, "Content-type: text/plain; charset=\"utf-8\"\n From: $recepient");
$body .= "Client : ".$nom." ".$prenom."\n\n"; 

}
?>


<?php

// submit
if (!isset($_POST['email']) || !isset($_POST['message']))
{
    echo('Il faut un email et un message pour soumettre le formulaire.');
    return;
}	


//$name = $_POST['Fullname'];
//$email = $_POST['email'];
//$message = $_POST['message'];

$name = htmlspecialchars ($_POST['Fullname']); 

$email = htmlspecialchars ($_POST['email']); 
$message = htmlspecialchars($_POST['message']);

?>

<h4>Message bien reçu !</h4>
        
<div class="art-contact-form">
    
    <div>
        <p>
            <br>Bonjour <?php echo($name); ?>, <p>Merci de m'avoir soumit votre message. 
                Je vous répondrai si possible dans un bref délais via votre mail <span><?php echo($email); ?></span>
                ou laissez moi message via <b>WatsApp: </b><a href= "https://wa.me/message/ANS5FI6446HTB1" target="_blank">@valdotechnoloy</a></span> pour une discussion en directe. 
        </p>
        <p>
            <b><h6><u>Votre demande</u></b> :</h6><br><?php echo strip_tags($message); ?>
        </p>
    </div>


<?php
if (
    (!isset($_POST['email']) || !filter_var($_POST['email'], FILTER_VALIDATE_EMAIL))
    || (!isset($_POST['message']) || empty($_POST['message']))
    )
{
    echo('Il faut un email et un message valides pour soumettre le formulaire.');
    return;
}
?>

<?php

use PHPMailer\PHPMailer\Exception;
use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\SMTP;

require_once "includes/phpmailer/Exception.php";
require_once "includes/phpmailer/PHPMailer.php";
require_once "includes/phpmailer/SMTP.php";

$mail = new PHPMailer(true);

try{

    // Collecter les informations dans les variables
    $name = htmlspecialchars ($_POST['Fullname']); 
    $email = htmlspecialchars ($_POST['email']); 
    $message = htmlspecialchars($_POST['message']);

    

    // On configure le SMTP
    $mail->isSMTP();                                            //Send using SMTP
    $mail->Host       = 'localhost';                            //Set the SMTP server to send through
    // $mail->SMTPAuth   = true;                                   //Enable SMTP authentication
    // $mail->Username   = 'user@example.com';                     //SMTP username
    // $mail->Password   = 'secret';                               //SMTP password
    // $mail->SMTPSecure = PHPMailer::ENCRYPTION_SMTPS;            //Enable implicit TLS encryption
    $mail->Port       = 1025;  
    
    // CharSet
    $mail->CharSet = "utf-8";

    
    // Moi je reçois le mail
    //récupération des variables 
    $recepient = "oswaldjchris@gmail.com";
    $sitename = "Mon_Portfolio"; 
 
    $message = "Mr $name a visité votre page $sitename \nEmail: $email \nMessage envoyé: $message";

    //Déclaration du mail en format texte 
    $pagetitle = "Nouveau message de votre Portfolio: \"$sitename\"";
    mail($recepient, $pagetitle, $message, "Content-type: text/plain; charset=\"utf-8\"\n From: $recepient");
    


    // Destinataires
    $mail->addAddress($email, $name);     //Add a recipient
    $mail->addAddress('chrisoswolf@gmail.com');               //Name is optional
    $mail->addCC('oswaldagbodjalou@gmail.com');
    $mail->addBCC('oswaldagbodjalou@gmail.com');

    //Expéditeur
    $mail->setFrom('oswaldjchris@gmail.com', 'Mailer');
    $mail->addReplyTo('chrisoswolf@gmail.com', 'Information');

    

    // Contenu
    $mail->isHTML();
    $mail->Subject = 'Sujet avec caractères accentués';
    $mail->Body    = '
    <p>
    <br>Bonjour <?php echo($name); ?>, <p>Merci de m\'avoir soumit votre message. 
        Je vous répondrai si possible dans un bref délais via votre mail <span><?php echo($email); ?></span>
        ou laissez moi message via <b>WatsApp: </b><a href= "https://wa.me/message/ANS5FI6446HTB1" target="_blank">@valdotechnoloy</a></span> pour une discussion en directe. 
    </p>
    <p>
        <b><h6><u>Votre demande</u></b> :</h6><br><?php echo strip_tags($message); ?>
    </p>';

    $mail->AltBody = "
    <p>
        <br>Bonjour <?php echo($name); ?>, <p>Merci de m\'avoir soumit votre message. 
        Je vous répondrai si possible dans un bref délais via votre mail <span><?php echo($email); ?></span>
        ou laissez moi message via <b>WatsApp: </b><a href= 'https://wa.me/message/ANS5FI6446HTB1' target='_blank'>@valdotechnoloy</a></span> pour une discussion en directe. 
    </p>
    <p>
        <b><h6><u>Votre demande</u></b> :</h6><br><?php echo strip_tags($message); ?>
    </p>";

    // On envoie
    $mail->send();
    echo "";
    
}catch(Exception){
    echo "Message non envoyé. 
    ";
}
?>