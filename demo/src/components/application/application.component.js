import template from './application.html';
import controller from './application.controller';

let applicationComponent = function () {
  return {
    restrict: 'E',
    scope: {},
    template,
    controller,
    controllerAs: 'vm',
    bindToController: true
  };
};

export default applicationComponent;
