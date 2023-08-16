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
  <link rel="shortcut icon" href="img/Valdo_Technology.ico" type="image/x-icon">
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

  <title>Oswald AGBODJALOU</title>
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
              <h5 class="art-name mb-10"><a href="/index.py">Oswald AGBODJALOU</a></h5>
              <!-- post -->
              <div class="art-sm-text">Développeur Fullstack <br>Python/Wordpress</div>
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
                    <h6>Age:</h6><span>27</span>
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
                  <h6>Langue locale</h6>
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
                <div class="row p-30-0">

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
                              <span class="art-date">Nov 2021</span>
                            </div>
                          </div>
                          <p>Les outils informatiques et le monde du web m'ont motivé à me faire former en premier lieu pour les compétences
                            en développement WordPress. Ainsi j'ai toutes les aptitudes à réaliser des projets de conception de site web,
                          application web et toute plateforme en ligne grâce à Wordpress.</p>
                          <a data-fancybox="diplome" href="files/attestation_wordpress.jpg" class="art-link art-color-link art-w-chevron">Certificat</a>
                        </div>

                      </div>

                      <div class="art-timeline-item">
                        <div class="art-timeline-mark-light"></div>
                        <div class="art-timeline-mark"></div>

                        <div class="art-a art-timeline-content">
                          <div class="art-card-header">
                            <div class="art-left-side">
                              <h5>Développeur Python</h5>
                              <div class="art-el-suptitle mb-15">Desktop - iOS - Android</div>
                            </div>
                            <div class="art-right-side">
                              <span class="art-date">jan 2021 - à nos jours</span>
                            </div>
                          </div>
                          <p>Pour étendre plus mes connaissances et performances, j'ai suivi avec succès toute la formation complète en
                            développement Python du professeur Jonathan Roux sur la plateforme e-learning d'Udemy. 
                            Je peux ainsi concevoir toutes applications web et moblies.
                          </p>
                          <a data-fancybox="diplome" href="files/certificat_python_officiel.png" class="art-link art-color-link art-w-chevron">Certificate</a>
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
                          <p>Ma motivation était de vendre mes connaissances dans plusieurs secteurs d'activités comme le trading
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
                              <h5>Mon Portfolio</h5>
                              <div class="art-el-suptitle mb-15">Réaliser sous Python avec Django</div>
                            </div>
                            <div class="art-right-side">
                              <span class="art-date">08 - 2023</span>
                            </div>
                          </div>
                          <p>Une fois classer parmi les développeurs pourquoi ne pas se faire connaître, faire valoir ses compétences ? Ainsi, j'ai mis en ligne 
                            mon portfolio pour les entreprises ou particuliers comme vous afin que vous aillez une description breve de qui je suis et ce que je sais 
                            faire. A base de celà, je crois avoir répondu à vos attentes et j'espère qu'on pourra collaborer tout suite !</p>
                          <a href="/contact.py" class="art-link art-color-link art-w-chevron">Me contacter</a>
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
                              <h5>Oswald J~Chris</h5>
                              <div class="art-el-suptitle mb-15">Dev Oswald</div>
                              <!-- text -->
                              <div class="mb-15">Je me donne 5 étoiles pour mes propres éfforts. </div>
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
                              <h5>Ma première application mobile</h5>
                              <div class="art-el-suptitle mb-15">Python</div>
                            </div>
                            <div class="art-right-side">
                              <span class="art-date">2023 (en cours)</span>
                            </div>
                          </div>
                          <p>Toujours en phase de développement. Je l'annoncerai d'ici là au grand public.</p>
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
                              <h5>Paul</h5>
                              <div class="art-el-suptitle mb-15">Dev PHP</div>
                              <!-- text -->
                              <div class="mb-15">Travailler avec Oswald c'est faire du jeux avec les codes. Merci Oswald !
                                Tiens ces 5 étoiles.</div>
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
                  <div>© 2023 VALDO TECHNOLOGY</div>
                  <div>AUTEUR :&#160; <a href="index.py" target="_blank">Oswald J~Chris</a></div>
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
                  <li class="menu-item"><a href="/index.py">Accueil</a></li>
                  <!-- menu item -->
                  <li class="menu-item menu-item-has-children">
                    <a href="#.">Portfolio</a>
                    <!-- sub menu -->
                    <ul class="sub-menu">
                      <!-- lvl 2 nav link -->
                      <li class="menu-item"><a href="/project_1.py">Projet 1</a></li>
                      <!-- lvl 2 nav link -->
                      <li class="menu-item"><a href="/all_projects.py">Les projets réalisés</a></li>
                    </ul>
                    <!-- sub menu end -->
                  </li>
                  <!-- menu item -->
                  <li class="menu-item current-menu-item"><a href="/history.py">Mon Parcours Professionnel</a></li>
                  <!-- menu item -->
                  <li class="menu-item"><a href="/contact.py">Contact</a></li>
                  <!-- menu item -->
                  <li class="menu-item menu-item-has-children">
                    <a href="#.">Blog</a>
                    <!-- sub menu -->
                    <ul class="sub-menu">
                      <!-- lvl 2 nav link -->
                      <!-- lvl 2 nav link -->
                      <li class="menu-item"><a href="/blog_1.py">Nouvelle annonce</a></li>
                      <!-- lvl 2 nav link -->
                      <li class="menu-item"><a href="/all_blog.py">Les annonces</a></li>
                    </ul>
                    <!-- sub menu end -->
                  </li>
                  <!-- menu item -->
                  <li class="menu-item"><a href="" target="_blank"></a></li>
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