pipeline {
    agent any

    stages {
        stage('Test') {
            steps {
                sh 'python3 -m unittest discover -v'
            }
        }
    }

    post {
        always {
            withCredentials([
                string(credentialsId: 'WEBEX_TOKEN', variable: 'WEBEX_TOKEN'),
                string(credentialsId: 'WEBEX_ROOM_ID', variable: 'WEBEX_ROOM_ID')
            ]) {
                sh '''
                    curl -s -X POST https://webexapis.com/v1/messages \
                      -H "Authorization: Bearer $WEBEX_TOKEN" \
                      -H "Content-Type: application/json" \
                      -d "{\\"roomId\\": \\"$WEBEX_ROOM_ID\\", \\"markdown\\": \\"Jenkins Build **${currentBuild.currentResult}**: ${env.JOB_NAME} #${env.BUILD_NUMBER}\\"}"
                '''
            }
        }
    }
}
