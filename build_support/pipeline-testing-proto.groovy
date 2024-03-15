pipeline {
  agent {
    kubernetes {
      yaml """
 apiVersion: v1
 kind: Pod
 spec:
   serviceAccountName: jenkins-role
   restartPolicy: Never
   containers:
     - name: python
       image: python:3.11-bookworm
       resources:
         requests:
           cpu: "1"
           memory: '1200Mi'
         limits:
           cpu: "2"
           memory: '2400Mi'
         args:
           - -cpus
           - "2"
       command: ['bash']
       tty: true
"""
    }
  }

  options {
    skipDefaultCheckout true
  }

  stages {

    stage('Checkout') {
      steps {
        deleteDir()
        checkout scm
      }
    }

    stage('Run Tests') {
      steps {
        container('python') {
          sh '''

          # Install additional OS libraries
          apt-get update -y && \
            apt-get install -y \
              libglib2.0-0 \
              libnss3 \
              libgconf-2-4 \
              libfontconfig1

          # Install Chrome
          # TODO This is less than ideal. Look into building custom images.
          echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections
          apt-get -qq -o=Dpkg::Use-Pty=0 update && apt-get -qq -o=Dpkg::Use-Pty=0 -y install gettext-base gnupg2 wget > /dev/null
          echo 'deb http://dl.google.com/linux/chrome/deb/ stable main' > /etc/apt/sources.list.d/chrome.list
          wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
          set -x && apt-get -qq -o=Dpkg::Use-Pty=0 update && apt-get -qq -o=Dpkg::Use-Pty=0 -y install xvfb google-chrome-stable > /dev/null
          ln -sf /usr/bin/xvfb-chrome /usr/bin/google-chrome

#            apt-get install -y \
#              libglib2.0-0=2.50.3-2 \
#              libnss3=2:3.26.2-1.1+deb9u1 \
#              libgconf-2-4=3.2.6-4+b1 \
#              libfontconfig1=2.11.0-6.7+b1

          # Check Python version
          python --version

          # Install required Python libraries
          python -m ensurepip --upgrade
          pip install pytest-cov pipreqs pip-tools

          pipreqs --savepath=requirements.in && pip-compile
          # run unit tests using pytest
          #mkdir -p reports/junit
          #mkdir -p reports/coverage

          pip install -r requirements.txt
          export PYTHONPATH=".:./src:./tests:./testCases"
          #. tests/test-env.sh
          pytest -o log_cli=true --log-cli-level=WARNING \
#            --junitxml=reports/junit/junit.xml \
#            --cov-report xml:reports/coverage/coverage.xml \
#            --cov-report html:reports/coverage/html_report \
#            --cov=src \
            testCases/

          '''
        }
      }
    }
  }
}
