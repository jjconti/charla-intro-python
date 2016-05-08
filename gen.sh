export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8
rst2html5 --jquery --reveal-js --reveal-js-opts theme=black,transition=convex \
          --pretty-print-code \
          --stylesheet-path=slides.css intro-python.rst \
          --title "Introducción a Python" > intro-python-reveal.html
