# coding:utf-8
import cgi

print("content-type: text/html; charset=utf-8\n")


html = """

<!doctype html>
<html lang="zxx">

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

  
  <title>Valdo</title>
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
              <div class="art-sm-text">Développeur Fullstack <br>Développeur Wordpress, </div>
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

                <!-- skill -->
                <div class="art-hard-skills-item">
                  <div class="art-skill-heading">
                    <!-- title -->
                    <h6>PHP</h6>
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
                    <h6>Wordpress</h6>
                  </div>
                  <!-- progressbar frame -->
                  <div class="art-line-progress">
                    <!-- progressbar -->
                    <div id="lineprog5"></div>
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
                <li>Bootstrap</li>
                <!-- list item -->
                <li>Laravel</li>
                <!-- list item -->
                <li>Pyton</li>
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
                            <a href="/portfolio-3-col-masonry.html" class="art-btn art-btn-md"><span>Explorer maintenant</span></a>
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
                <div class="row p-30-0">

                  <!-- col -->
                  <div class="col-lg-12">

                    <!-- section title -->
                    <div class="art-section-title">
                      <!-- title frame -->
                      <div class="art-title-frame">
                        <!-- title -->
                        <h4>Works</h4>
                      </div>
                      <!-- title frame end -->
                      <!-- right frame -->
                      <div class="art-right-frame">
                        <!-- filter -->
                        <div class="art-filter">
                          <!-- filter link -->
                          <a href="#" data-filter="*" class="art-link art-current">All Categories</a>
                          <!-- filter link -->
                          <a href="#" data-filter=".webTemplates" class="art-link">Web Templates</a>
                          <!-- filter link -->
                          <a href="#" data-filter=".logos" class="art-link">Logos</a>
                          <!-- filter link -->
                          <a href="#" data-filter=".drawings" class="art-link">Drawings</a>
                          <!-- filter link -->
                          <a href="#" data-filter=".ui" class="art-link">UI Elements</a>
                        </div>
                        <!-- filter end -->
                      </div>
                      <!-- right frame end -->
                    </div>
                    <!-- section title end -->

                  </div>
                  <!-- col end -->

                  <div class="art-grid art-grid-3-col art-gallery">

                    <!-- grid item -->
                    <div class="art-grid-item webTemplates">
                      <!-- grid item frame -->
                      <a data-fancybox="gallery" href="img/works/original-size/1.jpg" class="art-a art-portfolio-item-frame art-horizontal">
                        <!-- img -->
                        <img src="img/works/thumbnail/1.jpg" alt="item">
                        <!-- zoom icon -->
                        <span class="art-item-hover"><i class="fas fa-expand"></i></span>
                      </a>
                      <!-- grid item frame end -->
                      <!-- description -->
                      <div class="art-item-description">
                        <!-- title -->
                        <h5 class="mb-15">Project title</h5>
                        <!-- button -->
                        <a href="#." class="art-link art-color-link art-w-chevron">Read more</a>
                      </div>
                      <!-- description end -->

                    </div>
                    <!-- grid item end -->

                    <!-- grid item -->
                    <div class="art-grid-item logos">
                      <!-- grid item frame -->
                      <a data-fancybox="gallery" href="img/works/original-size/2.jpg" class="art-a art-portfolio-item-frame art-vertical">
                        <!-- img -->
                        <img src="img/works/thumbnail/2.jpg" alt="item">
                        <!-- zoom icon -->
                        <span class="art-item-hover"><i class="fas fa-expand"></i></span>
                      </a>
                      <!-- grid item frame end -->
                      <!-- description -->
                      <div class="art-item-description">
                        <!-- title -->
                        <h5 class="mb-15">Project title</h5>
                        <div class="mb-15">Sit amet, consectetur adipisicing elit. Quas, architecto.</div>
                        <!-- button -->
                        <a href="#." class="art-link art-color-link art-w-chevron">Read more</a>
                      </div>
                      <!-- description end -->

                    </div>
                    <!-- grid item end -->

                    <!-- grid item -->
                    <div class="art-grid-item drawings">
                      <!-- grid item frame -->
                      <a data-fancybox="gallery" href="img/works/original-size/3.jpg" class="art-a art-portfolio-item-frame art-square">
                        <!-- img -->
                        <img src="img/works/thumbnail/3.jpg" alt="item">
                        <!-- zoom icon -->
                        <span class="art-item-hover"><i class="fas fa-expand"></i></span>
                      </a>
                      <!-- grid item frame end -->
                      <!-- description -->
                      <div class="art-item-description">
                        <!-- title -->
                        <h5 class="mb-15">Project title</h5>
                        <div class="mb-15">Sit amet, consectetur adipisicing elit. Quas, architecto.</div>
                        <!-- button -->
                        <a href="#." class="art-link art-color-link art-w-chevron">Read more</a>
                      </div>
                      <!-- description end -->

                    </div>
                    <!-- grid item end -->

                    <!-- grid item -->
                    <div class="art-grid-item ui">
                      <!-- grid item frame -->
                      <a data-fancybox="gallery" href="img/works/original-size/4.jpg" class="art-a art-portfolio-item-frame art-vertical">
                        <!-- img -->
                        <img src="img/works/thumbnail/4.jpg" alt="item">
                        <!-- zoom icon -->
                        <span class="art-item-hover"><i class="fas fa-expand"></i></span>
                      </a>
                      <!-- grid item frame end -->
                      <!-- description -->
                      <div class="art-item-description">
                        <!-- title -->
                        <h5 class="mb-15">Project title</h5>
                        <div class="mb-15">Sit amet, consectetur adipisicing elit. Quas, architecto.</div>
                        <!-- button -->
                        <a href="#." class="art-link art-color-link art-w-chevron">Read more</a>
                      </div>
                      <!-- description end -->

                    </div>
                    <!-- grid item end -->

                    <!-- grid item -->
                    <div class="art-grid-item webTemplates">
                      <!-- grid item frame -->
                      <a data-fancybox="gallery" href="img/works/original-size/5.jpg" class="art-a art-portfolio-item-frame art-square">
                        <!-- img -->
                        <img src="img/works/thumbnail/5.jpg" alt="item">
                        <!-- zoom icon -->
                        <span class="art-item-hover"><i class="fas fa-expand"></i></span>
                      </a>
                      <!-- grid item frame end -->
                      <!-- description -->
                      <div class="art-item-description">
                        <!-- title -->
                        <h5 class="mb-15">Project title</h5>
                        <div class="mb-15">Sit amet, consectetur adipisicing elit. Quas, architecto.</div>
                        <!-- button -->
                        <a href="#." class="art-link art-color-link art-w-chevron">Read more</a>
                      </div>
                      <!-- description end -->

                    </div>
                    <!-- grid item end -->

                    <!-- grid item -->
                    <div class="art-grid-item logos">
                      <!-- grid item frame -->
                      <a data-fancybox="gallery" href="img/works/original-size/6.jpg" class="art-a art-portfolio-item-frame art-vertical">
                        <!-- img -->
                        <img src="img/works/thumbnail/6.jpg" alt="item">
                        <!-- zoom icon -->
                        <span class="art-item-hover"><i class="fas fa-expand"></i></span>
                      </a>
                      <!-- grid item frame end -->
                      <!-- description -->
                      <div class="art-item-description">
                        <!-- title -->
                        <h5 class="mb-15">Project title</h5>
                        <div class="mb-15">Sit amet, consectetur adipisicing elit. Quas, architecto.</div>
                        <!-- button -->
                        <a href="#." class="art-link art-color-link art-w-chevron">Read more</a>
                      </div>
                      <!-- description end -->

                    </div>
                    <!-- grid item end -->

                    <!-- grid item -->
                    <div class="art-grid-item drawings">
                      <!-- grid item frame -->
                      <a data-fancybox="gallery" href="img/works/original-size/7.jpg" class="art-a art-portfolio-item-frame art-square">
                        <!-- img -->
                        <img src="img/works/thumbnail/7.jpg" alt="item">
                        <!-- zoom icon -->
                        <span class="art-item-hover"><i class="fas fa-expand"></i></span>
                      </a>
                      <!-- grid item frame end -->
                      <!-- description -->
                      <div class="art-item-description">
                        <!-- title -->
                        <h5 class="mb-15">Project title</h5>
                        <div class="mb-15">Sit amet, consectetur adipisicing elit. Quas, architecto.</div>
                        <!-- button -->
                        <a href="#." class="art-link art-color-link art-w-chevron">Read more</a>
                      </div>
                      <!-- description end -->

                    </div>
                    <!-- grid item end -->

                    <!-- grid item -->
                    <div class="art-grid-item ui">
                      <!-- grid item frame -->
                      <a data-fancybox="gallery" href="img/works/original-size/8.jpg" class="art-a art-portfolio-item-frame art-horizontal">
                        <!-- img -->
                        <img src="img/works/thumbnail/8.jpg" alt="item">
                        <!-- zoom icon -->
                        <span class="art-item-hover"><i class="fas fa-expand"></i></span>
                      </a>
                      <!-- grid item frame end -->
                      <!-- description -->
                      <div class="art-item-description">
                        <!-- title -->
                        <h5 class="mb-15">Project title</h5>
                        <!-- button -->
                        <a href="#." class="art-link art-color-link art-w-chevron">Read more</a>
                      </div>
                      <!-- description end -->

                    </div>
                    <!-- grid item end -->

                  </div>

                </div>
                <!-- row end -->

              </div>
              <!-- container end -->

              <!-- container -->
              <div class="container-fluid">

                <!-- row -->
                <div class="row">

                  <!-- col -->
                  <div class="col-lg-6">

                    <!-- section title -->
                    <div class="art-section-title">
                      <!-- title frame -->
                      <div class="art-title-frame">
                        <!-- title -->
                        <h4>Etudes et diplômes</h4>
                      </div>
                      <!-- title frame end -->
                    </div>
                    <!-- section title end -->

                    <!-- timeline -->
                    <div class="art-timeline art-gallery" id="history">
                      <div class="art-timeline-item">
                        <div class="art-timeline-mark-light"></div>
                        <div class="art-timeline-mark"></div>

                        <div class="art-a art-timeline-content">
                          <div class="art-card-header">
                            <div class="art-left-side">
                              <h5>BACCALAUREAT </h5>
                              <div class="art-el-suptitle mb-15">Série C</div>
                            </div>
                            <div class="art-right-side">
                              <span class="art-date">oct 2016 - juin 2017</span>
                            </div>
                          </div>

                          <p>Ma passion pour les mathématiques m'a poussé à décrocher un baccalaureat série scientifique (C) avec mension. Ainsi 
                            j'ai poursuivi sur cette voix pour intégrer une université de ma ville de résidence.
                          </p>
                          <a data-fancybox="diplome" href="files/certificate.jpg" class="art-link art-color-link art-w-chevron">Diplome</a>
                        </div>
                      </div>

                      <div class="art-timeline-item">
                        <div class="art-timeline-mark-light"></div>
                        <div class="art-timeline-mark"></div>

                        <div class="art-a art-timeline-content">
                          <div class="art-card-header">
                            <div class="art-left-side">
                              <h5>Cursus universitaire</h5>
                              <div class="art-el-suptitle mb-15">Deux années universitaire</div>
                            </div>
                            <div class="art-right-side">
                              <span class="art-date">jan 2018 - mai 2020</span>
                            </div>
                          </div>
                          <div>
                            <p>J'ai ensuite intégré l'Ecole Nationnale de l'Econnomie Appliquée et du Management où j'ai étudié la Statistique
                              Economique et Sectorielle. J'ai fait une reconversion par la suite vers l'Informatique. 
                          </p>
                        </div>
                        </div>
                      </div>

                      <div class="art-timeline-item">
                        <div class="art-timeline-mark-light"></div>
                        <div class="art-timeline-mark"></div>

                        <div class="art-a art-timeline-content">
                          <div class="art-card-header">
                            <div class="art-left-side">
                              <h5>Développeur WordPress</h5>
                              <div class="art-el-suptitle mb-15">Technicien, maintenancier WordPress</div>
                            </div>
                            <div class="art-right-side">
                              <span class="art-date">jan 2020 - oct 2021</span>
                            </div>
                          </div>
                          <p>Les outils informatiques et le monde du web m'ont motivé à me faire former en premier lieu pour les compétences
                            en développement WordPress. Ainsi j'ai toutes les aptitudes à réaliser des projets de conception de site web,
                          application web et toute plateforme en ligne grâce à Wordpress.</p>
                          <a data-fancybox="diplome" href="files/certificate.jpg" class="art-link art-color-link art-w-chevron">Certificat</a>
                        </div>

                      </div>

                      <div class="art-timeline-item">
                        <div class="art-timeline-mark-light"></div>
                        <div class="art-timeline-mark"></div>

                        <div class="art-a art-timeline-content">
                          <div class="art-card-header">
                            <div class="art-left-side">
                              <h5>Développeur web</h5>
                              <div class="art-el-suptitle mb-15">back-end(Laravel)</div>
                            </div>
                            <div class="art-right-side">
                              <span class="art-date">jan 2021 - à nos jours</span>
                            </div>
                          </div>
                          <p>Pour étendre plus mes connaissance et performances, je me suis inscrit aux cours sur la programmation web sur
                            le site français OpenClassroom où j'ai acquéris du savoir en HTML, CSS, JavaScript, PHP, Bootstrap. Je peux 
                            à nos jours concevoir des applications web par ma spécialité en back-end avec Laravel.
                          </p>
                          <a data-fancybox="diplome" href="files/certificate.jpg" class="art-link art-color-link art-w-chevron">Certificate</a>
                        </div>

                      </div>

                    </div>
                    <!-- timeline end -->

                  </div>
                  <div class="col-lg-6">

                    <!-- section title -->
                    <div class="art-section-title">
                      <!-- title frame -->
                      <div class="art-title-frame">
                        <!-- title -->
                        <h4>Historiques de réalisations</h4>
                      </div>
                      <!-- title frame end -->
                    </div>
                    <!-- section title end -->

                    <!-- timeline -->
                    <div class="art-timeline">

                      <div class="art-timeline-item">
                        <div class="art-timeline-mark-light"></div>
                        <div class="art-timeline-mark"></div>


                        <div class="art-a art-timeline-content">
                          <div class="art-card-header">
                            <div class="art-left-side">
                              <h5>Mon tout premier site web</h5>
                              <div class="art-el-suptitle mb-15">WordPress</div>
                            </div>
                            <div class="art-right-side">
                              <span class="art-date">oct 2021 - jan 2021</span>
                            </div>
                          </div>
                          <p>Ma motivation était de vendre mes connaissance dans plusieurs secteurs d'activités comme le trading
                            d'actifs financiers et de cryptos, mes propres formations en développement Wordpress et programmation..</p>
                        </div>
                      </div>

                      <div class="art-timeline-item">
                        <div class="art-timeline-mark-light"></div>
                        <div class="art-timeline-mark"></div>


                        <div class="art-a art-timeline-content">
                          <div class="art-card-header">
                            <div class="art-left-side">
                              <h5>Site web EMI-MONDE</h5>
                              <div class="art-el-suptitle mb-15">WordPress</div>
                            </div>
                            <div class="art-right-side">
                              <span class="art-date">jan 2021 - mars 2021</span>
                            </div>
                          </div>
                          <p>
                            Le tout premier site (site e-learning) que j'ai conçu pour la boîte où j'étais au post de développeur WordPress. Ce site 
                            servait pour les formations en ligne  dont j'étais le formateur principal.
                          </p>
                          <a data-fancybox="recommendation" href="#art-recomendation-popup-1" class="art-link art-color-link art-w-chevron">Recommendation</a>
                        </div>

                        <!-- popup -->
                        <div class="art-recomendation-popup" style="display: none;" id="art-recomendation-popup-1">

                          <!-- testimonial -->
                          <div class="art-a art-testimonial">
                            <!-- testimonial body -->
                            <div class="testimonial-body">
                              <!-- photo -->
                              <img class="art-testimonial-face" src="img/testimonials/face-3.jpg" alt="face">
                              <!-- name -->
                              <h5>EMI-MONDE</h5>
                              <div class="art-el-suptitle mb-15">Notre avis</div>
                              <!-- text -->
                              <div class="mb-15">C'est avec grande satisfaction nous témoignons des compétences de notre collaborateur Mr Oswald
                                pour les traveaux menés à bien dans nos locaux. Et avec fièrté nous le recommandons pour des projets dans le monde
                                du numérique. Merci Oswald AGBODJALOU. 
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
                        <!-- popup end -->

                      </div>

                      <div class="art-timeline-item">
                        <div class="art-timeline-mark-light"></div>
                        <div class="art-timeline-mark"></div>

                        <div class="art-a art-timeline-content">
                          <div class="art-card-header">
                            <div class="art-left-side">
                              <h5>Title of section 1</h5>
                              <div class="art-el-suptitle mb-15">Template author</div>
                            </div>
                            <div class="art-right-side">
                              <span class="art-date">jan 2018 - may 2020</span>
                            </div>
                          </div>
                          <p>Consectetur adipisicing elit. Excepturi, obcaecati, quisquam id molestias eaque asperiores voluptatibus cupiditate error assumenda delectus odit similique earum voluptatem doloremque dolorem
                            ipsam quae rerum quis. Odit, itaque, deserunt corporis vero ipsum nisi eius odio natus ullam provident pariatur temporibus quia eos repellat consequuntur perferendis enim amet quae quasi repudiandae sed quod veniam
                            dolore
                            possimus rem voluptatum eveniet eligendi quis fugiat aliquam sunt similique aut adipisci.</p>
                          <a data-fancybox="recommendation" href="#art-recomendation-popup-2" class="art-link art-color-link art-w-chevron">Recommendation</a>
                        </div>

                        <!-- popup -->
                        <div class="art-recomendation-popup" style="display: none;" id="art-recomendation-popup-2">

                          <!-- testimonial -->
                          <div class="art-a art-testimonial">
                            <!-- testimonial body -->
                            <div class="testimonial-body">
                              <!-- photo -->
                              <img class="art-testimonial-face" src="img/testimonials/face-4.jpg" alt="face">
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
                        <!-- popup end -->

                      </div>

                      <div class="art-timeline-item">
                        <div class="art-timeline-mark-light"></div>
                        <div class="art-timeline-mark"></div>

                        <div class="art-a art-timeline-content">
                          <div class="art-card-header">
                            <div class="art-left-side">
                              <h5>Title of section 1</h5>
                              <div class="art-el-suptitle mb-15">Template author</div>
                            </div>
                            <div class="art-right-side">
                              <span class="art-date">jan 2018 - tonight</span>
                            </div>
                          </div>
                          <p>Dolor sit amet, consectetur adipisicing elit. Iusto, optio, dolorum provident rerum.</p>
                          <a data-fancybox="recommendation" href="#art-recomendation-popup-3" class="art-link art-color-link art-w-chevron">Recommendation</a>
                        </div>

                        <!-- popup -->
                        <div class="art-recomendation-popup" style="display: none;" id="art-recomendation-popup-3">

                          <!-- testimonial -->
                          <div class="art-a art-testimonial">
                            <!-- testimonial body -->
                            <div class="testimonial-body">
                              <!-- photo -->
                              <img class="art-testimonial-face" src="img/testimonials/face-2.jpg" alt="face">
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
                        <!-- popup end -->

                      </div>

                    </div>
                    <!-- timeline end -->

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
                        <h4>Newsletter</h4>
                      </div>
                      <!-- title frame end -->
                    </div>
                    <!-- section title end -->

                  </div>
                  <!-- col end -->

                  <!-- col -->
                  <div class="col-lg-12">

                    <!-- slider container -->
                    <div class="swiper-container art-blog-slider" style="overflow: visible">
                      <!-- slider wrapper -->
                      <div class="swiper-wrapper">
                        <!-- slide -->
                        <div class="swiper-slide">

                          <!-- blog post card -->
                          <div class="art-a art-blog-card">
                            <!-- post cover -->
                            <a href="#." class="art-port-cover">
                              <!-- img -->
                              <img src="img/blog/1.jpg" alt="blog post">
                            </a>
                            <!-- post cover end -->
                            <!-- post description -->
                            <div class="art-post-description">
                              <!-- title -->
                              <a href="#.">
                                <h5 class="mb-15">Blog post title</h5>
                              </a>
                              <!-- text -->
                              <div class="mb-15">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Amet!</div>
                              <!-- link -->
                              <a href="#." class="art-link art-color-link art-w-chevron">Read more</a>
                            </div>
                            <!-- post description end -->
                          </div>
                          <!-- blog post card end -->

                        </div>
                        <!-- slide end -->
                        <!-- slide -->
                        <div class="swiper-slide">

                          <!-- blog post card -->
                          <div class="art-a art-blog-card">
                            <!-- post cover -->
                            <a href="#." class="art-port-cover">
                              <!-- img -->
                              <img src="img/blog/2.jpg" alt="blog post">
                            </a>
                            <!-- post cover end -->
                            <!-- post description -->
                            <div class="art-post-description">
                              <!-- title -->
                              <a href="#.">
                                <h5 class="mb-15">Blog post title</h5>
                              </a>
                              <!-- text -->
                              <div class="mb-15">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Amet!</div>
                              <!-- link -->
                              <a href="#." class="art-link art-color-link art-w-chevron">Read more</a>
                            </div>
                            <!-- post description end -->
                          </div>
                          <!-- blog post card end -->

                        </div>
                        <!-- slide end -->
                        <!-- slide -->
                        <div class="swiper-slide">

                          <!-- blog post card -->
                          <div class="art-a art-blog-card">
                            <!-- post cover -->
                            <a href="#." class="art-port-cover">
                              <!-- img -->
                              <img src="img/blog/3.jpg" alt="blog post">
                            </a>
                            <!-- post cover end -->
                            <!-- post description -->
                            <div class="art-post-description">
                              <!-- title -->
                              <a href="#.">
                                <h5 class="mb-15">Blog post title</h5>
                              </a>
                              <!-- text -->
                              <div class="mb-15">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Amet!</div>
                              <!-- link -->
                              <a href="#." class="art-link art-color-link art-w-chevron">Read more</a>
                            </div>
                            <!-- post description end -->
                          </div>
                          <!-- blog post card end -->

                        </div>
                        <!-- slide end -->
                        <!-- slide -->
                        <div class="swiper-slide">

                          <!-- blog post card -->
                          <div class="art-a art-blog-card">
                            <!-- post cover -->
                            <a href="#." class="art-port-cover">
                              <!-- img -->
                              <img src="img/blog/4.jpg" alt="blog post">
                            </a>
                            <!-- post cover end -->
                            <!-- post description -->
                            <div class="art-post-description">
                              <!-- title -->
                              <a href="#.">
                                <h5 class="mb-15">Blog post title</h5>
                              </a>
                              <!-- text -->
                              <div class="mb-15">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Amet!</div>
                              <!-- link -->
                              <a href="#." class="art-link art-color-link art-w-chevron">Read more</a>
                            </div>
                            <!-- post description end -->
                          </div>
                          <!-- blog post card end -->

                        </div>
                        <!-- slide end -->
                        <!-- slide -->
                        <div class="swiper-slide">

                          <!-- blog post card -->
                          <div class="art-a art-blog-card">
                            <!-- post cover -->
                            <a href="#." class="art-port-cover">
                              <!-- img -->
                              <img src="img/blog/5.jpg" alt="blog post">
                            </a>
                            <!-- post cover end -->
                            <!-- post description -->
                            <div class="art-post-description">
                              <!-- title -->
                              <a href="#.">
                                <h5 class="mb-15">Blog post title</h5>
                              </a>
                              <!-- text -->
                              <div class="mb-15">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Amet!</div>
                              <!-- link -->
                              <a href="#." class="art-link art-color-link art-w-chevron">Read more</a>
                            </div>
                            <!-- post description end -->
                          </div>
                          <!-- blog post card end -->

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
                          <div class="art-slider-nav art-blog-swiper-prev"><i class="fas fa-chevron-left"></i></div>
                          <!-- next -->
                          <div class="art-slider-nav art-blog-swiper-next"><i class="fas fa-chevron-right"></i></div>
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
                <div class="row p-30-0">

                  <!-- col -->
                  <div class="col-lg-12">

                    <!-- section title -->
                    <div class="art-section-title">
                      <!-- title frame -->
                      <div class="art-title-frame">
                        <!-- title -->
                        <h4>Contact information</h4>
                      </div>
                      <!-- title frame end -->
                    </div>
                    <!-- section title end -->

                  </div>
                  <!-- col end -->
                  <!-- col -->
                  <div class="col-lg-4">
                    <!-- contact card -->
                    <div class="art-a art-card">
                      <div class="art-table p-15-15">
                        <ul>
                          <li>
                            <h6>Country:</h6><span>Canada</span>
                          </li>
                          <li>
                            <h6>City:</h6><span>Toronto</span>
                          </li>

                          <li>
                            <h6>Streat:</h6><span>20 Dellbank Rd</span>
                          </li>
                        </ul>
                      </div>
                    </div>
                    <!-- contact card end -->
                  </div>
                  <!-- col end -->
                  <!-- col -->
                  <div class="col-lg-4">
                    <!-- contact card -->
                    <div class="art-a art-card">
                      <div class="art-table p-15-15">
                        <ul>
                          <li>
                            <h6>Email:</h6><span>carter.inbox@mail.com</span>
                          </li>
                          <li>
                            <h6>Telegram:</h6><span>@arter</span>
                          </li>
                          <li>
                            <h6>Skype:</h6><span>Arter</span>
                          </li>
                        </ul>
                      </div>
                    </div>
                    <!-- contact card end -->
                  </div>
                  <!-- col end -->
                  <!-- col -->
                  <div class="col-lg-4">
                    <!-- contact card -->
                    <div class="art-a art-card">
                      <div class="art-table p-15-15">
                        <ul>
                          <li>
                            <h6>Support service:</h6><span>+78 (098) 333 11 22</span>
                          </li>
                          <li>
                            <h6>Office:</h6><span>+78 (098) 326 11 22</span>
                          </li>
                          <li>
                            <h6>Personal:</h6><span>+78 (077) 114 26 53</span>
                          </li>
                        </ul>
                      </div>
                    </div>
                    <!-- contact card end -->

                  </div>
                  <!-- col end -->

                  <!-- col -->
                  <div class="col-lg-12">

                    <!-- section title -->
                    <div class="art-section-title">
                      <!-- title frame -->
                      <div class="art-title-frame">
                        <!-- title -->
                        <h4>Get in touch</h4>
                      </div>
                      <!-- title frame end -->
                    </div>
                    <!-- section title end -->

                    <!-- contact form frame -->
                    <div class="art-a art-card">

                      <!-- contact form -->
                      <form id="form" class="art-contact-form">
                        <!-- form field -->
                        <div class="art-form-field">
                          <!-- name input -->
                          <input id="name" name="name" class="art-input" type="text" placeholder="Name" required>
                          <!-- label -->
                          <label for="name"><i class="fas fa-user"></i></label>
                        </div>
                        <!-- form field end -->
                        <!-- form field -->
                        <div class="art-form-field">
                          <!-- email input -->
                          <input id="email" name="email" class="art-input" type="email" placeholder="Email" required>
                          <!-- label -->
                          <label for="email"><i class="fas fa-at"></i></label>
                        </div>
                        <!-- form field end -->
                        <!-- form field -->
                        <div class="art-form-field">
                          <!-- message textarea -->
                          <textarea id="message" name="text" class="art-input" placeholder="Message" required></textarea>
                          <!-- label -->
                          <label for="message"><i class="far fa-envelope"></i></label>
                        </div>
                        <!-- form field end -->
                        <!-- button -->
                        <div class="art-submit-frame">
                          <button class="art-btn art-btn-md art-submit" type="submit"><span>Send message</span></button>
                          <!-- success -->
                          <div class="art-success">Success <i class="fas fa-check"></i></div>
                        </div>
                      </form>
                      <!-- contact form end -->

                    </div>
                    <!-- contact form frame end -->

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
                    <img class="art-brand" src="img/brands/1.png" alt="brand">
                  </div>
                  <!-- col end -->

                  <!-- col -->
                  <div class="col-6 col-lg-3">
                    <!-- brand -->
                    <img class="art-brand" src="img/brands/2.png" alt="brand">
                  </div>
                  <!-- col end -->

                  <!-- col -->
                  <div class="col-6 col-lg-3">
                    <!-- brand -->
                    <img class="art-brand" src="img/brands/3.png" alt="brand">
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
                  <div>© 2020 Artur Carter</div>
                  <!-- author ( Please! Do not delete it. You are awesome! :) -->
                  <div>Template author:&#160; <a href="https://themeforest.net/user/millerdigitaldesign" target="_blank">Nazar Miller</a></div>
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

      </div>
      <!-- app container end -->

    </div>
    <!-- app wrapper end -->

    <!-- preloader -->
    <div class="art-preloader">
      <!-- preloader content -->
      <div class="art-preloader-content">
        <!-- title -->
        <h4>Artur Carter</h4>
        <!-- progressbar -->
        <div id="preloader" class="art-preloader-load"></div>
      </div>
      <!-- preloader content end -->
    </div>
    <!-- preloader end -->

  </div>
  <!-- app end -->
  <div id="swupMenu"></div>

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