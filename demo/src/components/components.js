import angular from 'angular';
import Home from './home/home';
import Application from './application/application';
import Contact from './contact/contact';
import ContactAddress from './contact/contact.address';
import ContactForm from './contact/contact.form';
import User from './user/user';

let componentModule = angular.module('app.components', [
  Application.name,
  Contact.name,
  ContactAddress.name,
  ContactForm.name,
  Home.name,
  User.name
]);

export default componentModule;
