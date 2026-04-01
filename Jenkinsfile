pipeline {
    agent any

    environment {
        PYTHON_VERSION = '3.10'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Python Info') {
            steps {
                script {
                    if (isUnix()) {
                        sh 'python --version'
                    } else {
                        bat 'python --version'
                    }
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    if (isUnix()) {
                        sh '''
                            python -m pip install --upgrade pip
                            if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
                            pip install ruff pytest coverage
                        '''
                    } else {
                        bat '''
                            python -m pip install --upgrade pip
                            if exist requirements.txt pip install -r requirements.txt
                            pip install ruff pytest coverage
                        '''
                    }
                }
            }
        }

        stage('Lint with Ruff') {
            steps {
                catchError(buildResult: 'SUCCESS', stageResult: 'UNSTABLE') {
                    script {
                        if (isUnix()) {
                            sh 'ruff --output-format=github --target-version=py310 .'
                        } else {
                            bat 'ruff --output-format=github --target-version=py310 .'
                        }
                    }
                }
            }
        }

        stage('Test with Pytest + Coverage') {
            steps {
                script {
                    if (isUnix()) {
                        sh 'coverage run -m pytest -v -s'
                    } else {
                        bat 'coverage run -m pytest -v -s'
                    }
                }
            }
        }

        stage('Coverage Report') {
            steps {
                script {
                    if (isUnix()) {
                        sh 'coverage report -m'
                    } else {
                        bat 'coverage report -m'
                    }
                }
            }
        }
    }
}
