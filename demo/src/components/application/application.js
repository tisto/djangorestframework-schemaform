import angular from 'angular';
import uiRouter from 'angular-ui-router';
import applicationComponent from './application.component';
import applicationService from './application.service';
import ngSanitize from 'angular-sanitize';
require('script!tv4/tv4.js');
require('script!objectpath/lib/ObjectPath');
require('script!angular-schema-form/dist/schema-form');
require('script!angular-schema-form/dist/bootstrap-decorator');
// XXX: regular import do not work!
// import schemaForm from 'angular-schema-form/dist/schema-form';
// import 'angular-schema-form/dist/bootstrap-decorator';

let applicationModule = angular.module('application', [
  uiRouter,
  schemaForm.name
])

.config(($stateProvider) => {
  $stateProvider
    .state('application', {
      url: '/application',
      template: '<application></application>'
    });
})

.directive('application', applicationComponent)
.service('applicationService', applicationService);

export default applicationModule;
