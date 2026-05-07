pipeline {
    agent any 

    environment {
        APP_NAME = "LittleLemon"
    }

    stages {
        stage('Checkout') {
            steps {
      
                checkout scm
            }
        }
        stage('Build') {
            steps {
                echo "Building ${env.APP_NAME}..."
    
            }
        }
        stage('Test') {
            steps {
                echo "Running Tests..."

            }
        }
        stage('Deploy') {
            steps {
                echo "Deploying to Production..."
            }
        }
    }
    
    post {
        always {
            echo "Cleaning up workspace..."
        }
        success {
            echo "Pipeline finished successfully!"
        }
        failure {
            echo "Pipeline failed. Check the logs."
        }
    }
}