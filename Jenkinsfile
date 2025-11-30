pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t demo-f:${GIT_COMMIT} .'
            }
        }

        stage('Security Scan (Trivy)') {
            steps {
                sh '''
                    trivy image --exit-code 1 \
                        --severity HIGH,CRITICAL \
                        --format table \
                        demo-f:${GIT_COMMIT} > trivy_report.txt || true
                '''
            }
        }
    }

    post {
        success {
            echo "Build & Scan passed. Deploying."
        }
        unsuccessful {
            echo "Security scan failed. Blocking deployment."
        }
        always {
            sh 'curl -X POST -H "Content-Type: text/plain" --data-binary @trivy_report.txt $WEBEX_WEBHOOK'
        }
    }
}
