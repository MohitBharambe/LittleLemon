pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        bat 'echo "compiling"'
      }
    }

    stage('Test') {
      steps {
        echo 'Testing the app'
      }
    }

    stage('Deploy') {
      steps {
        bat 'echo "Deployment Complete"'
      }
    }

  }
}