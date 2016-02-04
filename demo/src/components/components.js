import angular from 'angular';
import Application from './application/application';
import Home from './home/home';
import User from './user/user';

let componentModule = angular.module('app.components', [
  Application.name,
  Home.name,
  User.name
]);

export default componentModule;
