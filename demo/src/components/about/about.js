import angular from 'angular';
import uiRouter from 'angular-ui-router';
import aboutComponent from './about.component';
import aboutService from './about.service';
import ngSanitize from 'angular-sanitize';
require('script!tv4/tv4.js');
require('script!objectpath/lib/ObjectPath');
require('script!angular-schema-form/dist/schema-form');
require('script!angular-schema-form/dist/bootstrap-decorator');
// XXX: regular import do not work!
// import schemaForm from 'angular-schema-form/dist/schema-form';
// import 'angular-schema-form/dist/bootstrap-decorator';

let aboutModule = angular.module('about', [
  uiRouter,
  schemaForm.name
])

.config(($stateProvider) => {
  $stateProvider
    .state('about', {
      url: '/about',
      template: '<about></about>'
    });
})

.directive('about', aboutComponent)
.service('aboutService', aboutService);

export default aboutModule;
