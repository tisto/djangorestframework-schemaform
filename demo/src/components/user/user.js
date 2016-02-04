import angular from 'angular';
import uiRouter from 'angular-ui-router';
import userComponent from './user.component';
import userService from './user.service';
import ngSanitize from 'angular-sanitize';
require('script!tv4/tv4.js');
require('script!objectpath/lib/ObjectPath');
require('script!angular-schema-form/dist/schema-form');
require('script!angular-schema-form/dist/bootstrap-decorator');
// XXX: regular import do not work!
// import schemaForm from 'angular-schema-form/dist/schema-form';
// import 'angular-schema-form/dist/bootstrap-decorator';

let userModule = angular.module('user', [
  uiRouter,
  schemaForm.name
])

.config(($stateProvider) => {
  $stateProvider
    .state('user', {
      url: '/user',
      template: '<user></user>'
    });
})

.directive('user', userComponent)
.service('userService', userService);

export default userModule;
