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

  <title>Arter</title>
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
                <a data-fancybox="avatar" href="img/face-1.jpg" class="art-avatar-curtain">
                  <img src="img/face-1.jpg" alt="avatar">
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
              <h5 class="art-name mb-10"><a href="/home.html">Artur Carter</a></h5>
              <!-- post -->
              <div class="art-sm-text">Front-end Deweloper <br>Ui/UX Designer, </div>
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
                    <h6>Residence:</h6><span>Canada</span>
                  </li>
                  <!-- city -->
                  <li>
                    <h6>City:</h6><span>Toronto</span>
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
                  <h6>French</h6>
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
                  <h6>Spanish</h6>
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
                <li>Bootstrap, Materialize</li>
                <!-- list item -->
                <li>Stylus, Sass, Less</li>
                <!-- list item -->
                <li>Gulp, Webpack, Grunt</li>
                <!-- list item -->
                <li>GIT knowledge</li>
              </ul>
              <!-- knowledge list end -->

              <!-- divider -->
              <div class="art-ls-divider"></div>

              <!-- links frame -->
              <div class="art-links-frame p-15-15">

                <!-- download cv button -->
                <a href="files/cv.txt" class="art-link" download>Download cv <i class="fas fa-download"></i></a>

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

                    <!-- filter -->
                    <div class="art-filter mb-30">
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
                  <!-- col end -->

                  <div class="art-grid art-grid-3-col art-gallery">

                    <!-- grid item -->
                    <div class="art-grid-item webTemplates">
                      <!-- grid item frame -->
                      <a data-fancybox="gallery" href="img/works/original-size/1.jpg" class="art-a art-portfolio-item-frame art-square">
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
                        <div class="mb-15">Sit amet, consectetur adipisicing elit. Quas, architecto.</div>
                        <!-- button -->
                        <a href="/portfolio-single.html" class="art-link art-color-link art-w-chevron">Read more</a>
                      </div>
                      <!-- description end -->

                    </div>
                    <!-- grid item end -->

                    <!-- grid item -->
                    <div class="art-grid-item logos">
                      <!-- grid item frame -->
                      <a data-fancybox="gallery" href="img/works/original-size/2.jpg" class="art-a art-portfolio-item-frame art-square">
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
                        <a href="/portfolio-single.html" class="art-link art-color-link art-w-chevron">Read more</a>
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
                        <a href="/portfolio-single.html" class="art-link art-color-link art-w-chevron">Read more</a>
                      </div>
                      <!-- description end -->

                    </div>
                    <!-- grid item end -->

                    <!-- grid item -->
                    <div class="art-grid-item ui">
                      <!-- grid item frame -->
                      <a data-fancybox="gallery" href="img/works/original-size/4.jpg" class="art-a art-portfolio-item-frame art-square">
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
                        <a href="/portfolio-single.html" class="art-link art-color-link art-w-chevron">Read more</a>
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
                        <a href="/portfolio-single.html" class="art-link art-color-link art-w-chevron">Read more</a>
                      </div>
                      <!-- description end -->

                    </div>
                    <!-- grid item end -->

                    <!-- grid item -->
                    <div class="art-grid-item logos">
                      <!-- grid item frame -->
                      <a data-fancybox="gallery" href="img/works/original-size/6.jpg" class="art-a art-portfolio-item-frame art-square">
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
                        <a href="/portfolio-single.html" class="art-link art-color-link art-w-chevron">Read more</a>
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
                        <a href="/portfolio-single.html" class="art-link art-color-link art-w-chevron">Read more</a>
                      </div>
                      <!-- description end -->

                    </div>
                    <!-- grid item end -->

                    <!-- grid item -->
                    <div class="art-grid-item ui">
                      <!-- grid item frame -->
                      <a data-fancybox="gallery" href="img/works/original-size/8.jpg" class="art-a art-portfolio-item-frame art-square">
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
                        <div class="mb-15">Sit amet, consectetur adipisicing elit. Quas, architecto.</div>
                        <!-- button -->
                        <a href="/portfolio-single.html" class="art-link art-color-link art-w-chevron">Read more</a>
                      </div>
                      <!-- description end -->

                    </div>
                    <!-- grid item end -->

                    <!-- grid item -->
                    <div class="art-grid-item webTemplates">
                      <!-- grid item frame -->
                      <a data-fancybox="gallery" href="img/works/original-size/9.jpg" class="art-a art-portfolio-item-frame art-square">
                        <!-- img -->
                        <img src="img/works/thumbnail/9.jpg" alt="item">
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
                        <a href="/portfolio-single.html" class="art-link art-color-link art-w-chevron">Read more</a>
                      </div>
                      <!-- description end -->

                    </div>
                    <!-- grid item end -->

                    <!-- grid item -->
                    <div class="art-grid-item logos">
                      <!-- grid item frame -->
                      <a data-fancybox="gallery" href="img/works/original-size/10.jpg" class="art-a art-portfolio-item-frame art-square">
                        <!-- img -->
                        <img src="img/works/thumbnail/10.jpg" alt="item">
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
                        <a href="/portfolio-single.html" class="art-link art-color-link art-w-chevron">Read more</a>
                      </div>
                      <!-- description end -->

                    </div>
                    <!-- grid item end -->

                    <!-- grid item -->
                    <div class="art-grid-item drawings">
                      <!-- grid item frame -->
                      <a data-fancybox="gallery" href="img/works/original-size/11.jpg" class="art-a art-portfolio-item-frame art-square">
                        <!-- img -->
                        <img src="img/works/thumbnail/11.jpg" alt="item">
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
                        <a href="/portfolio-single.html" class="art-link art-color-link art-w-chevron">Read more</a>
                      </div>
                      <!-- description end -->

                    </div>
                    <!-- grid item end -->

                    <!-- grid item -->
                    <div class="art-grid-item drawings">
                      <!-- grid item frame -->
                      <a data-fancybox="gallery" href="img/works/original-size/13.jpg" class="art-a art-portfolio-item-frame art-square">
                        <!-- img -->
                        <img src="img/works/thumbnail/13.jpg" alt="item">
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
                        <a href="/portfolio-single.html" class="art-link art-color-link art-w-chevron">Read more</a>
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
                  <li class="menu-item"><a href="/home.html">Home</a></li>
                  <!-- menu item -->
                  <li class="menu-item menu-item-has-children current-menu-item">
                    <a href="#.">Portfolio</a>
                    <!-- sub menu -->
                    <ul class="sub-menu">
                      <!-- lvl 2 nav link -->
                      <li class="menu-item"><a href="/portfolio-2-col.html">2 column</a></li>
                      <!-- lvl 2 nav link -->
                      <li class="menu-item"><a href="/portfolio-3-col.html">3 column</a></li>
                      <!-- lvl 2 nav link -->
                      <li class="menu-item"><a href="/portfolio-2-col-masonry.html">2 column masonry</a></li>
                      <!-- lvl 2 nav link -->
                      <li class="menu-item"><a href="/portfolio-3-col-masonry.html">3 column masonry</a></li>
                      <!-- lvl 2 nav link -->
                      <li class="menu-item"><a href="/portfolio-single.html">Single project</a></li>
                      <!-- lvl 2 nav link -->
                      <li class="menu-item"><a href="/portfolio-single-2.html">Single project 2</a></li>
                    </ul>
                    <!-- sub menu end -->
                  </li>
                  <!-- menu item -->
                  <li class="menu-item"><a href="/history.html">History</a></li>
                  <!-- menu item -->
                  <li class="menu-item"><a href="/contact.html">Contact</a></li>
                  <!-- menu item -->
                  <li class="menu-item menu-item-has-children">
                    <a href="#.">Blog</a>
                    <!-- sub menu -->
                    <ul class="sub-menu">
                      <!-- lvl 2 nav link -->
                      <li class="menu-item"><a href="/blog-2-col.html">2 column</a></li>
                      <!-- lvl 2 nav link -->
                      <li class="menu-item"><a href="/blog-3-col.html">3 column</a></li>
                      <!-- lvl 2 nav link -->
                      <li class="menu-item"><a href="/blog-post.html">Publication</a></li>
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
        <h4>Artur Carter</h4>
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