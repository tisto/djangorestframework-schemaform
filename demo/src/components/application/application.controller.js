class ApplicationController {

  constructor(applicationService) {
    this.name = 'Application';
    this.result = {};
    this.service = applicationService;
    this.model = {};
    this.schema = {};
    this.form = [];
    this.getSchema();
  }

  getSchema() {
    this.service.getSchema().then((res) => {
      this.schema = res;
      this.form = res.form;
    });
  }

  onSubmit(form) {
    // First we broadcast an event so all fields validate themselves
    $scope.$broadcast('schemaFormValidate');

    // Then we check if the form is valid
    if (form.$valid) {
      console.log('form is valid');
    } else {
      console.log('form is invalid');
    }
  }
}

export default ApplicationController;
