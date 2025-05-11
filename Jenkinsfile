pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/PPS11395193/Calculadora', branch: "main"
            }ww
        }
        stage('Unit Test') {
            steps {
                sh 'python -m unittest discover -s . -p "test_*.py"'
            }
        }
    }
}

