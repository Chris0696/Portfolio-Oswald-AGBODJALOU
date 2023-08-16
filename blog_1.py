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
                  <div class="col-lg-12">

                    <!-- section title -->
                    <div class="art-section-title">
                      <!-- title frame -->
                      <div class="art-title-frame">
                        <!-- title -->
                        <h4>Publication title</h4>
                      </div>
                      <!-- title frame end -->
                      <!-- right frame -->
                      <div class="art-right-frame">
                        <div class="art-project-category">Ui Design, Graphic</div>
                      </div>
                      <!-- right frame end -->
                    </div>
                    <!-- section title end -->

                  </div>
                  <!-- col end -->

                  <!-- col -->
                  <div class="col-lg-12">

                    <!-- project cover -->
                    <div class="art-a art-project-cover">
                      <!-- item frame -->
                      <a data-fancybox="gallery" href="img/blog/2.jpg" class="art-portfolio-item-frame art-horizontal">
                        <!-- img -->
                        <img src="img/blog/2.jpg" alt="item">
                        <!-- zoom icon -->
                        <span class="art-item-hover"><i class="fas fa-expand"></i></span>
                      </a>
                      <!-- item end -->
                    </div>
                    <!-- project cover nd -->

                  </div>
                  <!-- col end -->

                  <!-- col -->
                  <div class="col-lg-8">

                    <!-- post text -->
                    <div class="art-a art-card">
                      <p class="art-lg-text art-white"><i>Consectetur adipisicing elit. Magni debitis nemo, minus aut tempora impedit quis quam omnis, odit saepe ipsa sunt magnam culpa quisquam iusto consectetur necessitatibus. Tenetur, eligendi!</i>
                      </p>

                      <p>Vero praesentium voluptatibus repellendus, delectus harum. Necessitatibus temporibus, veritatis sapiente laudantium eius rem dolore voluptas porro assumenda quam ea
                        earum ad dolor dolores ut ipsam optio! Numquam dolore quidem sequi eum placeat voluptatum, assumenda et culpa iure nemo vero animi mollitia facere fuga sit debitis
                        doloremque quo tempore nesciunt voluptates cum. Est, labore pariatur cupiditate non alias officia ad nihil animi itaque soluta quo perferendis vero libero ex. Iste ipsam eaque veniam facilis architecto unde, quibusdam
                        accusamus culpa cumque delectus deserunt nemo saepe minima.</p>
                      <ul class="art-custom-list">
                        <li>Doloribus recusandae</li>
                        <li>Alias officia ad nihil </li>
                        <li>Culpa repellat</li>
                        <li>Officiis deleniti</li>
                      </ul>
                      <p>Doloribus recusandae vel odio laboriosam, officia, neque ad. Eius porro, quas adipisci mollitia similique possimus ex odio eum harum eos ut optio architecto eveniet corporis nostrum beatae impedit, iste officia tempora
                        sapiente aut, distinctio numquam inventore et! Ducimus quasi ullam saepe aliquid aut minus molestiae nam. Dolor consequuntur cum consectetur ducimus obcaecati perspiciatis harum quae atque, architecto aut voluptatibus quaerat
                        nisi, nobis asperiores.</p>

                      <blockquote>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Nemo officiis aliquam, placeat quis voluptatum ad. Eum, alias quo fuga sed?</blockquote>

                      <p>Est nesciunt dolorum asperiores sint mollitia quod, nostrum eos maxime illo eveniet ducimus labore amet voluptatum laborum, ex ut similique omnis ipsum. Totam tempore praesentium assumenda ducimus porro ullam quasi, expedita
                        sit esse alias quisquam! Asperiores at suscipit officiis deleniti soluta fugit quidem illo fuga, adipisci maiores. Nesciunt dolor, minus ex tenetur necessitatibus et id minima, vitae sit a, assumenda, iste suscipit facere.
                        Voluptatibus animi, laboriosam qui officiis voluptatum. Voluptates quibusdam numquam distinctio fuga.</p>

                      <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. </p>
                    </div>
                    <!-- post text end -->

                  </div>
                  <!-- col end -->

                  <!-- col -->
                  <div class="col-lg-4">

                    <div class="art-a art-card">
                      <!-- table -->
                      <div class="art-table p-15-15">
                        <ul>
                          <li>
                            <h6>Date:</h6><span>24.12.2019</span>
                          </li>
                          <li>
                            <h6>Author:</h6><span>Artur Carter</span>
                          </li>
                          <li>
                            <h6>Category:</h6><span>Product design</span>
                          </li>
                        </ul>
                      </div>
                      <!-- table end -->
                    </div>

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

                    <!-- pagination -->
                    <div class="art-a art-pagination">
                      <!-- button -->
                      <a href="#" class="art-link art-color-link art-w-chevron art-left-link"><span>annonce précédente</span></a>
                      <div class="art-pagination-center art-m-hidden">
                        <a class="art-link" href="/all_blog.py">Toutes les annonces</a>
                      </div>
                      <!-- button -->
                      <a href="#" class="art-link art-color-link art-w-chevron"><span>annonce suivante</span></a>
                    </div>
                    <!-- pagination end -->

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
                        <h4>Similar posts</h4>
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
                            <a href="/blog-post.py" class="art-port-cover">
                              <!-- img -->
                              <img src="img/blog/1.jpg" alt="blog post">
                            </a>
                            <!-- post cover end -->
                            <!-- post description -->
                            <div class="art-post-description">
                              <!-- title -->
                              <a href="/blog-post.py">
                                <h5 class="mb-15">Blog post title</h5>
                              </a>
                              <!-- text -->
                              <div class="mb-15">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Amet!</div>
                              <!-- link -->
                              <a href="/blog-post.py" class="art-link art-color-link art-w-chevron">Read more</a>
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
                            <a href="/blog-post.py" class="art-port-cover">
                              <!-- img -->
                              <img src="img/blog/2.jpg" alt="blog post">
                            </a>
                            <!-- post cover end -->
                            <!-- post description -->
                            <div class="art-post-description">
                              <!-- title -->
                              <a href="/blog-post.py">
                                <h5 class="mb-15">Blog post title</h5>
                              </a>
                              <!-- text -->
                              <div class="mb-15">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Amet!</div>
                              <!-- link -->
                              <a href="/blog-post.py" class="art-link art-color-link art-w-chevron">Read more</a>
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
                            <a href="/blog-post.py" class="art-port-cover">
                              <!-- img -->
                              <img src="img/blog/3.jpg" alt="blog post">
                            </a>
                            <!-- post cover end -->
                            <!-- post description -->
                            <div class="art-post-description">
                              <!-- title -->
                              <a href="/blog-post.py">
                                <h5 class="mb-15">Blog post title</h5>
                              </a>
                              <!-- text -->
                              <div class="mb-15">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Amet!</div>
                              <!-- link -->
                              <a href="/blog-post.py" class="art-link art-color-link art-w-chevron">Read more</a>
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
                            <a href="/blog-post.py" class="art-port-cover">
                              <!-- img -->
                              <img src="img/blog/4.jpg" alt="blog post">
                            </a>
                            <!-- post cover end -->
                            <!-- post description -->
                            <div class="art-post-description">
                              <!-- title -->
                              <a href="/blog-post.py">
                                <h5 class="mb-15">Blog post title</h5>
                              </a>
                              <!-- text -->
                              <div class="mb-15">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Amet!</div>
                              <!-- link -->
                              <a href="/blog-post.py" class="art-link art-color-link art-w-chevron">Read more</a>
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
                            <a href="/blog-post.py" class="art-port-cover">
                              <!-- img -->
                              <img src="img/blog/5.jpg" alt="blog post">
                            </a>
                            <!-- post cover end -->
                            <!-- post description -->
                            <div class="art-post-description">
                              <!-- title -->
                              <a href="/blog-post.py">
                                <h5 class="mb-15">Blog post title</h5>
                              </a>
                              <!-- text -->
                              <div class="mb-15">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Amet!</div>
                              <!-- link -->
                              <a href="/blog-post.py" class="art-link art-color-link art-w-chevron">Read more</a>
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
                  <li class="menu-item"><a href="/index.py">Acceuil</a></li>
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
                  <li class="menu-item"><a href="/history.py">Mon Parcours professionnel</a></li>
                  <!-- menu item -->
                  <li class="menu-item"><a href="/contact.py">Contact</a></li>
                  <!-- menu item -->
                  <li class="menu-item menu-item-has-children current-menu-item">
                    <a href="#.">Blog</a>
                    <!-- sub menu -->
                    <ul class="sub-menu">
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