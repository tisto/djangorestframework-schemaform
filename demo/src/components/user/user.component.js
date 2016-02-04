import template from './user.html';
import controller from './user.controller';

let userComponent = function () {
  return {
    restrict: 'E',
    scope: {},
    template,
    controller,
    controllerAs: 'vm',
    bindToController: true
  };
};

export default userComponent;
