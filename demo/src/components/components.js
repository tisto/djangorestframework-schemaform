import angular from 'angular';
import Home from './home/home';
import About from './about/about';
import Contact from './contact/contact';
import ContactAddress from './contact/contact.address';
import ContactForm from './contact/contact.form';
import User from './user/user';

let componentModule = angular.module('app.components', [
  About.name,
  Contact.name,
  ContactAddress.name,
  ContactForm.name,
  Home.name,
  User.name
]);

export default componentModule;
