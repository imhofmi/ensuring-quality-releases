# Ensuring Quality Releases
This project demonstrates the capabilities of automated CI/CD pipelines using Azure DevOps.

The CI/CD pipeline consists of four stages:
* Stage 1. [Infrastructure](#infrastructure)
* Stage 2. [Build](#build)
* Stage 3. [Deploy](#deploy)
* Stage 4. [Test](#test)

![Pipeline overview](screenshots/S1-pipeline-overview.PNG "Pipeline Overview")

## Infrastructure

Infrastructure is described as code that is instantiated and managed by Terraform.

The Infrastructure stage uses the terraform configuration in the 'terraform' directory to perform the following tasks:

* Install Terraform
* Terraform Init
* Terraform Plan
* Terraform Apply

![Infrastructure Terraform](screenshots/S2-infrastructure-terraform.PNG "Infrastructure Terraform")

## Build

The Build stage packages the FakeRestAPI web application contained in the 'fakerestapi' directory into an artifact.

![Build Artifact](screenshots/S3-build-artifact.PNG "Build Artifact")

## Deploy

The Deploy stage deploys the artifact generated in the Build stage to the Azure AppService created in the Infrastructure stage.

![Deploy Webapp](screenshots/S4-deploy-webapp.PNG "Deploy Webapp")


## Test

The Test stage consists of performs three different steps:
* [Integration Tests](#integration-tests)
* [Performance Tests](#performance-tests)
* [UI Tests](#-ui-tests)

### Integration Tests

Integration Tests are performed to check the APIs provided by the webapp for existence (regression) and correctness (validation).

The tests were created using Postman and can be found in 'automatedtesting/postman'.

Execution within the pipeline is done via newman.

![Test Integration Regression](screenshots/S5-test-integration-regression.PNG "Test Integration Regression")

![Test Integration Validation](screenshots/S6-test-integration-validation.PNG "Test Integration Validation")

Test results are uploaded to the pipeline and are directly visible:

![Test Integration Results Publish](screenshots/S7-test-integration-results-publish.PNG "Test Integration Results Publish")

![Test Integration Results](screenshots/S8-test-integration-results.PNG "Test Integration Results")

### Performance Tests

Performance Tests ensure that the webapp can handle the expected load in different situations.

JMeter is used to perform two types of performance tests:

* Stress Test: High load during short period of time.

![Test Performance Stress](screenshots/S9-test-performance-stress.PNG "Test Performance Stress")

* Endurance Test: Constant load over long period of time.

![Test Performance Endurance](screenshots/S10-test-performance-endurance.PNG "Test Performance Endurance")

<!-- Test results are uploaded to the pipeline and are directly visible:  -->
<!-- ![Test Performance Result](screenshots/S10-test-performance-result "Test Performance Result") -->

### UI tests

UI Tests ensure that the functionality of an app works as expected.

Selenium is used to test a web shop by adding items to a cart and removing them.

![Test UI](screenshots/S11-test-ui.PNG "Test UI")


## Monitoring

### Alerting

An alert is triggered whenever too many 404 errors occur:

![Alarm Rule Graph](screenshots/S12-alarm-rule-graph.PNG "Alarm Rule Graph")

It automatically generates eMails as shown below:

![Alarm Rule eMail](screenshots/S13-alarm-rule-email.PNG "Alarm Rule eMail")

### Logging

Azure log analytics is used for the webapp http logs:

![Logs HTTP](screenshots/S14-logs-http.PNG "Logs HTTP")

And is also used for the UI test logs produced by selenium:

![Logs UI Test](screenshots/S15-logs-ui-test.PNG "Logs UI Test")