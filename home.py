# coding:utf-8
import cgi

print("content-type: text/html; charset=utf-8\n")


html = """

<!doctype html>
<html lang="fr">

<head>
  <!-- Required meta tags -->
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  <!-- color of address bar in mobile browser -->
  <meta name="theme-color" content="#2B2B35">
  <!-- favicon  -->
  <link rel="shortcut icon" href="img/thumbnail.ico" type="image/x-icon">
  <!-- bootstrap css -->
  <link rel="stylesheet" href="css/plugins/bootstrap.min.css">
  <!-- font awesome css -->
  <link rel="stylesheet" href="css/plugins/font-awesome.min.css">
  <!-- swiper css -->
  <link rel="stylesheet" href="css/plugins/swiper.min.css">
  <!-- fancybox css -->
  <link rel="stylesheet" href="css/plugins/fancybox.min.css">
  <!-- main css -->
  <link rel="stylesheet" href="css/style.css">

  <title>Valdo-Tech</title>
</head>

<body>

  <!-- app -->
  <div class="art-app">

    <!-- mobile top bar -->
    <div class="art-mobile-top-bar"></div>

    <!-- app wrapper -->
    <div class="art-app-wrapper">

      <!-- app container end -->
      <div class="art-app-container">

        <!-- info bar -->
        <div class="art-info-bar">

          <!-- menu bar frame -->
          <div class="art-info-bar-frame">

            <!-- info bar header -->
            <div class="art-info-bar-header">
              <!-- info bar button -->
              <a class="art-info-bar-btn" href="#.">
                <!-- icon -->
                <i class="fas fa-ellipsis-v"></i>
              </a>
              <!-- info bar button end -->
            </div>
            <!-- info bar header end -->

            <!-- info bar header -->
            <div class="art-header">
              <!-- avatar -->
              <div class="art-avatar">
                <a data-fancybox="avatar" href="img/Valdo.jpg" class="art-avatar-curtain">
                  <img src="img/Valdo.jpg" alt="avatar">
                  <i class="fas fa-expand"></i>
                </a>
                <!-- available -->
                <div class="art-lamp-light">
                  <!-- add class 'art-not-available' if not available-->
                  <div class="art-available-lamp"></div>
                </div>
              </div>
              <!-- avatar end -->
              <!-- name -->
              <h5 class="art-name mb-10"><a href="/home.html">Oswald AGBODJALOU<a></h5>
              <!-- post -->
              <div class="art-sm-text">Développeur Fullstack <br>Python/Wordpress, </div>
            </div>
            <!-- info bar header end -->

            <!-- scroll frame -->
            <div id="scrollbar2" class="art-scroll-frame">

              <!-- info bar about -->
              <div class="art-table p-15-15">
                <!-- about text -->
                <ul>
                  <!-- country -->
                  <li>
                    <h6>Pays de desidence:</h6><span>Benin</span>
                  </li>
                  <!-- city -->
                  <li>
                    <h6>Ville:</h6><span>Calavi</span>
                  </li>
                  <!-- age -->
                  <li>
                    <h6>Age:</h6><span>26</span>
                  </li>
                </ul>
              </div>
              <!-- info bar about end -->

              <!-- divider -->
              <div class="art-ls-divider"></div>

              <!-- language skills -->
              <div class="art-lang-skills p-30-15">

                <!-- skill -->
                <div class="art-lang-skills-item">
                  <div id="circleprog1" class="art-cirkle-progress"></div>
                  <!-- title -->
                  <h6>Français</h6>
                </div>
                <!-- skill end -->

                <!-- skill -->
                <div class="art-lang-skills-item">
                  <div id="circleprog2" class="art-cirkle-progress"></div>
                  <!-- title -->
                  <h6>English</h6>
                </div>
                <!-- skill end -->

                <!-- skill -->
                <div class="art-lang-skills-item">
                  <div id="circleprog3" class="art-cirkle-progress"></div>
                  <!-- title -->
                  <h6>Fon</h6>
                </div>
                <!-- skill end -->

              </div>
              <!-- language skills end -->

              <!-- divider -->
              <div class="art-ls-divider"></div>

              <!-- hard skills -->
              <div class="art-hard-skills p-30-15">

                <!-- skill -->
                <div class="art-hard-skills-item">
                  <div class="art-skill-heading">
                    <!-- title -->
                    <h6>WordPress</h6>
                  </div>
                  <!-- progressbar frame -->
                  <div class="art-line-progress">
                    <!-- progressbar -->
                    <div id="lineprog4"></div>
                  </div>
                  <!-- progressbar frame end -->
                </div>
                <!-- skill end -->

                <!-- skill -->
                <div class="art-hard-skills-item">
                  <div class="art-skill-heading">
                    <!-- title -->
                    <h6>Python</h6>
                  </div>
                  <!-- progressbar frame -->
                  <div class="art-line-progress">
                    <!-- progressbar -->
                    <div id="lineprog5"></div>
                  </div>
                  <!-- progressbar frame end -->
                </div>
                <!-- skill end --

                <!-- skill -->
                <div class="art-hard-skills-item">
                  <div class="art-skill-heading">
                    <!-- title -->
                    <h6>html</h6>
                  </div>
                  <!-- progressbar frame -->
                  <div class="art-line-progress">
                    <!-- progressbar -->
                    <div id="lineprog1"></div>
                  </div>
                  <!-- progressbar frame end -->
                </div>
                <!-- skill end -->

                <!-- skill -->
                <div class="art-hard-skills-item">
                  <div class="art-skill-heading">
                    <!-- title -->
                    <h6>CSS</h6>
                  </div>
                  <!-- progressbar frame -->
                  <div class="art-line-progress">
                    <!-- progressbar -->
                    <div id="lineprog2"></div>
                  </div>
                  <!-- progressbar frame end -->
                </div>
                <!-- skill end -->

                <!-- skill -->
                <div class="art-hard-skills-item">
                  <div class="art-skill-heading">
                    <!-- title -->
                    <h6>Js</h6>
                  </div>
                  <!-- progressbar frame -->
                  <div class="art-line-progress">
                    <!-- progressbar -->
                    <div id="lineprog3"></div>
                  </div>
                  <!-- progressbar frame end -->
                </div>
                <!-- skill end -->

              </div>
              <!-- language skills end -->

              <!-- divider -->
              <div class="art-ls-divider"></div>

              <!-- knowledge list -->
              <ul class="art-knowledge-list p-15-0">
                <!-- list item -->
                <li>SQL</li>
                <!-- list item -->
                <li>Framework Django</li>
                <!-- list item -->
                <li>Photoshop</li>
                <!-- list item -->
                <li>Woocommerce</li>
                <!-- list item -->
                <li>Elementor</li>
              </ul>
              <!-- knowledge list end -->

              <!-- divider -->
              <div class="art-ls-divider"></div>

              <!-- links frame -->
              <div class="art-links-frame p-15-15">

                <!-- download cv button -->
                <a href="files/CV.jpg" class="art-link" download>Télécharger mon CV <i class="fas fa-download"></i></a>

              </div>
              <!-- links frame end -->

            </div>
            <!-- scroll frame end -->

            <!-- sidebar social -->
            <div class="art-ls-social">
              <!-- social link -->
              <a href="#." target="_blank"><i class="far fa-circle"></i></a>
              <!-- social link -->
              <a href="#." target="_blank"><i class="far fa-circle"></i></a>
              <!-- social link -->
              <a href="#." target="_blank"><i class="far fa-circle"></i></a>
              <!-- social link -->
              <a href="#." target="_blank"><i class="far fa-circle"></i></a>
              <!-- social link -->
              <a href="#." target="_blank"><i class="far fa-circle"></i></a>
            </div>
            <!-- sidebar social end -->

          </div>
          <!-- menu bar frame end -->

        </div>
        <!-- info bar end -->

        <!-- content -->
        <div class="art-content">

          <!-- curtain -->
          <div class="art-curtain"></div>

          <!-- top background -->
          <div class="art-top-bg" style="background-image: url(img/bg.jpg)">
            <!-- overlay -->
            <div class="art-top-bg-overlay"></div>
            <!-- overlay end -->
          </div>
          <!-- top background end -->

          <!-- swup container -->
          <div class="transition-fade" id="swup">

            <!-- scroll frame -->
            <div id="scrollbar" class="art-scroll-frame">

              <!-- container -->
              <div class="container-fluid">

                <!-- row -->
                <div class="row p-60-0 p-lg-30-0 p-md-15-0">
                  <!-- col -->
                  <div class="col-lg-12">

                    <!-- banner -->
                    <div class="art-a art-banner" style="background-image: url(img/bg.jpg)">
                      <!-- banner back -->
                      <div class="art-banner-back"></div>
                      <!-- banner dec -->
                      <div class="art-banner-dec"></div>
                      <!-- banner overlay -->
                      <div class="art-banner-overlay">
                        <!-- main title -->
                        <div class="art-banner-title">
                          <!-- title -->
                          <h1 class="mb-15">Découvrez mon Incroyable <br>Parcours professionnel !</h1>
                          <!-- suptitle -->
                          <div class="art-lg-text art-code mb-25">&lt;<i>code</i>&gt; Je crée <span class="txt-rotate" data-period="2000"
                              data-rotate='[ "des interfaces web.", "tout type de site web.", "des maquettes de conception.", "des outils automatisation." ]'></span>&lt;/<i>code</i>&gt;</div>
                          <div class="art-buttons-frame">
                            <!-- button -->
                            <a href="/history.html" class="art-btn art-btn-md"><span>SAVOIR TOUT SUR MOI</span></a>
                          </div>
                        </div>
                        <!-- main title end -->
                        <!-- photo -->
                        <img src="img/face-2.png" class="art-banner-photo" alt="Your Name">
                      </div>
                      <!-- banner overlay end -->
                    </div>
                    <!-- banner end -->

                  </div>
                  <!-- col end -->
                </div>
                <!-- row end -->

              </div>
              <!-- container end -->

              <!-- container -->
              <div class="container-fluid">

                <!-- row -->
                <div class="row p-30-0">

                  <!-- col -->
                  <div class="col-md-3 col-6">

                    <!-- couner frame -->
                    <div class="art-counter-frame">
                      <!-- counter -->
                      <div class="art-counter-box">
                        <!-- counter number -->
                        <span class="art-counter">02</span><span class="art-counter-plus">+</span>
                      </div>
                      <!-- counter end -->
                      <!-- title -->
                      <h6>Années d'expérience</h6>
                    </div>
                    <!-- couner frame end -->

                  </div>
                  <!-- col end -->

                  <!-- col -->
                  <div class="col-md-3 col-6">

                    <!-- couner frame -->
                    <div class="art-counter-frame">
                      <!-- counter -->
                      <div class="art-counter-box">
                        <!-- counter number -->
                        <span class="art-counter">06</span>
                      </div>
                      <!-- counter end -->
                      <!-- title -->
                      <h6>Projets achevés</h6>
                    </div>
                    <!-- couner frame end -->

                  </div>
                  <!-- col end -->

                  <!-- col -->
                  <div class="col-md-3 col-6">

                    <!-- couner frame -->
                    <div class="art-counter-frame">
                      <!-- counter -->
                      <div class="art-counter-box">
                        <!-- counter number -->
                        <span class="art-counter">30</span>
                      </div>
                      <!-- counter end -->
                      <!-- title -->
                      <h6>Clients satisfaits</h6>
                    </div>
                    <!-- couner frame end -->

                  </div>
                  <!-- col end -->

                  <!-- col -->
                  <div class="col-md-3 col-6">

                    <!-- couner frame -->
                    <div class="art-counter-frame">
                      <!-- counter -->
                      <div class="art-counter-box">
                        <!-- counter number -->
                        <span class="art-counter">20</span><span class="art-counter-plus">+</span>
                      </div>
                      <!-- counter end -->
                      <!-- title -->
                      <h6>Honneurs et récompenses</h6>
                    </div>
                    <!-- couner frame end -->

                  </div>
                  <!-- col end -->

                </div>
                <!-- row end -->

              </div>
              <!-- container end -->

              <!-- container -->
              <div class="container-fluid">

                <!-- row -->
                <div class="row">

                  <!-- col -->
                  <div class="col-lg-12">

                    <!-- section title -->
                    <div class="art-section-title">
                      <!-- title frame -->
                      <div class="art-title-frame">
                        <!-- title -->
                        <h4>Mes services</h4>
                      </div>
                      <!-- title frame end -->
                    </div>
                    <!-- section title end -->

                  </div>
                  <!-- col end -->

                  <!-- col -->
                  <div class="col-lg-4 col-md-6">

                    <!-- service -->
                    <div class="art-a art-service-icon-box">
                      <!-- service content -->
                      <div class="art-service-ib-content">
                        <!-- title -->
                        <h5 class="mb-15">Création de sites Web</h5>
                        <!-- text -->
                        <div class="mb-15">Vous êtes à la recherche d'un site qui pourra étendre votre business. Oui
                          vous avez la possibilité avec moi. Même vendre en ligne et recevoir votre paiement sur votre Mobile money.
                          </div>
                        <!-- button -->
                        <div class="art-buttons-frame"><a href="/contact.html" class="art-link art-color-link art-w-chevron">Passer une commande</a></div>
                      </div>
                      <!-- service content end -->
                    </div>
                    <!-- service end -->

                  </div>
                  <!-- col end -->

                  <!-- col -->
                  <div class="col-lg-4 col-md-6">

                    <!-- service -->
                    <div class="art-a art-service-icon-box">
                      <!-- service content -->
                      <div class="art-service-ib-content">
                        <!-- title -->
                        <h5 class="mb-15">UI/UX Design</h5>
                        <!-- text -->
                        <div class="mb-15"> Je vais vous concevoir une interface et optimiser tous les éléments graphiques qui la compose. 
                          J'optimiserai les enchaînements des actions, les parcours, la navigation et la facilité d'utilisation, de votre interface.</div>
                        <!-- button -->
                        <div class="art-buttons-frame"><a href="/contact.html" class="art-link art-color-link art-w-chevron">Passer une commande</a></div>
                      </div>
                      <!-- service content end -->
                    </div>
                    <!-- service end -->

                  </div>
                  <!-- col end -->

                  <!-- col -->
                  <div class="col-lg-4 col-md-6">

                    <!-- service -->
                    <div class="art-a art-service-icon-box">
                      <!-- service content -->
                      <div class="art-service-ib-content">
                        <!-- title -->
                        <h5 class="mb-15">Graphisme et design</h5>
                        <!-- text -->
                        <div class="mb-15">Je vais vous créer des affiches publicitaires, des enseignes, 
                          toute sorte de visuel numérique et digital. Je peux vous designer toutes les interfaces sur le web.</div>
                        <!-- button -->
                        <div class="art-buttons-frame"><a href="/contact.html" class="art-link art-color-link art-w-chevron">Passer une commande</a></div>
                      </div>
                      <!-- service content end -->
                    </div>
                    <!-- service end -->

                  </div>
                  <!-- col end -->

                </div>
                <!-- row end -->

              </div>
              <!-- container end -->

              <!-- container -->
              <div class="container-fluid">

                <!-- row -->
                <div class="row p-0-0">

                  <!-- col -->
                  <div class="col-lg-12">

                    <!-- section title -->
                    <div class="art-section-title">
                      <!-- title frame -->
                      <div class="art-title-frame">
                        <!-- title -->
                        <h4>Plans tarifaires</h4>
                      </div>
                      <!-- title frame end -->
                    </div>
                    <!-- section title end -->

                  </div>
                  <!-- col end -->

                  <!-- col -->
                  <div class="col-lg-4">

                    <!-- price -->
                    <div class="art-a art-price">
                      <!-- price body -->
                      <div class="art-price-body">
                        <h5 class="mb-30">Prix de départ</h5>
                        <!-- price cost -->
                        <div class="art-price-cost">
                          <div class="art-number">GRATUIT<sup>*</sup></div>
                        </div>
                        <!-- price cost end -->
                        <!-- price list -->
                        <ul class="art-price-list">
                          <!-- list item -->
                          <li>Introduction au trading</li>
                          <!-- list item -->
                          <li>Coaching personnel</li>
                          <!-- list item -->
                          <li class="art-empty-item">Programmation Web</li>
                          <!-- list item -->
                          <li class="art-empty-item">SEO optimization</li>
                          <!-- list item -->
                          <li class="art-empty-item">Formation Wordpress</li>
                        </ul>
                        <!-- price list end -->
                        <!-- button -->
                        <a href="/contact.html" class="art-link art-color-link art-w-chevron">Passez votre commande</a>
                        <div class="art-asterisk"><sup>*</sup>Gratuit uniquement lors de la commande de services payants</div>
                      </div>
                      <!-- price body end -->
                    </div>
                    <!-- price end -->

                  </div>
                  <!-- grid -->

                  <!-- col -->
                  <div class="col-lg-4">

                    <!-- price -->
                    <div class="art-a art-price art-popular-price">
                      <!-- price body -->
                      <div class="art-price-body">
                        <h5 class="mb-30">Paiement horaire</h5>
                        <!-- price cost -->
                        <div class="art-price-cost">
                          <div class="art-number"><span>/heure</span>85.600<span>FCFA</span></div>
                        </div>
                        <!-- price cost end -->
                        <!-- price list -->
                        <ul class="art-price-list">
                          <!-- list item -->
                          <li>Formation trading pour débutants</li>
                          <!-- list item -->
                          <li>Formation Wordpress</li>
                          <!-- list item -->
                          <li>SEO optimization</li>
                          <!-- list item -->
                          <li class="art-empty-item">Programmation Web</li>
                          <!-- list item -->
                          <li class="art-empty-item">Site web professionnel</li>
                        </ul>
                        <!-- price list end -->
                        <!-- button -->
                        <a href="/contact.html" class="art-link art-color-link art-w-chevron">Passez votre commande</a>
                      </div>
                      <!-- price body end -->
                    </div>
                    <!-- price end -->

                  </div>
                  <!-- col end -->

                  <!-- col -->
                  <div class="col-lg-4">

                    <!-- price -->
                    <div class="art-a art-price">
                      <!-- price body -->
                      <div class="art-price-body">
                        <h5 class="mb-30"> À plein temps</h5>
                        <!-- price cost -->
                        <div class="art-price-cost">
                          <div class="art-number"><span></span>195.000<span>FCFA</span></div>
                        </div>
                        <!-- price cost end -->
                        <!-- price list -->
                        <ul class="art-price-list">
                          <!-- list item -->
                          <li>Formation trading avancée</li>
                          <!-- list item -->
                          <li>Programmation Web fullstack</li>
                          <!-- list item -->
                          <li>Site web professionnel</li>
                          <!-- list item -->
                          <li>Web design</li>
                          <!-- list item -->
                          <li>Programmation mobile</li>
                        </ul>
                        <!-- price list end -->
                        <!-- button -->
                        <a href="/contact.html" class="art-link art-color-link art-w-chevron">Passez votre commande</a>
                      </div>
                      <!-- price body end -->
                    </div>
                    <!-- price end -->

                  </div>
                  <!-- col end -->

                  <!-- col -->
                  <div class="col-lg-4">

                    <!-- price -->
                    <div class="art-a art-price">
                      <!-- price body -->
                      <div class="art-price-body">
                        <h5 class="mb-30">Prix de départ</h5>
                        <!-- price cost -->
                        <div class="art-price-cost">
                          <div class="art-number">GRATUIT<sup>*</sup></div>
                        </div>
                        <!-- price cost end -->
                        <!-- price list -->
                        <ul class="art-price-list">
                          <!-- list item -->
                          <li>Achat d'hébergement</li>
                          <!-- list item -->
                          <li>Coaching personnel</li>
                          <!-- list item -->
                          <li class="art-empty-item">Outils d'installation WordPress</li>
                          <!-- list item -->
                          <li class="art-empty-item">Achat de thème Wordpress</li>
                          <!-- list item -->
                          <li class="art-empty-item">Assistance en création de site</li>
                        </ul>
                        <!-- price list end -->
                        <!-- button -->
                        <a href="/contact.html" class="art-link art-color-link art-w-chevron">Passez votre commande</a>
                        <div class="art-asterisk"><sup>*</sup>Gratuit uniquement lors de la commande de services payants</div>
                      </div>
                      <!-- price body end -->
                    </div>
                    <!-- price end -->

                  </div>
                  <!-- grid -->

                  <!-- col -->
                  <div class="col-lg-4">

                    <!-- price -->
                    <div class="art-a art-price art-popular-price">
                      <!-- price body -->
                      <div class="art-price-body">
                        <h5 class="mb-30">Paiement horaire</h5>
                        <!-- price cost -->
                        <div class="art-price-cost">
                          <div class="art-number"><span>/heure</span>40.000<span>FCFA</span></div>
                        </div>
                        <!-- price cost end -->
                        <!-- price list -->
                        <ul class="art-price-list">
                          <!-- list item -->
                          <li>Outils d'installation WordPress</li>
                          <!-- list item -->
                          <li>Achat de thème Wordpress</li>
                          <!-- list item -->
                          <li>Assistance en création de site</li>
                          <!-- list item -->
                          <li class="art-empty-item">Créer un site WordPress</li>
                          <!-- list item -->
                          <li class="art-empty-item">Formation WordPress avancée</li>
                        </ul>
                        <!-- price list end -->
                        <!-- button -->
                        <a href="/contact.html" class="art-link art-color-link art-w-chevron">Passez votre commande</a>
                      </div>
                      <!-- price body end -->
                    </div>
                    <!-- price end -->

                  </div>
                  <!-- col end -->

                  <!-- col -->
                  <div class="col-lg-4">

                    <!-- price -->
                    <div class="art-a art-price">
                      <!-- price body -->
                      <div class="art-price-body">
                        <h5 class="mb-30">Livraison programmée</h5>
                        <!-- price cost -->
                        <div class="art-price-cost">
                          <div class="art-number"><span>/mois</span>150.000<span>FCFA</span></div>
                        </div>
                        <!-- price cost end -->
                        <!-- price list -->
                        <ul class="art-price-list">
                          <!-- list item -->
                          <li>Créer un site web pro WordPress</li>
                          <!-- list item -->
                          <li>Formation WordPress avancée</li>
                          <!-- list item -->
                          <li>Web design & Graphisme</li>
                          <!-- list item -->
                          <li>Gestion de site</li>
                        </ul>
                        <!-- price list end -->
                        <!-- button -->
                        <a href="/contact.html" class="art-link art-color-link art-w-chevron">Passez votre commande</a>
                      </div>
                      <!-- price body end -->
                    </div>
                    <!-- price end -->

                  </div>
                  <!-- col end -->

                </div>
                <!-- row end -->

              </div>
              <!-- container end -->

              <!-- container -->
              <div class="container-fluid">

                <!-- row -->
                <div class="row">

                  <!-- col -->
                  <div class="col-lg-12">

                    <!-- section title -->
                    <div class="art-section-title">
                      <!-- title frame -->
                      <div class="art-title-frame">
                        <!-- title -->
                        <h4>Recommandation</h4>
                      </div>
                      <!-- title frame end -->
                    </div>
                    <!-- section title end -->

                  </div>
                  <!-- col end -->

                  <!-- col -->
                  <div class="col-lg-12">

                    <!-- slider container -->
                    <div class="swiper-container art-testimonial-slider" style="overflow: visible">
                      <!-- slider wrapper -->
                      <div class="swiper-wrapper">
                        <!-- slide -->
                        <div class="swiper-slide">

                          <!-- testimonial -->
                          <div class="art-a art-testimonial">
                            <!-- testimonial body -->
                            <div class="testimonial-body">
                              <!-- photo -->
                              <img class="art-testimonial-face" src="img/testimonials/Valdo.jpeg" alt="face">
                              <!-- name -->
                              <h5>Oswald le duc</h5>
                              <div class="art-el-suptitle mb-15">Responsable de Digital Marcket</div>
                              <!-- text -->
                              <div class="mb-15">Travailler avec VALDO TECHNOLOGY  a été un plaisir. Mieux encore - je les ai alertés d'un problème mineur avant d'aller dormir. Le problème a été résolu le lendemain matin. Je ne pouvais pas demander un meilleur soutien. Merci Oswald !
                                Je laisse 5 étoiles pour les encourager.</div>
                            </div>
                            <!-- testimonial body end -->
                            <!-- testimonial footer -->
                            <div class="art-testimonial-footer">
                              <div class="art-left-side">
                                <!-- star rate -->
                                <ul class="art-star-rate">
                                  <li><i class="fas fa-star"></i></li>
                                  <li><i class="fas fa-star"></i></li>
                                  <li><i class="fas fa-star"></i></li>
                                  <li><i class="fas fa-star"></i></li>
                                  <li><i class="fas fa-star"></i></li>
                                </ul>
                                <!-- star rate end -->
                              </div>
                              <div class="art-right-side">

                              </div>
                            </div>
                            <!-- testimonial footer end -->
                          </div>
                          <!-- testimonial end -->

                        </div>
                        <!-- slide end -->

                        <!-- slide -->
                        <div class="swiper-slide">

                          <!-- testimonial -->
                          <div class="art-a art-testimonial">
                            <!-- testimonial body -->
                            <div class="testimonial-body">
                              <!-- photo -->
                              <img class="art-testimonial-face" src="img/testimonials/Valdo.jpeg" alt="face">
                              <!-- name -->
                              <h5>Evelyne ELEKUSSI</h5>
                              <div class="art-el-suptitle mb-15">Sécrétaire</div>
                              <!-- text -->
                              <div class="mb-15">Merci à Valdo technology pour ses services dans la
                                Conception de notre site web qui dans tout son aspect
                                a réussi à convaincre Ie grand public Grace à ce site.
                                Nous avons réussi à multiplier nos finances en un rien de temps. Nos clients sont satisfaits de son utilisation
                                facile et des nombreux services offerts. Nous vous le conseillons vivement. C'est le meilleur.</div>
                            </div>
                            <!-- testimonial body end -->
                            <!-- testimonial footer -->
                            <div class="art-testimonial-footer">
                              <div class="art-left-side">
                                <!-- star rate -->
                                <ul class="art-star-rate">
                                  <li><i class="fas fa-star"></i></li>
                                  <li><i class="fas fa-star"></i></li>
                                  <li><i class="fas fa-star"></i></li>
                                  <li><i class="fas fa-star"></i></li>
                                  <li class="art-empty-item"><i class="fas fa-star"></i></li>
                                </ul>
                                <!-- star rate end -->
                              </div>
                              <div class="art-right-side">

                              </div>
                            </div>
                            <!-- testimonial footer end -->
                          </div>
                          <!-- testimonial end -->

                        </div>
                        <!-- slide end -->

                        <!-- slide -->
                        <div class="swiper-slide">

                          <!-- testimonial -->
                          <div class="art-a art-testimonial">
                            <!-- testimonial body -->
                            <div class="testimonial-body">
                              <!-- photo -->
                              <img class="art-testimonial-face" src="img/testimonials/Valdo.jpeg" alt="face">
                              <!-- name -->
                              <h5>Paul Trueman</h5>
                              <div class="art-el-suptitle mb-15">Template author</div>
                              <!-- text -->
                              <div class="mb-15">Working with Artur has been a pleasure. Better yet - I alerted them of a minor issue before going to sleep. The issue was fixed the next morning. I couldn't ask for better support. Thank you Artur!
                                This is easily a 5 star freelancer.</div>
                            </div>
                            <!-- testimonial body end -->
                            <!-- testimonial footer -->
                            <div class="art-testimonial-footer">
                              <div class="art-left-side">
                                <!-- star rate -->
                                <ul class="art-star-rate">
                                  <li><i class="fas fa-star"></i></li>
                                  <li><i class="fas fa-star"></i></li>
                                  <li><i class="fas fa-star"></i></li>
                                  <li><i class="fas fa-star"></i></li>
                                  <li><i class="fas fa-star"></i></li>
                                </ul>
                                <!-- star rate end -->
                              </div>
                              <div class="art-right-side">

                              </div>
                            </div>
                            <!-- testimonial footer end -->
                          </div>
                          <!-- testimonial end -->

                        </div>
                        <!-- slide end -->

                        <!-- slide -->
                        <div class="swiper-slide">

                          <!-- testimonial -->
                          <div class="art-a art-testimonial">
                            <!-- testimonial body -->
                            <div class="testimonial-body">
                              <!-- photo -->
                              <img class="art-testimonial-face" src="img/testimonials/Valdo.jpeg" alt="face">
                              <!-- name -->
                              <h5>Paul Trueman</h5>
                              <div class="art-el-suptitle mb-15">Template author</div>
                              <!-- text -->
                              <div class="mb-15">Working with Artur has been a pleasure. Better yet - I alerted them of a minor issue before going to sleep. The issue was fixed the next morning. I couldn't ask for better support. Thank you Artur!
                                This is easily a 5 star freelancer.</div>
                            </div>
                            <!-- testimonial body end -->
                            <!-- testimonial footer -->
                            <div class="art-testimonial-footer">
                              <div class="art-left-side">
                                <!-- star rate -->
                                <ul class="art-star-rate">
                                  <li><i class="fas fa-star"></i></li>
                                  <li><i class="fas fa-star"></i></li>
                                  <li><i class="fas fa-star"></i></li>
                                  <li><i class="fas fa-star"></i></li>
                                  <li><i class="fas fa-star"></i></li>
                                </ul>
                                <!-- star rate end -->
                              </div>
                              <div class="art-right-side">

                              </div>
                            </div>
                            <!-- testimonial footer end -->
                          </div>
                          <!-- testimonial end -->

                        </div>
                        <!-- slide end -->

                      </div>
                      <!-- slider wrapper end -->
                    </div>
                    <!-- slider container end -->

                  </div>
                  <!-- col end -->

                  <!-- col -->
                  <div class="col-lg-12">

                    <!-- slider navigation -->
                    <div class="art-slider-navigation">

                      <!-- left side -->
                      <div class="art-sn-left">

                        <!-- slider pagination -->
                        <div class="swiper-pagination"></div>

                      </div>
                      <!-- left side end -->

                      <!-- right side -->
                      <div class="art-sn-right">

                        <!-- slider navigation -->
                        <div class="art-slider-nav-frame">
                          <!-- prev -->
                          <div class="art-slider-nav art-testi-swiper-prev"><i class="fas fa-chevron-left"></i></div>
                          <!-- next -->
                          <div class="art-slider-nav art-testi-swiper-next"><i class="fas fa-chevron-right"></i></div>
                        </div>
                        <!-- slider navigation -->

                      </div>
                      <!-- right side end -->

                    </div>
                    <!-- slider navigation end -->

                  </div>
                  <!-- col end -->

                </div>
                <!-- row end -->

              </div>
              <!-- container end -->

              <!-- container -->
              <div class="container-fluid">

                <!-- row -->
                <div class="row">

                  <!-- col -->
                  <div class="col-6 col-lg-3">
                    <!-- brand -->
                    <img class="art-brand" src="img/brands/logo valdo.png" alt="brand">
                  </div>
                  <!-- col end -->

                  <!-- col -->
                  <div class="col-6 col-lg-3">
                    <!-- brand -->
                    <img class="art-brand" src="img/brands/emi_monde.png" alt="brand">
                  </div>
                  <!-- col end -->

                  <!-- col -->
                  <div class="col-6 col-lg-3">
                    <!-- brand -->
                    <img class="art-brand" src="img/brands/10xcode.png" alt="brand">
                  </div>
                  <!-- col end -->

                  <!-- col -->
                  <div class="col-6 col-lg-3">
                    <!-- brand -->
                    <img class="art-brand" src="img/brands/1.png" alt="brand">
                  </div>
                  <!-- col end -->

                </div>
                <!-- row end -->

              </div>
              <!-- container end -->

              <!-- container -->
              <div class="container-fluid">

                <!-- footer -->
                <footer>
                  <!-- copyright -->
                  <div>© 2023 VALDO TECHNOLOGY</div>
                  <!-- author ( Please! Do not delete it. You are awesome! :) -->
                  <div>AUTEUR :&#160; <a href="https://valdo-tech.com/our_team/oswald-jchris/" target="_blank">Oswald J~Chris</a></div>
                </footer>
                <!-- footer end -->

              </div>
              <!-- container end -->

            </div>
            <!-- scroll frame end -->

          </div>
          <!-- swup container end -->

        </div>
        <!-- content end -->

        <!-- menu bar -->
        <div class="art-menu-bar">

          <!-- menu bar frame -->
          <div class="art-menu-bar-frame">

            <!-- menu bar header -->
            <div class="art-menu-bar-header">
              <!-- menu bar button -->
              <a class="art-menu-bar-btn" href="#.">
                <!-- icon -->
                <span></span>
              </a>
              <!-- menu bar button end -->
            </div>
            <!-- menu bar header end -->

            <!-- current page title -->
            <div class="art-current-page"></div>
            <!-- current page title end -->

            <!-- scroll frame -->
            <div class="art-scroll-frame">

              <!-- menu -->
              <nav id="swupMenu">
                <!-- menu list -->
                <ul class="main-menu">
                  <!-- menu item -->
                  <li class="menu-item current-menu-item"><a href="/portfolio_de_oswald_agbodj.html">Accueil</a></li>
                  <!-- menu item -->
                  <li class="menu-item menu-item-has-children">
                    <a href="#.">Portfolio</a>
                    <!-- sub menu -->
                    <ul class="sub-menu">
                      <!-- lvl 2 nav link -->
                      <li class="menu-item"><a href="/portfolio-single-2.html">Single project 2</a></li>
                      <!-- lvl 2 nav link -->
                      <li class="menu-item"><a href="/portfolio-2-col-masonry.html">2 column masonry</a></li>
                      
                    </ul>
                    <!-- sub menu end -->
                  </li>
                  <!-- menu item -->
                  <li class="menu-item"><a href="/history.html">Mon Parcours Professionnel</a></li>
                  <!-- menu item -->
                  <li class="menu-item"><a href="/contact.html">Contact</a></li>
                  <!-- menu item -->
                  <li class="menu-item menu-item-has-children">
                    <a href="#.">Blog</a>
                    <!-- sub menu -->
                    <ul class="sub-menu">
                      <!-- lvl 2 nav link -->
                      <li class="menu-item"><a href="/blog_1.html">Nouvelle annonce</a></li>
                      <!-- lvl 2 nav link -->
                      <li class="menu-item"><a href="/all_blog.html">Les annonces</a></li>
                    </ul>
                    <!-- sub menu end -->
                  </li>
                  <!-- menu item -->
                  <li class="menu-item"><a href="onepage.html" target="_blank">Onepage</a></li>
                </ul>
                <!-- menu list end -->
              </nav>
              <!-- menu end -->

              <!-- language change -->
              <ul class="art-language-change">
                <!-- language item -->
                <li><a href="javascript:void()" onclick="window.location.hash='#googtrans(en)';location.reload();">EN</a></li>
                <!-- language item -->
                <li class="art-active-lang"><a href="javascript:void()" onclick="window.location.hash='#googtrans(fr)';location.reload();">Fr</a></li>
              </ul>
              <!-- language change end -->

            </div>
            <!-- scroll frame end -->

          </div>
          <!-- menu bar frame -->

        </div>
        <!-- menu bar end -->

      </div>
      <!-- app container end -->

    </div>
    <!-- app wrapper end -->

    <!-- preloader -->
    <div class="art-preloader">
      <!-- preloader content -->
      <div class="art-preloader-content">
        <!-- title -->
        <h4>VALDO TECHNOLOGY</h4>
        <!-- progressbar -->
        <div id="preloader" class="art-preloader-load"></div>
      </div>
      <!-- preloader content end -->
    </div>
    <!-- preloader end -->

  </div>
  <!-- app end -->

  <!-- jquery js -->
  <script src="js/plugins/jquery.min.js"></script>
  <!-- anime js -->
  <script src="js/plugins/anime.min.js"></script>
  <!-- swiper js -->
  <script src="js/plugins/swiper.min.js"></script>
  <!-- progressbar js -->
  <script src="js/plugins/progressbar.min.js"></script>
  <!-- smooth scrollbar js -->
  <script src="js/plugins/smooth-scrollbar.min.js"></script>
  <!-- overscroll js -->
  <script src="js/plugins/overscroll.min.js"></script>
  <!-- typing js -->
  <script src="js/plugins/typing.min.js"></script>
  <!-- isotope js -->
  <script src="js/plugins/isotope.min.js"></script>
  <!-- fancybox js -->
  <script src="js/plugins/fancybox.min.js"></script>
  <!-- swup js -->
  <script src="js/plugins/swup.min.js"></script>

  <!-- main js -->
  <script src="js/main.js"></script>

  <script type="text/javascript">
  function googleTranslateElementInit() {
    new google.translate.TranslateElement({pageLanguage: 'en'}, 'google_translate_element');
  }
  </script>

  <script type="text/javascript" src="//translate.google.com/translate_a/element.js?cb=googleTranslateElementInit"></script>

</body>

</html>


"""

print(html)